
from django.urls import path
from . import views


urlpatterns = [
    # path('', views.index, name= 'index'),
    path('register/', views.Register, name= 'register'),
    path('login/', views.Login, name= 'login'),
    path('logout/', views.Logout, name= 'logout'),
    path('list/', views.BlogList, name= 'bloglist'),
    path('create-blog/', views.Createblog, name= 'createblog'),
    path('update/<slug:slug>/', views.Updateblog, name= 'updateblog'),
    path('delete/<slug:slug>/', views.Deleteblog, name= 'deleteblog'),

]