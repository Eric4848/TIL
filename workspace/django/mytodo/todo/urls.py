from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'todo'
urlpatterns = [
    path("", views.todo_list, name='todo_list'),
    path("post/", views.todo_post, name='todo_post'),
    path("<int:pk>/", views.todo_detail, name='todo_detail'),
    path("<int:pk>/edit/", views.todo_edit, name='todo_edit'),
    path("done/", views.done_list, name='done_list'),
    path("done/<int:pk>/", views.todo_done, name='todo_done'),
    path("<int:pk>/delete/", views.todo_delete, name='todo_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
