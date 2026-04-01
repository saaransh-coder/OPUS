"""
URL configuration for finance_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from tracker import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),   # homepage
    path('api/transactions/',views.get_transactions,name='get_transactions'),
    path('api/add/',views.add_transaction,name='add_transaction'),
    path('api/delete/<int:id>/',views.delete_transaction,name='delete_transaction'),
    
]
