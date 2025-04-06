from .models import Cart


def site_cart(request):
    if request.user.is_authenticated:
        return {'cart': Cart.objects.prefetch_related('items').filter(user=request.user).last()}
    return {}