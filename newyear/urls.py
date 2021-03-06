"""dailyfresh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from .views import newYear,User,asyData
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^index/$',newYear.as_view(),name='newyear'),#用户等级
    url(r'^asydata/$',asyData.as_view(),name='asydata'),
    url(r'^user/$',User.as_view(),name='user'),#用户等级
]
