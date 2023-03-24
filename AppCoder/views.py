from django.shortcuts import render,redirect
from django.http import HttpResponse
from AppCoder.models import Doctor, Medicina, Paciente, Profile
from django.http.request import QueryDict
from AppCoder.forms import UserRegisterForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView

# Create your views here.
def inicio(request):
    return render(request, "AppCoder/inicio.html")

def about(request):
    return render(request, "AppCoder/about.html")
  
def buscar(request):
    if  request.GET["especialidad"]:
        especialidad = request.GET['especialidad'] 
        doctores = Doctor.objects.filter(especialidad__icontains=especialidad)
        return render(request, "AppCoder/inicio.html", {"doctores":doctores, "especialidad":especialidad})
    else:
        respuesta = "No ingresaste datos"
    return HttpResponse(respuesta)

class Login(LoginView):
    next_page = reverse_lazy('inicio')

class Logout(LogoutView):
    next_page = reverse_lazy('login')
 
def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()   
            return render(request, "AppCoder/inicio.html", {"usuario_creado":user.username})
    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request, 'registration/signup.html', context)

class DoctorList(ListView):
    model = Doctor
    context_object_name = "doctores"

class DoctorDetail(DetailView):
    model = Doctor
    context_object_name = "doctor"

class DoctorUpdate(LoginRequiredMixin, UpdateView):
    model = Doctor
    success_url = reverse_lazy("doctor-list")
    fields = '__all__'

class DoctorDelete(LoginRequiredMixin, DeleteView):
    model = Doctor
    context_object_name = "doctor"
    success_url = reverse_lazy("doctor-list")

class DoctorCreate(LoginRequiredMixin, CreateView):
    model = Doctor
    success_url = reverse_lazy("doctor-list")
    fields = '__all__'

class PacienteList(ListView):
    model = Paciente
    context_object_name = "pacientes"

class PacienteDetail(DetailView):
    model = Paciente
    context_object_name = "paciente"

class PacienteUpdate(LoginRequiredMixin, UpdateView):
    model = Paciente
    success_url = reverse_lazy("paciente-list")
    fields = '__all__'

class PacienteDelete(LoginRequiredMixin, DeleteView):
    model = Paciente
    context_object_name = "paciente"
    success_url = reverse_lazy("paciente-list")

class PacienteCreate(LoginRequiredMixin, CreateView):
    model = Paciente
    success_url = reverse_lazy("paciente-list")
    fields = '__all__'

class MedicinaList(ListView):
    model = Medicina
    context_object_name = "medicinas"

class MedicinaDetail(DetailView):
    model = Medicina
    context_object_name = "medicina"

class MedicinaUpdate(LoginRequiredMixin, UpdateView):
    model = Medicina
    success_url = reverse_lazy("medicina-list")
    fields = '__all__'

class MedicinaDelete(LoginRequiredMixin, DeleteView):
    model = Medicina
    context_object_name = "medicina"
    success_url = reverse_lazy("medicina-list")

class MedicinaCreate(LoginRequiredMixin, CreateView):
    model = Medicina
    success_url = reverse_lazy("medicina-list")
    fields = '__all__'
    
class ProfileCreate(LoginRequiredMixin, CreateView):
    model = Profile
    success_url = reverse_lazy("doctor-list")
    fields = ['avatar',]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProfileUpdate(LoginRequiredMixin, UserPassesTestMixin,  UpdateView):
    model = Profile
    success_url = reverse_lazy("doctor-list")
    fields = ['avatar',]

    def test_func(self):
        return Profile.objects.filter(user=self.request.user).exists()
