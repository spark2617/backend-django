from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics
from .models import Produto, VendaMaster, VendaDetalhe,Pessoa
from .serializers import ProdutoSerializer, VendaMasterSerializer, VendaDetalheSerializer,PessoaSerializer
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status



# =====================PRODUTO=====================


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def produto_list(request):
    if request.method == 'GET':
        produtos = Produto.objects.all()
        serializer = ProdutoSerializer(produtos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProdutoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((permissions.AllowAny,))
def produto_detail(request, pk):
    try:
        produto = Produto.objects.get(pk=pk)
    except Produto.DoesNotExist:
        return Response({"mensagem": "Produto não encontrado na base dados!"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProdutoSerializer(produto)
        return Response(serializer.data)

    elif request.method == 'PUT':

        serializer = ProdutoSerializer(produto, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        produto.delete()
        return Response({"mesagem": "Produto deletado da base de dados com sucesso!"}, status=status.HTTP_204_NO_CONTENT)




#=======================VENDA MASTER============================


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def vendasMaster_list(request):
    if request.method == 'GET':
        vendas = VendaMaster.objects.all()
        serializer = VendaMasterSerializer(vendas, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = VendaMasterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((permissions.AllowAny,))
def vendasMaster_detail(request, codigo):
    try:
        venda = VendaMaster.objects.get(codigo=codigo)
    except VendaMaster.DoesNotExist:
        return Response({"message": "Venda não encontrada!"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VendaMasterSerializer(venda)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = VendaMasterSerializer(venda, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        venda.delete()
        return Response({"mesagem": "Venda Master deletado da base de dados com sucesso!"}, status=status.HTTP_204_NO_CONTENT)
    

#===========================VENDAS DETALHE==================================================

@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def vendasDetalhe_list(request):
    if request.method == 'GET':
        vendas_detalhe = VendaDetalhe.objects.all()
        serializer = VendaDetalheSerializer(vendas_detalhe, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = VendaDetalheSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((permissions.AllowAny,))
def vendasDetalhe_detail(request, codigo):
    try:
        venda_detalhe = VendaDetalhe.objects.get(codigo=codigo)
    except VendaDetalhe.DoesNotExist:
        return Response({"message": "Venda detalhe não encontrado!"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VendaDetalheSerializer(venda_detalhe)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = VendaDetalheSerializer(venda_detalhe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        venda_detalhe.delete()
        return Response({"mesagem": "Venda detalhe deletado da base de dados com sucesso!"}, status=status.HTTP_204_NO_CONTENT)
    

#===========================Pessoa===============================

@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def pessoa_list(request):
    if request.method == 'GET':
        pessoas = Pessoa.objects.all()
        serializer = PessoaSerializer(pessoas, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PessoaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((permissions.AllowAny,))
def pessoa_detail(request, pk):
    try:
        pessoa = Pessoa.objects.get(pk=pk)
    except Pessoa.DoesNotExist:
        return Response({"message": "Pessoa não encontrada!"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PessoaSerializer(pessoa)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PessoaSerializer(pessoa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        pessoa.delete()
        return Response({"mesagem": "Pessoa deletado da base de dados com sucesso!"}, status=status.HTTP_204_NO_CONTENT)