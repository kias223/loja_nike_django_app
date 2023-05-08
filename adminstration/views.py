from django.shortcuts import render
from .models import product_props, purchase_props, perfil
from django.views.generic import UpdateView, ListView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, get_object_or_404
from .forms import Postform, userform, purchaseform
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.decorators import login_required
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from rolepermissions.roles import assign_role
from rolepermissions.decorators import has_role_decorator, has_permission_decorator
from rolepermissions.mixins import HasRoleMixin
from rolepermissions.checkers import has_role


# from django.urls import reverse_lazy
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.decorators import login_required


def post_format(post):
    post_list = [
        {
            'modelo': obj.modelo,
            'preco': obj.preço,
            'img': obj.img_produto.url,
            'desconto': obj.desconto,
            'parcela': obj.parcelas,
            'id': obj.id
        }
        for obj in post
    ]

    for position, value in enumerate(post_list):
        preco = value['preco']
        preco = float(preco.replace(',', '.'))
        desconto = value['desconto']
        preco_with_descont = preco - (preco * desconto) / 100
        preco = '%.2f' % preco_with_descont
        preco = preco.replace('.', ',')
        value['preco'] = preco

    return post_list


class new_product(HasRoleMixin, CreateView):
    allowed_roles = 'adminstrador'
    model = product_props
    form_class = Postform
    template_name = 'new_product.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.autor = self.request.user
        obj.save()
        return super().form_valid(form)


@has_role_decorator('adminstrador')
def adminstration_view(request):
    posts = product_props.objects.all()
    return render(request, 'admin.html', {'posts': posts})


def excluir_post(request, id):
    posts = product_props.objects.get(id=id)
    posts.delete()
    return redirect('/adminstration')


class editar_post(HasRoleMixin, SuccessMessageMixin, UpdateView, ListView):
    allowed_roles = 'adminstrador'

    context_object_name = 'post'
    model = product_props
    form_class = Postform
    template_name = 'edit_product.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.autor = self.request.user
        obj.save()
        return super().form_valid(form)


class purchase_serializer(ModelSerializer):
    class Meta:
        model = purchase_props
        fields = '__all__'


class purchase_list(APIView):
    def post(self, request):
        serializer = purchase_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@has_role_decorator('adminstrador')
def adminstration_purchases(request):
    form = purchaseform()

    if (request.method == 'POST'):
        id = request.POST.get('post_id')
        post_user = get_object_or_404(purchase_props, id=id)
        form = purchaseform(request.POST, instance=post_user)

        if (form.is_valid()):
            post = form.save(commit=False)
            post.save()
            return redirect('adminstration_purchases')
        else:
            errro = 'nao deu certo'
            return render(request, 'adminstration_purchases.html', {'form': form, 'erro': errro})

    elif (request.method == 'GET'):
        posts = purchase_props.objects.all()
        status_aguardado_pagamento = purchase_props.objects.filter(status=None)
        status_pagamento_confirmado = purchase_props.objects.filter(
            status='pagamento confirmado')
        status_preparando_produto_para_entrega = purchase_props.objects.filter(
            status='preparando produto para entrega')
        status_produto_em_rota = purchase_props.objects.filter(
            status='produto em rota')
        status_produto_entregue = purchase_props.objects.filter(
            status='produto entregue')

        return render(request, 'adminstration_purchases.html', {
            'form': form,
            'posts': posts,
            'status01': status_aguardado_pagamento,
            'status02': status_pagamento_confirmado,
            'status03': status_preparando_produto_para_entrega,
            'status04': status_produto_em_rota,
            'status05': status_produto_entregue,
        })


@has_role_decorator('adminstrador')
def adminstration_purchases_details(request, id):
    post_props = purchase_props.objects.filter(id=id)

    for obj in post_props:
        user = obj.user_id
        modelo = obj.modelo.split(',')
        modelo_id = obj.modelo_id.split(',')
        img_url = obj.img_url.split(',')
        quantidade = obj.quantidade.split(',')
        tamanho = obj.tamanho.split(',')

    purchase_details = [
        {
            'modelo': data[0],
            'modelo_id': data[1],
            'img_url': data[2],
            'quantidade': data[3],
            'tamanho': data[4]
        }
        for data in zip(modelo, modelo_id, img_url, quantidade, tamanho)
    ]

    perfil_props = perfil.objects.filter(user=user)

    return render(request, 'adminstration_purchases_details.html', {
        'post': post_props,
        'perfil': perfil_props,
        'purchase_details': purchase_details,
    })


@login_required()
def user_perfil(request):
    post_user = get_object_or_404(perfil, user=request.user)
    form = userform(instance=post_user)

    if (request.method == 'POST'):
        form = userform(request.POST, instance=post_user)

        if (form.is_valid()):
            post = form.save(commit=False)
            post.save()

            return redirect('perfil_update')
        else:
            return render(request, 'perfil.html', {'form': form})

    elif (request.method == 'GET'):
        marca = request.GET.get('marca')
        if marca:
            posts = product_props.objects.filter(modelo__icontains=marca)
            post_list = post_format(posts)
            return render(request, 'search.html', {'posts': post_list})

        return render(request, 'perfil.html', {'form': form})


@has_role_decorator('adminstrador')
def create_admin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username, password=password)
        user.save()
        assign_role(user, 'adminstrador')
    return render(request, 'create_admin.html')


def page_admins(request):
    users = User.objects.all()
    admin_list = []
    for user in users:
        if has_role(user, 'adminstrador'):
            admin_list.append(user.username)

    return render(request, 'page_admins.html', {
        'admins': admin_list,
    })
