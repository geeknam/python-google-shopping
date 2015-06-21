from .utils import gtin_pad
from .mixins import ResourceMixin


class Product(object):

    def __init__(self, **kwargs):
        gtin = kwargs.get('gtin', None)
        if gtin:
            try:
                gtin = gtin_pad(gtin)
            except (IndexError, ValueError):
                kwargs['identifierExists'] = False
        else:
            kwargs['identifierExists'] = False
        self.__dict__.update(**kwargs)

    def __repr__(self):
        return '<Product %s: %s>' % (self.id, self.title)


class ProductManager(ResourceMixin):
    scope = 'products'
    resource_class = Product
    single_resource_id = 'productId'
