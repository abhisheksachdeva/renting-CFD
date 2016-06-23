"""CFD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from renting import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users/reg/$', views.RegUser.as_view()),
    url(r'^user/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='myuser-detail'),
    url(r'^login/', views.Login.as_view()),
    url(r'^token/', views.TokenView.as_view()),
    url(r'^posts/', views.PostList.as_view()),
    # url(r'^book/(?P<pk>[0-9]+)/$', views.BookDetail.as_view(), name='book-detail'),
    # url(r'^notifications/', views.NotificationsList.as_view()),
    # url(r'^search/', views.SearchBookList.as_view()),
    
]
