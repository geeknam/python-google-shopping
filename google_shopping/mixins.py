import json


class ResourceMixin(object):

    def __init__(self, manager):
        self.manager = manager
        self.resource_url = '%s/%s/%s' % (
            self.manager.BASE_CONTENT_API_URL,
            self.manager.merchant_id, self.scope
        )
        self.batch_url = '%s/%s/batch' % (
            self.manager.BASE_CONTENT_API_URL,
            self.scope
        )

    @staticmethod
    def get_resource_id(country_code, resource_id):
        """
        Construct valid Google Shopping resource id
        based on an identifier
        """
        resource_id = 'online:en:%s:%s' % (
            country_code, resource_id
        )

    def get(self, resource_id):
        """
        Returns a resource instance based on the id
        provided
        """
        self.get_resource_id(
            self.manager.country_code,
            resource_id
        )
        url = '%s/%s' % (self.resource_url, resource_id)
        data = self.manager.request(url, 'GET')
        return self.resource_class(**data)

    def insert(self, resource):
        """
        resource arg: can be either a dict or an object that
        has a defined google_shopping_serialiser attr
        """
        if hasattr('resource', 'shopping_serialiser'):
            resource = resource.shopping_serialiser(
                resource
            ).serialise()
        data = self.manager.request(
            self.resource_url, 'POST',
            data=json.dumps(resource)
        )
        return self.resource_class(**data)

    def list(self):
        """
        Yield all entries for this resource
        """
        has_next_page = True
        next_page_token = None
        while has_next_page:
            params = {
                'maxResults': self.manager.max_results
            }
            if next_page_token:
                params.update({
                    'pageToken': next_page_token
                })
            data = self.manager.request(
                self.resource_url, 'GET', params=params
            )
            try:
                next_page_token = data['nextPageToken']
            except KeyError:
                has_next_page = False

            for resource in data['resources']:
                yield self.resource_class(**resource)

    def delete(self, resource_id):
        """
        Deletes the entry from Merchant,
        returns True if successfully deleted
        """
        resource_id = 'online:en:%s:%s' % (
            self.manager.country_code,
            resource_id
        )
        url = '%s/%s' % (self.resource_url, resource_id)
        data = self.manager.request(url, 'DELETE', json=False)
        return data.status_code == 204

    def batch(self, resources, method):
        entries = []
        for resource in resources:
            entry = {
                'batchId': resource.id,
                'merchantId': self.merchant_id,
                'method': method,
            }
            if method in ['get', 'delete']:
                entry[self.single_resource_id] = self.get_resource_id(
                    self.manager.country_code,
                    resource.id
                )
            entries.append(entry)
        batch_data = {'entries': entries}

        resp = self.manager.request(
            self.batch_url, 'POST',
            data=json.dumps(batch_data)
        )
        return resp.json()

    def batch_delete(self, resources):
        return self.batch(resources, method='DELETE')
