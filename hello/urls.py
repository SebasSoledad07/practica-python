from django.urls import path
from hello import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),

    

    
]
urlpatterns += staticfiles_urlpatterns()
