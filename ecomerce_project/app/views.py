
from django.shortcuts import render
from django.views import View
from .models import Customer,Product
from .forms import CustomerRegistrationForm ,CustomerProfileForm
from math import ceil
def base(request):
    return render(request,'app/base.html')

#def home(request):
   # return render(request,'app/home.html')
class ProductView(View):
    def get(self,request):
        topwears=Product.objects.filter(category='TW')
        bottomwears = Product.objects.filter(category='BW')
        mobiles = Product.objects.filter(category='M')
        return render(request,'app/home.html',{'topwears':topwears,'bottomwears':bottomwears,'mobiles':mobiles})


class ProductDetailView(View):
    def get(self,request,pk):
        product=Product.objects.get(pk=pk)
        return render(request,'app/product_details.html',{'product':product})

def add_to_cart(request):
    return render(request,'app/add_to_cart.html')

def buy_now(request):
    return render(request,'app/buy_now.html')

class ProfileView(View):
    def get(self,request):
        form=CustomerProfileForm()
        return render(request,'app/profile.html',{'form':form,'active':'btn-primary'})
    def post(self,request):
        form=CustomerProfileForm(request.POST)
        if form.is_valid():
            usr=request.user()
            name=form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode=form.cleaned_data['zipcode']
            reg=Customer(user=usr,name=name,locality=locality,city=city,state=state,zipcode=zipcode)
            reg.save()
            return render(request, 'app/profile.html', {'form': form, 'active': 'btn-primary'})
#def address(request):
    #return render(request,'app/address.html')

def orders(request):
    return render(request,'app/orders.html')

def product_details(request):
    return render(request,'app/product_details.html')

def mobile(request,data=None):
    if data==None:
        mobiles=Product.objects.filter(category='M')
    elif data == 'Redmi' or data=='Samsung':
        mobiles = Product.objects.filter(category='M').filter(brand=data)
    return render(request,'app/mobile.html',{'mobiles':mobiles})


class CustomerRegistrationView(View):
    def get(self,request):
        form=CustomerRegistrationForm()
        return render(request,'app/customerregistration.html',{'form':form})
    def post(self,request):
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'app/customerregistration.html', {'form': form})


def searchMatch(query,item):
    if query in item.desc.lower() or query in item.title or query in item.category:
        return True
    return False





def Recommendation(request):
        query = request.GET.get('Product_id')
        products = Product.objects.filter(name__icontains=query)
        return render(request, 'app/recommendation.html', {'products': products})

def searchMatch(query,item):

    if query in item.category or query in item.id:
        return True
    else:
        return False

def search(request):
    query = request.GET.get('search')
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) != 0:
            allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds, "msg": ""}
    if len(allProds) == 0 or len(prod)<4:
        params = {'msg': "Please make sure to enter relevant search query"}
    return render(request, 'app/search.html', params)
