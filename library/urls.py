"""
URL configuration for library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from myapp import views
from myapp.views import reports

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.adminlogin),
    path('admin_login_code/',views.admin_login_code),
    path('dashboard/',views.dashboard),
    path('manage_books/',views.manage_books),
    path('manage_books_code/',views.manage_books_code),
    path('manage_members/',views.manage_members),
    path('manage_members_code/',views.manage_members_code),
    path('manage_books_delete/<int:id>',views.manage_books_delete),
    path('manage_books_edit/<int:id>',views.manage_books_edit),
    path('manage_book_update/',views.manage_books_update),
    path('manage_members_delete/<int:id>',views.manage_members_delete),
    path('manage_members_edit/<int:id>',views.manage_members_edit),
    path('manage_members_update/',views.manage_members_update),
    path('issue_return/',views.issue_return),
    path('issue_return_code/',views.issue_return_code),
    path('return_book_code/',views.return_book_code),
    path('reports/',views.reports),
]
