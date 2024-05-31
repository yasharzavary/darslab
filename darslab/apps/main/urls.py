from django.urls import path
import apps.main.views as view


urlpatterns = [
    path('', view.index, name='main-index')
]
