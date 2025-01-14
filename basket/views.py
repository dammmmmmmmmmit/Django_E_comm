from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from store.models import Product
from .basket import Basket


def basket_summary(request):
    return render(request, 'store/basket/summary.html')
    
def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('product_qty'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, qty= product_qty)
        response = JsonResponse({'test':'data'})
        return response
    