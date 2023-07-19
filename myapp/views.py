from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from django.urls import reverse_lazy
from .models import kPOP

class kPOPListView(ListView):
    model = kPOP
    context_object_name = 'groups'
    template_name = 'kPOP_list.html'

class kPOPCreateView(CreateView):
    model = kPOP
    template_name = 'kPOP_create.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('kPOP_list')

class kPOPDeleteView(DeleteView):
    model = kPOP
    template_name = 'kPOP_delete.html'
    success_url = reverse_lazy('kPOP_list')

class kPOPDetailView(DetailView):
    context_object_name = 'kPOP'
    model = kPOP
    template_name = 'kPOP_detail.html'

class kPOPUpdateView(UpdateView):
    model = kPOP
    template_name = 'kPOP_update.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('kPOP_list')
