"""Proyecto_V2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from django.urls import path
from paginas.views import HomePageView, AboutPageView, AndroidPageView, CPageView, HtmlPageView, IosPageView, JavaPageView

urlpatterns = [
   path('',HomePageView.as_view(), name='index'),
   path('about',AboutPageView.as_view(), name='about'),

   path('android',AndroidPageView.as_view(), name='android'),
   path('C',CPageView.as_view(), name='C'),
    path('Java',JavaPageView.as_view(), name='Java'),
 
   path('html',HtmlPageView.as_view(), name='html'),
   path('ios',IosPageView.as_view(), name='ios'),
]
