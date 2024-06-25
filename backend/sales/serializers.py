from rest_framework import serializers
from .models import Produto, VendaMaster, VendaDetalhe, Pessoa

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['codigo','tipo','referencia','unidade','empresa']

class VendaMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendaMaster
        fields = ['codigo', 'cpf_nota', 'troco', 'dinheiro', 'total']


class VendaDetalheSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendaDetalhe
        fields = ['codigo','qtd','total','qtd_devolvida']


class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = ['codigo', 'empresa', 'cnpj', 'endereco', 'municipio', 'email1', 'celular1']
