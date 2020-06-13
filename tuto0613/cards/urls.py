from cards import views
from rest_framework.routers import DefaultRouter
from cards.views import CardViewSet, UserViewSet

routers = DefaultRouter()

routers.register(r'users', views.UserViewSet)
routers.register(r'users/<int:pk>', views.UserViewSet)
routers.register(r'cards', views.CardViewSet)
routers.register(r'cards/<int:pk>', views.CardViewSet)

urlpatterns = routers.urls
