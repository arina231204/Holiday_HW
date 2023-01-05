from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.urls import path, include

from rest_framework import routers
from accounts import views as acc_views
from  rest_framework.authtoken import views as auth_views

from posts import views
from posts.models import Tweet

router = routers.DefaultRouter()
router.register('tweet', views.TweetViewSet),
router.register('comment', views.CommentViewSet),


ac_router = routers.DefaultRouter()
ac_router.register('account', acc_views.AuthorViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include(ac_router.urls)),
    path('api/token/', auth_views.obtain_auth_token),


    path('api/tweet/all/', views.TweetListAPIView.as_view(), name='all_tweet'),
    path('api/comment/all/', views.CommentListAPIView.as_view()),

    path('api/', include(router.urls)),

]
