from django.urls import path
from AppCoder import views , forms
#from AppCoder.views import (Login, Logout, SignUp)
from AppCoder.views import (Login, Logout, DoctorList,DoctorDetail,DoctorUpdate,DoctorDelete,DoctorCreate,PacienteList,PacienteDetail,PacienteUpdate,PacienteDelete,PacienteCreate,MedicinaList,MedicinaDetail,MedicinaUpdate,MedicinaDelete,MedicinaCreate,ProfileCreate,ProfileUpdate)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('', views.inicio, name="inicio"),
   path('about', views.about, name="about"),
   path('doctor/list', DoctorList.as_view(), name="doctor-list"),
   path('doctor/<pk>/detail', DoctorDetail.as_view(), name="doctor-detail"),
   path('doctor/<pk>/update', DoctorUpdate.as_view(), name="doctor-update"),
   path('doctor/<pk>/delete', DoctorDelete.as_view(), name="doctor-delete"),
   path('doctor/create', DoctorCreate.as_view(), name="doctor-create"),
   path('paciente/list', PacienteList.as_view(), name="paciente-list"),
   path('paciente/<pk>/detail', PacienteDetail.as_view(), name="paciente-detail"),
   path('paciente/<pk>/update', PacienteUpdate.as_view(), name="paciente-update"),
   path('paciente/<pk>/delete', PacienteDelete.as_view(), name="paciente-delete"),
   path('paciente/create', PacienteCreate.as_view(), name="paciente-create"),
   path('medicina/list', MedicinaList.as_view(), name="medicina-list"),
   path('medicina/<pk>/detail', MedicinaDetail.as_view(), name="medicina-detail"),
   path('medicina/<pk>/update', MedicinaUpdate.as_view(), name="medicina-update"),
   path('medicina/<pk>/delete', MedicinaDelete.as_view(), name="medicina-delete"),
   path('medicina/create', MedicinaCreate.as_view(), name="medicina-create"),
   path('profile/create', ProfileCreate.as_view(), name="profile-create"),
   path('profile/<pk>/update', ProfileUpdate.as_view(), name="profile-update"),
   path('login/', Login.as_view(), name="login"),
   path('logout/', Logout.as_view(), name="logout"),
   #path('signup/', SignUp.as_view(), name="signup"),
   path('signup/', views.signup, name="signup"),
   path('buscar/', views.buscar),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)