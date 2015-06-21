from .mixins import ResourceMixin


class ProductStatus(object):

    def __init__(self, **kwargs):
        self.__dict__.update(**kwargs)

    def __repr__(self):
        return '<ProductStatus %s: %s>' % (
            self.productId, self.title
        )

    def has_issue_level(self, level):
        if hasattr(self, 'dataQualityIssues'):
            for issue in self.dataQualityIssues:
                if issue['severity'] == level:
                    return True
        return False


class ProductStatusManager(ResourceMixin):
    scope = 'productstatuses'
    resource_class = ProductStatus
    single_resource_id = 'productId'

    def with_issues_level(self, level):
        result = []
        statuses = self.list()
        for status in statuses:
            if status.has_issue_level(level):
                result.append(status)
        return result
