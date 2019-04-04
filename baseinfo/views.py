from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from .forms import *

# Create your views here.
class home_view(TemplateView):
    template_name='home.html'

def orgnizations_view(request,*args,**kwargs):
    render(request,'organizations.html',{})

class AddOrganizationView(FormView):
    template_name='input_form.html'
    form_class=EmployerForm
    success_url='/organizations/'
    def form_valid(self, form):
        form.save_record()
        return super().form_valid(form)

class AddEmployeeStatusView(FormView):
    template_name='input_form.html'
    form_class=EmployeeStatusForm
    success_url='/success/'
    def form_valid(self, form):
        form.save_record()
        return super().form_valid(form)

class AddWorkStatusView(FormView):
    template_name='input_form.html'
    form_class=WorkStatusForm
    success_url='/success/'
    def form_valid(self, form):
        form.save_record()
        return super().form_valid(form)

class AddMaritalStatusView(FormView):
    template_name='input_form.html'
    form_class=MaritalStatusForm
    success_url='/success/'
    def form_valid(self, form):
        form.save_record()
        return super().form_valid(form)
        
class AddBankView(FormView):
    template_name='input_form.html'
    form_class=BankForm
    success_url='/success/'
    def form_valid(self, form):
        form.save_record()
        return super().form_valid(form)

class AddWorkGroupView(FormView):
    template_name='input_form.html'
    form_class=WorkGroupForm
    success_url='/success/'
    def form_valid(self, form):
        form.save_record()
        return super().form_valid(form)

class AddWorkPlaceView(FormView):
    template_name='input_form.html'
    form_class=WorkPlaceForm
    success_url='/success/'
    def form_valid(self, form):
        form.save_record()
        return super().form_valid(form)

class AddPostPlaceView(FormView):
    template_name='input_form.html'
    form_class=PostPlaceForm
    success_url='/success/'
    def form_valid(self, form):
        form.save_record()
        return super().form_valid(form)

class AddEmployeeView(FormView):
    template_name='input_form.html'
    form_class=EmployeeForm
    success_url='/success/'
    def form_valid(self, form):
        form.save_record()
        return super().form_valid(form)