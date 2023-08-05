from django.contrib import admin
from django.urls import path
from index.views import save,process_form


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', save, name='save'),
    path('process_form/', process_form, name='process_form'),
]
