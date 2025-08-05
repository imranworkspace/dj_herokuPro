from django.contrib import admin
from django.urls import path
from studentapp.views import formview
urlpatterns = [
    path('admin/', admin.site.urls),
    path('myform/', formview),
]
