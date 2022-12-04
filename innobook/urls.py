from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from contacts.views import ContactsViewSet

router = DefaultRouter()
router.register('contacts', ContactsViewSet, basename='contacts')


urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += router.urls
