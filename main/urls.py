from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('courses/', views.courses, name='courses'),
    path('allcourse/', views.allcourse, name='allcourse'),
    path('course/<int:id>/', views.course_detail, name='course_detail'),
    path('service-booking/', views.service_booking, name='service_booking'),
    # path('live-demo/', views.live_demo, name='live_demo'),
    path('services/', views.services, name='services'),
    path('services/<int:pk>/', views.service_detail, name='service_detail'),
    path('contact/', views.contact, name='contact'),
    path('placement/', views.placement, name='placement'),
    path('careers/', views.career_list, name='careers'),
    path('careers/<int:pk>/', views.career_detail, name='career_detail'),
    path('careers/<int:pk>/apply/', views.apply_job, name='apply_job'),
    path("demo-booking/", views.demo_booking, name="demo_booking"),
    path("demo-request/", views.demo_request, name="demo_request"),
    path('book-course/<int:id>/', views.book_course, name="book_course"),
    path('reviews/', views.review_page, name='reviews'),
    path('workshops/', views.workshop_gallery, name='workshops'),
    path('certificates/', views.certificate_gallery, name='certificates'),
    path('internships/', views.internship_list, name='internship_list'),
    path('internships/<int:pk>/', views.internship_detail, name='internship_detail'),
    path("workshop-registration/",views.workshop_registration,name="workshop_registration"),
]    

#if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)