from .mixins import ResourceMixin


class ProductStatus(object):

    def __init__(self, **kwargs):
        self.__dict__.update(**kwargs)

    def __repr__(self):
        return '<ProductStatus %s: %s>' % (
            self.productId, self.title
        )

    def get_internal_id(self):
        return self.productId.split(':')[-1]

    def has_issue_level(self, level):
        if hasattr(self, 'dataQualityIssues'):
            for issue in self.dataQualityIssues:
                if issue['severity'] == level:
                    return True
        return False

    @property
    def should_be_removed(self):
        return self.has_issue_level('critical')


class ProductStatusManager(ResourceMixin):
    scope = 'productstatuses'
    resource_class = ProductStatus
    single_resource_id = 'productId'

    def remove_critical_issues(self):
        """
        Iterator through all statuses and remove products
        which has severity of critical
        """
        for status in self.list():
            if status.should_be_removed:
                self.manager.products.delete(
                    status.get_internal_id()
                )
