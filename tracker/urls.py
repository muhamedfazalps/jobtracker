from django.urls import path
from . import views

urlpatterns = [
    path('signup/recruiter/', views.recruiter_signup, name='recruiter_signup'),
    path('signup/jobseeker/', views.jobseeker_signup, name='jobseeker_signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
