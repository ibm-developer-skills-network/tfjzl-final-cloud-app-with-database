from django.urls import path
from . import views

app_name = 'onlinecourse'

urlpatterns = [
    path(
        'course/<int:pk>/review/',
        views.submit_review,
        name='submit_review'
    ),
]