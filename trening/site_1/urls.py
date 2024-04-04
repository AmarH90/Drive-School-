from django.urls import path
from . import views 


urlpatterns = [
    path("Drive-school", views.check_1, name="check_1"),
    path("services", views.check_2, name="check_2"),
    path("Teachers",views.check_3, name="check_3"),
    path("Gallery", views.check_4, name="check_4"),
    path("About", views.check_5,  name="check_5"),
    path("Contact", views.check_6, name="check_6"),
    path("graduation", views.check_7, name="check_7"),
    path("notifications", views.check_8, name="check_8"),
    path("education", views.check_9, name="check_9"),
    path("registrations", views.register, name="register"),
    #path('submit-form', views.submit_form, name='submit_form'),
    #path('submit', views.submit_form, name='submit_form'),
    #path('register', views.register, name='register'),
]


