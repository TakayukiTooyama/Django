from django.contrib import admin
from django.urls import include, path
from .views import helloworldfunction, HelloWorld

urlpatterns = [
    path('admin/', admin.site.urls),
    path('helloworld/', helloworldfunction),
    path('helloworld2/', HelloWorld.as_view()),
    path('v1/', include('helloworldapp.urls'))
]
