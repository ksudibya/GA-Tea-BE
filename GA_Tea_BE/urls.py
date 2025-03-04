from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from GA_Tea.views import AccountViewSet, PostViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register(r'account', AccountViewSet)
router.register(r'post', PostViewSet)
router.register(r'comment', CommentViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls)
]