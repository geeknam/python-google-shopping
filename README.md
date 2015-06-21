Python Google Shopping for Human
=================================

Python client for Google Content API v2

Installation
-------------

.. code-block:: bash

   pip install python-google-shopping

Features
------------

* Supports multicast message
* Resend messages using exponential back-off
* Proxy support
* Easily handle errors
* Uses `requests` from version > 0.2

Usage
------------
        
Basic

.. code-block:: bash

  export GOOGLE_SHOPPING_CLIENT_ID=my_client_id
  export GOOGLE_SHOPPING_CLIENT_SECRET=my_client_secret
  export GOOGLE_SHOPPING_REFRESH_TOKEN=my_refresh_token


.. code-block:: python

  from google_shopping.managers import GoogleShopping
  merchant_id = '536476575676'
  shopping = GoogleShopping(merchant_id, country_code='AU')
  
  # Get product resource
  product_resource = shopping.products.get(1234)

  # Delete product resource
  product = Product.objects.order_by('?').first()
  shopping.products.delete(product.id)

