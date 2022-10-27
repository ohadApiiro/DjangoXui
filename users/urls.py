from django.conf.urls import url
import views
from urls import urlpatterns

xui_urlpatterns = [
    url(r'^cloud_cost/',
        views.cloud_cost,
        name='cloud_cost'),
]

urlpatterns.extend(xui_urlpatterns)