from django.contrib import admin
from django.urls import path
import main.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',main.views.main, name = 'main'),
    path('about/',main.views.about, name = 'about'),
    path('result/',main.views.result, name = 'result'),

]
