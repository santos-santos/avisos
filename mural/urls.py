from django.urls import path
from .views import lista_avisos, criar_aviso#, detalhe_aviso

urlpatterns = [
    path('', lista_avisos, name='home'),
    #path('aviso/<int:id>', detalhe_aviso, name='detalhe_aviso'),
    path('novo/', criar_aviso, name='criar_aviso'),

]