from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
from  .views import CustomLoginView, RegisterPage, TaskCreate, TaskDelete, TaskList, TaskDetail, TaskUpdate
from django.contrib.auth.views import LogoutView

urlpatterns=[
   path('register/',RegisterPage.as_view(), name='register'),
    path('login/',CustomLoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(next_page='login'), name='logout'),
    path('',TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/',TaskDetail.as_view(),name='task'),
    path('task-create/',TaskCreate.as_view(),name='task-create'),
    path('task-update/<int:pk>/',TaskUpdate.as_view(),name='task-update'),
    path('task-delete/<int:pk>/',TaskDelete.as_view(),name='task-delete'),
]
