"""registration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf import settings
from apps.views import gmail,homepage,login,relogin,newuser

urlpatterns = [
    path('gmail/', gmail, name="gmail"),
    path('home', homepage, name="homepage"),
    path('login/', login, name="login"),
    path('relogin/', relogin, name="relogin"),
    path('new/', newuser, name="newuser")
    
]


