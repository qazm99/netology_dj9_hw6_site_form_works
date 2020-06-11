from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.views.generic import View

from .models import Product, Review
from .forms import ReviewForm

class ProductView(View):
    template = 'app/product_detail.html'

    def post(self, request, pk):
        text_of_review = request.POST.get("text")
        Review(text=text_of_review, product=Product.objects.get(id=pk)).save()
        if request.session.get('reviewed_products'):
            if pk not in request.session['reviewed_products']:
                request.session['reviewed_products'].append(pk)
        else:
            request.session.update({"reviewed_products": [pk, ]})
        return self.get(request, pk, is_review_exist=True)

    def get(self, request, pk, is_review_exist=False):
        if request.session.get('reviewed_products'):
            if pk in request.session.get('reviewed_products'):
                is_review_exist = True

        product = get_object_or_404(Product, id=pk)
        reviews = Review.objects.filter(product=pk)
        context = {
            'product': product,
            "reviews": reviews
        }
        if not is_review_exist:
            form = ReviewForm
            context.update({'form': form, "is_review_exist": False})
        else:
            context.update({ "is_review_exist": True})
        return render(request, self.template, context)


def product_list_view(request):
    template = 'app/product_list.html'
    products = Product.objects.all()

    context = {
        'product_list': products,
    }

    return render(request, template, context)

