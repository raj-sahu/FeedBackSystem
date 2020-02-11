"""webapp URL Configuration

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
from django.contrib import admin
from django.urls import path
from test1 import views






















admin.site.site_header = 'FeedBack System Admin'                    # default: "Django Administration"
admin.site.index_title = 'Features area'                 # default: "Site administration"
admin.site.site_title = 'Admin Site' # default: "Django site admin"

urlpatterns = [
    path('', views.index,name='index'),
    path('review/', views.review),
    path('admin/', admin.site.urls),
    path('logout/', views.user_logout, name='logout'),
    path('special/', views.special, name='special'),
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login')
]
