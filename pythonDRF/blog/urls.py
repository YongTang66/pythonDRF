from django.urls import path

from blog.views import PostList, PostUpdate

urlpatterns = [
    path('<int:pk>/', PostUpdate.as_view(), name='post_update'),
    path('', PostList.as_view(), name='post_list'),
]

from rest_framework.routers import DefaultRouter
from blog.views import PostViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'blog', PostViewSet)
router.register(r'comment', CommentViewSet)
urlpatterns += router.urls
