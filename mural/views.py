from django.shortcuts import render, get_object_or_404, redirect
from .models import Aviso
from .forms import AvisoForm


def lista_avisos(request):
    """Exibe todos os avisos, agora usando o filtro por ForeignKey."""
    avisos = Aviso.objects.all().order_by('-data_criacao')
    
    # O filtro agora busca pelo ID ou Slug da categoria #
    # Exemplo: ?categoria=1 (filtra pelo ID da categoria) 
    categoria_id = request.GET.get('categoria')
    if categoria_id:
        avisos = avisos.filter(categoria_id=categoria_id)
    return render(request, 'mural/lista_avisos.html', {'avisos': avisos})




def detalhe_aviso(request, id):
    """Busca o aviso e o Django automaticamente traz a categoria relacionada."""
    aviso = get_object_or_404(Aviso, id=id)
    return render(request, 'mural/detalhe_aviso.html', {'aviso: aviso'})

def criar_aviso(request):
    """O MdelForm irá gerar automaticamente um <select> com as Categorias"""
    if request.method == "POST":
        form = AvisoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AvisoForm()
    return render(request, 'mural/form_aviso.html', {'form': form})    

