from django.urls import path

from dinofacts.views import show_dino


urlpatterns = [
    path("show_dino/<str:name>/", show_dino),
]
