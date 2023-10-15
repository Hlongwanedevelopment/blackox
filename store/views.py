import json
from django import forms
from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from django.core.mail import send_mail, BadHeaderError
from website.models import Post
from store.models import OrderModel, Breed, Cattle_Stock, Sheep_Stock, Item, StoreItem
from django.contrib import messages
from django.db.models import Q
from decimal import Decimal
# Create your views here.
# Search Query
def search(request):
    if request.method == "GET":
        query = request.GET.get('query')
        if query:
            # make use of `Quesryset` object to filter 
            # out desired results
            items = StoreItem.objects.filter(
                Q(name__icontains=query)|
                Q(description__icontains=query)|
                Q(category__name__icontains=query)
            )
            
            context = {
                'results': items,
                'query':query
            }
            return render(request, 'store/search.html', context)
        else:
            message = f"No results for query {query}"
            messages.info(request, f"Try search by tittle")
            return render(request, "store/search.html", {
                'msg': message
            })

# Store Functional Rendering Views
class StoreLanding(View):
    def get(self, request, *args, **kwargs):
        # get all the available stock.
        cattles = Cattle_Stock.objects.all()[:5]
        sheep = Sheep_Stock.objects.all()[:5]
        store_items = StoreItem.objects.filter(category=int(2))[:2]

        # pass them into the context dictionary to be rendered in the frontend

        # template
        context = {
            'cattles': cattles,
            'sheeps': sheep,
            'storeitems': store_items,
            'post': Post.objects.all()[:1]
        }
        return render(request, 'store/store.html', context)

class Store(View):
    def get(self, request, *args, **kwargs):
        # get all the available stock.
        store_items = StoreItem.objects.all()

        # pass them into the context dictionary to be rendered in the frontend
        # template
        context = {
            'storeitems': store_items
        }

        return render(request, 'store/storeproducts.html', context)
    
    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        street = request.POST.get('street')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip_code ')

        # create an instance of ordered items
        order_items = {
            'items': []
        }

        # create variables of all products
        items = request.POST.getlist('items[]')

        # loop over all the available stock and populate the
        # dictionary
        for item in items:
            store_item = StoreItem.objects.get(pk__contains=int(item))
            item_date = {
                'id': store_item.pk,
                'name': store_item.name,
                'price': store_item.price
            }
            print(item_date)
            order_items['items'].append(item_date)

            # create a turple for invoicing and cart
            price = 0
            item_ids = []
            

        for item in order_items['items']:
            price += item['price']   
            item_ids.append(item['id'])

            order = OrderModel.objects.create(
                price=price,
                name=name,
                email=email,
                street=street,
                city=city,
                state=state,
                zip_code=zip_code
            )
            order.items.add(*item_ids)

            return redirect('store:order-confirmation', pk=order.pk)
    

class Orderconfirmation(View):
    def get(self, request, pk, *args, **kwargs):
        order = OrderModel.objects.get(pk=pk)

        context = {
            'pk': order.pk,
            'items': order.items,
            'price': order.price,
            'name': order.name,
            'email': order.email,
            'street': order.street,
            'city': order.city,
            'state': order.state,
            'zipcode': order.zip_code
        }

        return render(request, 'store/confirm-order.html', context) 

    def post(self, request, pk, *args, **kwargs):
        data = json.loads(request.body)

        if data['isPaid']:
            order= OrderModel.objects.get(pk=pk)
            order.is_paid = True
            order.save()

        return redirect('payment-submitted')

class OrderPaymentConfirmation(View):
    def get(self, request, pk, *args, **kwargs):
        order = OrderModel.objects.get(pk=pk)

        context = {
            'pk': order.pk,
            'items': order.items,
            'price': order.price,
        }
        return render(request, 'customers/order_pay_confirmation.html', context)
    
    def post(self, request, pk, *args, **kwargs):
        option = request.POST.get('option')

        if option == "Yes":
            pass

        else:
            pass
