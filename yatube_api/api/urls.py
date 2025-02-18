from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import (
    FollowViewSet,
    PostViewSet,
    CommentViewSet,
    GroupViewSet,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

router = DefaultRouter()
router.register('v1/posts', PostViewSet, basename='posts')
router.register('v1/groups', GroupViewSet, basename='groups')
router.register('v1/follow', FollowViewSet, basename='follow')
router.register(
    r'v1/posts/(?P<post_id>\d+)/comments',  # Добавляем полный путь
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('', include(router.urls)),
    path('v1/jwt/create/', TokenObtainPairView.as_view()),
    path('v1/jwt/refresh/', TokenRefreshView.as_view()),
    path('v1/jwt/verify/', TokenVerifyView.as_view()),
]
