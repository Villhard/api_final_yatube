from django.urls import path, include
from rest_framework.routers import SimpleRouter
from api.views import PostViewSet


router_v1 = SimpleRouter()
router_v1.register(r"posts", PostViewSet)

urlpatterns = [
    path("v1/", include(router_v1.urls)),
    path("v1/", include("djoser.urls.jwt"))
]
