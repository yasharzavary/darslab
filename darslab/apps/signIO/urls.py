from django.urls import path
import apps.signIO.views as view

urlpatterns = [
    path('sign_in', view.signI, name='sign-in'),
    path('sign_out', view.signU, name='sign-out'),
]
