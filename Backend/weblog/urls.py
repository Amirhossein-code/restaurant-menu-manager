from django.urls import path, include
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()


urlpatterns = router.urls
