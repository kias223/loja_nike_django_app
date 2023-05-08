from django.shortcuts import render
from adminstration.models import perfil
from django.views import generic
from django.urls import reverse_lazy
from .forms import user_creation_from_with_email
# Create your views here.

class signup_view(generic.CreateView):
    form_class = user_creation_from_with_email
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

    def form_valid(self, form):
        url = super().form_valid(form)
        self.object.save()
        perfil.objects.create(user= self.object)
        return url