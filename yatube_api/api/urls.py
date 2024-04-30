from django.urls import path, include
from rest_framework.routers import SimpleRouter
from api.views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet


router_v1 = SimpleRouter()
router_v1.register(r"posts", PostViewSet)
router_v1.register(
    r"posts/(?P<post_id>\d+)/comments", CommentViewSet, basename="comments"
)
router_v1.register(r"groups", GroupViewSet)
router_v1.register(r"follow", FollowViewSet, basename="follow")

urlpatterns = [
    path("v1/", include(router_v1.urls)),
    path("v1/", include("djoser.urls.jwt")),
]
