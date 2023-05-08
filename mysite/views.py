from django.shortcuts import render
from adminstration.models import product_props, purchase_props, perfil
from django.shortcuts import redirect
from .forms import PurchaseForm
import random
from django.contrib.auth.decorators import login_required
from datetime import datetime




from rest_framework.views import APIView


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


def home(request):
    marca = request.GET.get('marca')
    if marca:
        posts = product_props.objects.filter(modelo__icontains=marca)
        post_list = post_format(posts)

        return render(request, 'search.html', {'posts': post_list})

    posts = product_props.objects.all()
    post_list = post_format(posts)

    date = datetime.now()
    year = date.year
    post_list02 = product_props.objects.filter(data_lançamento__icontains=year)
    post_list02 = post_format(post_list02)
    post_random_list = []

    i = 0
    while i < 4:
        i = i + 1
        post_random = random.choice(post_list02)
        post_random_list.append(post_random)
        post_list02.remove(post_random)

    return render(request, 'index.html', {
        'posts': post_list,
        'banners': post_random_list
    })

#
# def promotions(request):
#         marca = request.GET.get('marca')
#         if marca:
#                 posts = product_props.objects.filter(modelo__icontains=marca)
#                 post_list = post_format(posts)
#
#                 return render(request, 'search.html', {'posts': post_list})
#
#         posts = product_props.objects.all()
#         post_list = post_format(posts)

#        return render(request, 'promotions.html',{'posts': post_list})


def product(request, id):
    posts = product_props.objects.filter(id=id)

    for obj in posts:
        preco_descont = {
            'preco': obj.preço,
            'desconto': obj.desconto
        }

    pd = float(preco_descont['preco'].replace(',', '.'))
    pd = pd - (pd * preco_descont['desconto']) / 100
    pd = '%.2f' % pd
    pd = pd.replace('.', ',')

    marca = request.GET.get('marca')
    if marca:
        posts = product_props.objects.filter(modelo__icontains=marca)
        post_list = post_format(posts)
        return render(request, 'search.html', {'posts': post_list})

    return render(request, 'product.html', {'post_props': posts,
                                            'preco': pd
                                            })


def cart(request):
    marca = request.GET.get('marca')
    if marca:
        posts = product_props.objects.filter(modelo__icontains=marca)
        post_list = post_format(posts)
        return render(request, 'search.html', {'posts': post_list})

    return render(request, 'cart.html')


@login_required
def purchase(request):
    user_props = perfil.objects.filter(user=request.user)
    return render(request, 'purchase.html', {'user_props': user_props})


# def cancel_user_purchase(request, id):
#         user_props = purchase_props.objects.get(id=id)
#         user_props.delete()
#         return redirect('user_purchase')


@login_required
def user_purchase(request):
    marca = request.GET.get('marca')
    if marca:
        posts = product_props.objects.filter(modelo__icontains=marca)
        post_list = post_format(posts)
        return render(request, 'search.html', {'posts': post_list})

    posts = purchase_props.objects.filter(user_id=request.user.id)

    purchase_details = [
        {
            'preco_total': obj.preco_total,
            'modelo': obj.modelo.split(','),
            'modelo_id': obj.modelo_id.split(','),
            'img_url': obj.img_url.split(','),
            'quantidade': obj.quantidade.split(','),
            'tamanho': obj.tamanho.split(','),
            'id': obj.id,
            'data_hora': obj.data_hora,
            'status': obj.status,
            'parcelas': obj.valor_parcelas
        }
        for obj in posts
    ]

    for position, element in enumerate(purchase_details):
        element['props'] = ''
        for x in zip(
            element['modelo'],
            element['modelo_id'],
            element['img_url'],
            element['quantidade'],
            element['tamanho'],
        ):

            element['props'] += f'''
                        <div class="purchase_props">
                            <div class="purchase_img_product">
                                <img src="{x[2]}">
                                <a href="http://127.0.0.1:8000/product/{x[1]}">ver na loja</a>
                            </div>
                            <div class="purchase_informations">
                                <p>{x[0]}</p>
                                <p>tamanho: {x[4]}</p>
                                <p>quantidade: {x[3]}</p>
                            </div>
                        </div>
'''

    return render(request, 'user_purchase.html', {'purchase_details': purchase_details})
