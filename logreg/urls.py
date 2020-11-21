from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('success', views.success),
    path('logout', views.logout),
    path('process_message', views.post_mess),
    path('add_comment/<int:id>', views.post_comment),
    path('user_profile/<int:id>', views.profile),
    path('like/<int:id>', views.add_like),
    path('delete/<int:id>', views.destroy),
    path('edit/<int:id>', views.user_edit),
    path('process_edit/<int:id>', views.process_edit),
    path('edit_my_account', views.edit_my_account),
    ]