from django.shortcuts import render, get_object_or_404, redirect
from .models import Photo
from .forms import PhotoForm

# Create your views here.


def photo_list(request):
    photo = Photo.objects.all()
    return render(request, 'photo/photoList.html', {'photos': photo})


def photo_detail(request, pk):
    selectedPhoto = get_object_or_404(Photo, id=pk)
    return render(request, 'photo/detail.html', {'sp': selectedPhoto})


def photo_post(request):
    pass


def photo_edit(request, pk):
    selectedPhoto = get_object_or_404(Photo, id=pk)
    if request.method == "GET":
        form = PhotoForm(instance=selectedPhoto)
        return render(request, 'photo/edit.html', {'form': form})
    elif request.method == "POST":
        form = PhotoForm(request.POST, instance=selectedPhoto)
        if form.is_valid():
            selectedPhoto = form.save(commit=False)
            selectedPhoto.save()
            return redirect('photo_detail', pk=selectedPhoto.id)
