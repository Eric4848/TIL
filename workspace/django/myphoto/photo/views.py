from django.shortcuts import render, get_object_or_404, redirect
from .models import Photo
from .forms import PhotoForm
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.http import HttpResponse

# Create your views here.


def photo_list(request):
    photo = Photo.objects.all()
    return render(request, 'photo/photoList.html', {'photos': photo})


def photo_detail(request, pk):
    selectedPhoto = get_object_or_404(Photo, id=pk)
    return render(request, 'photo/detail.html', {'sp': selectedPhoto})


def photo_post(request):
    if request.method == "GET":
        form = PhotoForm()
        return render(request, 'photo/post.html', {'form': form})
    elif request.method == "POST":
        form = PhotoForm(request.POST)
        if form.is_valid:
            photo = form.save(commit=False)
            photo.save()

            upload_file = request.FILES['imagefile']
            upload = default_storage.save(upload_file.name,ContentFile(upload_file.read()))
            Photo.objects.filter(id=id).update(imagefile=upload_file)

            return redirect('photo_detail', pk=id)


def photo_edit(request, pk):
    selectedPhoto = get_object_or_404(Photo, id=pk)
    if request.method == "GET":
        form = PhotoForm(instance=selectedPhoto)
        return render(request, 'photo/post.html', {'form': form})
    elif request.method == "POST":
        form = PhotoForm(request.POST, instance=selectedPhoto)
        if form.is_valid():
            selectedPhoto = form.save(commit=False)
            selectedPhoto.save()

            upload_file = request.FILES['imagefile']
            upload = default_storage.save(upload_file.name,ContentFile(upload_file.read()))
            Photo.objects.filter(id=id).update(imagefile=upload_file)

            return redirect('photo_detail', pk=id)
        else:
            return redirect('photo/post.html')
    else:
        return redirect('photo/post.html')

def photo_delete(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    photo.delete()
    # Photo.objects.get(id = pk).delete()
    photos = Photo.objects.all()
    return redirect('photo_list')
    
def download_proc(request, filename):
    return HttpResponse(default_storage.open(filename).read(),
    content_type='apllication/force-download')