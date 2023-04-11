
from django.urls import path
from test_app.views import EntityViewSet


urlpatterns = [
        path('entity/', 
             EntityViewSet.as_view({'get': 'list',
                                    'post': 'create'})),
]

