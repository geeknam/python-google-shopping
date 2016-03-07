from .mixins import ResourceMixin


class LocationGroup(object):

    def __init__(self, **kwargs):
        self.__dict__.update(**kwargs)

    def __repr__(self):
        return '<LocationGroup %s: %s>' % (self.country, self.name)


class RateTable(object):

    def __init__(self, **kwargs):
        self.__dict__.update(**kwargs)

    def __repr__(self):
        return '<RateTable %s: %s>' % (self.saleCountry, self.name)


class AccountShipping(object):

    class_map = {
        'locationGroups': LocationGroup,
        'rateTables': RateTable
    }

    def __init__(self, **kwargs):
        self.accountId = kwargs.get('accountId')
        self.locationGroups = []
        self.rateTables = []

        for key, data in kwargs.items():
            for entry in data:
                try:
                    getattr(self, key).append(
                        self.class_map[key](**entry)
                    )
                except (AttributeError, KeyError):
                    pass

    def __repr__(self):
        return '<AccountShipping %s>' % self.accountId


class AccountShippingManager(ResourceMixin):
    scope = 'accountshipping'
    resource_class = AccountShipping
    single_resource_id = 'productId'
