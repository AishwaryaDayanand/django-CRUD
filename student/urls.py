from django.urls import path
from .import views as stud_views


urlpatterns = [
    path('', stud_views.form, name='form' ),
    path('<int:id>/', stud_views.form, name='update' ),
    path('delete/<int:id>/', stud_views.delete, name='delete' ),
    path('list/', stud_views.list, name='list' ),
]
