from django.urls import path
import apps.account.views as view


urlpatterns = [
    path('account/', view.register, name='acc'),
    path('log_in/', view.login, name='log_int'),
]
