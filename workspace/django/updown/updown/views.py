from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def upload_proc(request):
    upload_file = request.FILES['upload_file']
    upload = default_storage.save(
        upload_file.name, ContentFile(upload_file.read()))

    return redirect('index')
# default_storage : settings.py에서 설정한 MEDIA_ROOT = BASE_DIR/media로 지정
# pload_file.name : random을 파일명에 더해서 올림 (덮어쓰기 방지)


def download(request):
    return render(request, 'download.html')


def download_proc(request, filename):
    return HttpResponse(default_storage.open(filename).read(),
                        content_type='application/force-download')
# content_type='application/force-download' => 다운로드 할 수 있도록 해준다.
