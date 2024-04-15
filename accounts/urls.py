"""Define padroes de URL para contas"""

from django.urls import path, include

app_name = 'accounts'
urlpatterns=[
    #inclui URLs de autentificação default
    path('', include('django.contrib.auth.urls')),
]