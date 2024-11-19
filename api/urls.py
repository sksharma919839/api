from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r"about", aboutView, basename="aboutView")

prouter = DefaultRouter()
prouter.register(r"projecthome", projectHomeView, basename="projecthome")

phrouter = DefaultRouter()
phrouter.register(r"project", projectView, basename="project")

cvrouter = DefaultRouter()
cvrouter.register(r"cv", cvView, basename="cv")

urlpatterns = [
    path("contact/", contact_view, name="contact"),
    path("", include(cvrouter.urls)),
    path("", include(prouter.urls)),
    path("", include(phrouter.urls)),
    path("", include(router.urls)),
]
