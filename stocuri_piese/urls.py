from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path("base/", base),
    path("cautare-model/", cautare_model, name="cautare-model"),
    path("cautare-cod-piesa/", cautare_piesa_veche, name="cautare-piesa-veche"),
    path("cauta-piesa-dupa-model/", cauta_piesa_veche, name="cauta-piesa-dupa-model"),
    path("cauta-model-dupa-cod-piesa/", cauta_model_dupa_cod_piesa, name="cauta-model-dupa-cod-piesa"),
]