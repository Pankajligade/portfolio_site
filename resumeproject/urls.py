"""
URL configuration for resumeproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth import views as auth_views
from core import views
from two_factor.urls import urlpatterns as tf_urls
from django.urls import path
from core.views import contact_submit


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    # path('contact/submit/', views.contact_submit, name='contact_submit'),
    path('contact-submit/', contact_submit, name='contact_submit'),

    path('serv/', include('serv.urls')),
    path('edu/', include('edu.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('maintain/', include('maintain.urls')),
    # path('account/', include(('two_factor.urls', 'two_factor'))),  # Correct inclusion of 2FA URLs
    # path('two_factor/', include(('two_factor.urls', 'two_factor'), namespace='two_factor')),  # Updated line
    # path('account/', include(('two_factor.urls'), namespace='two_factor')),
    # path('two_factor/', include(('two_factor.urls', 'two_factor'), namespace='two_factor')),
    # path('account/', include('two_factor.urls', namespace='two_factor')),  # Correct inclusion
    path('account', include(tf_urls)),
]








# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.home, name='home'),
#     path('contact/', views.contact, name='contact'),
#     path('contact/submit/', views.contact_submit, name='contact_submit'),
#     # path('account/', include('two_factor.urls', 'two_factor')),  # Add 2FA URLs here

#     path('serv/', include('serv.urls')),
#     path('edu/',include('edu.urls')),
#     path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
#     path('logout/', auth_views.LogoutView.as_view(), name='logout'),
#     path('maintain/', include('maintain.urls')),
#     path('account/', include('two_factor.urls', 'two_factor')),  # Add this line
#     path('two_factor/', include(('two_factor.urls', 'two_factor'), namespace='two_factor')),  # Updated line


# ]
