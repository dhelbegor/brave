from django.urls import include, path


app_name = 'api'
urlpatterns = [
    path('core/', include('apps.core.api.urls', namespace='core')),
]
