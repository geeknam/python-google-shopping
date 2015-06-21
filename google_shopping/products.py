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
        return '<Product %s: %s>' % (
            self.id, self.title.encode('ascii', 'ignore')
        )

    @property
    def is_out_of_stock(self):
        return self.availability == 'out of stock'


class ProductManager(ResourceMixin):
    scope = 'products'
    resource_class = Product
    single_resource_id = 'productId'

    def get_sold_out(self):
        result = []
        products = self.list()
        for product in products:
            if product.is_out_of_stock:
                result.append(product)
        return result
