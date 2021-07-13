from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from carros.models import Carro
from django.urls import reverse_lazy



class IndexList(ListView):
    model = Carro
    template_name = 'index.html'
    paginate_by = 10


class CreateCarro(CreateView):
    model = Carro
    fields = '__all__'
    template_name = 'form/form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Adicionar novo carro'
        context['botao'] = 'adicionar novo carro'
        return context

class UpdateCarro(UpdateView):
    model = Carro 
    fields = '__all__'
    template_name = 'form/form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Edite o carro abaixo'
        context['botao'] = 'Editar'
        return context

class DeleteCarro(DeleteView):
    model = Carro 
    template_name = 'form/form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['paragrafo'] = 'Deseja Excluir este registro permanentemente?'
        context['botao'] = 'Deletar carro'
        return context