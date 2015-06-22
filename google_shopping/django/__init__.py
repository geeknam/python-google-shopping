

class GoogleShoppingMixin(object):

    @property
    def shopping_serialiser(self):
        return self.shopping_serialiser_class(self)
