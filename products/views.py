from django.shortcuts import render, redirect
from django.http import HttpResponse
from products.models import Product, Category, SubCategory, Feature, UserWishlist
from users.models import UserProfile
from django.db.models import Q
# Create your views here.
def index(request):
    if request.user.is_authenticated and UserProfile.objects.filter(user = request.user):
        row4 = Product.objects.filter(top_product = True).values()
        row2 = Product.objects.filter(category__category_name = 'Fashion').values()
        row3 = Product.objects.exclude(category__category_name = 'Watch')
        wishlist = UserWishlist.objects.filter(userprofile__username = request.user.username)
        
        list = []
        for i in wishlist:
            list.append(i.product.id)
        context = {
            'instances': row4,
            'row2': row2,
            'row3': row3,
            'onwishlist':list,
        }

        return render(request, 'index.html', context=context)
    else:
        return redirect('login')

def products(request, value):
    categories = SubCategory.objects.filter(category__category_name = value)
    product_imgs = Product.objects.filter(category__category_name = value)
    brands = Product.objects.filter(category__category_name = value).values('name').distinct()
    fields = [field.name for field in Product._meta.get_fields()]
    wishlist = UserWishlist.objects.filter(userprofile__username = request.user.username)

    list = []
    for i in wishlist:
        list.append(i.product.id)
    context = {
        'product': product_imgs,
        'brands': brands,
        'fields':fields,
        'categories':categories,
        'item':value,
        'count':len(product_imgs),
        'onwishlist':list,
        'name':request.user.first_name,
    }
    # print(list)
    return render(request, 'menswatch.html', context=context)

def singlepage(request, value):
    # print(value)
    if(Product.objects.get(id = value)):
        product = Product.objects.get(id = value)
        
        context = {
            'id':product.id,
            'name': product.name,
            'image':product.image,
            'original_price':product.original_price,
            'discount_price':product.discount_price,
            'discount':product.discount,
            'subcategory':product.subcategory.name,
            'category':product.category.category_name,
            'stock':product.stock,
            'package_contents':product.package_contents,
            'rating':product.rating,
           
        }
        print(product)
        return render(request, 'singlepage.html', context=context)


def sample(request):
    instances = Product.objects.all().values()
    features = Feature.objects.all().values()
    context = {
        'instances': instances,
    }
    
    return render(request, 'sample.html', context=context)