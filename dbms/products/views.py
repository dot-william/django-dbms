from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from .models import Product
from .forms import ProductCreate

# Create your views here.
def home(request):
    template = loader.get_template("products/home.html")
    actions = []
    
    add_product_form = ProductCreate(request.POST or None)  # This is only for adding new products
    products = Product.objects.all()

    for product in products:
        edit_product_form= ProductCreate(request.POST or None, instance=product)  # Separate form for editing
        actions.append({
            'edit_form': edit_product_form,
            'product': product
        })

    context =  {'add_product_form': add_product_form,  # Separate form for adding new products
                'products': products,
                'actions': actions}

    return HttpResponse(template.render(context, request))


# Create
def add_product(request):
    print("In add product")
    form = ProductCreate()
    if request.method == 'POST':
        form = ProductCreate(request.POST)
        if form.is_valid():
            form.save()
            form = ProductCreate()  # Clear form
            return redirect('home')
        else:
            return HttpResponse('''Form is invalid, please reload the page''')
    else:
        return redirect('home')
    

# Update a specific product
def update_product(request, prod_id):
    try:
        prod_id = int(prod_id)
        product = Product.objects.get(prod_id=prod_id)
    except Product.DoesNotExist:
        return redirect('home')

    edit_product_form = ProductCreate(request.POST or None, instance = product)
    if edit_product_form.is_valid():
        product.save()
        return redirect('home')
    else:
        print(edit_product_form.errors)
        return HttpResponse('''Invalid form''')
    


# Delete a specific product
def delete_product(request, prod_id):
    try:
        prod_id = int(prod_id)
        product = Product.objects.get(prod_id=prod_id)
    except Product.DoesNotExist:
        return redirect('home')

    product.delete()
    
    return redirect('home')