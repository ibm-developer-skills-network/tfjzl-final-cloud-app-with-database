from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'onlinecourse'

urlpatterns = [
    # Liste des cours
    path('', views.CourseListView.as_view(), name='index'),

    # Authentification
    path('registration/', views.registration_request, name='registration'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),

    # Détail d’un cours
    path('<int:pk>/', views.CourseDetailView.as_view(), name='course_details'),

    # Inscription à un cours
    path('<int:course_id>/enroll/', views.enroll, name='enroll'),

    # Soumission de l’examen
    path('<int:course_id>/submit/', views.submit, name='submit'),

    # Affichage des résultats de l’examen
    path('course/<int:course_id>/submission/<int:submission_id>/result/', views.show_exam_result, name='show_exam_result'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

