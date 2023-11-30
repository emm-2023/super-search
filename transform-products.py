import json
import os, math
from algoliasearch.search_client import SearchClient

#create algolia client and initialize new index product_index
client = SearchClient.create('8QR08I72M0', '9770b1e714bd3d2db7453b524e9edc63')
index = client.init_index('product_index')

with open('./data/products.json') as f:
    contents = f.read()

products = json.loads(contents)

#check if category attr of the product contains Cameras, etc.
def is_camera(p):
    return "Cameras & Camcorders" in p['categories']

script_dir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(script_dir, "output.json"), 'w') as output_file:

    #we create a list of objects to write as output

    #we map each item in the input product list of objects to a function which,
    #if is_camera(product) returns True for that object, updates the price attribute of the product,
    #and if is_camera returns False, just makes an entry in the output with no update
    json_to_write = list(
      map(
        #the update function
        lambda p:
          {
            **p,
            'price': math.floor(p['price']* .8)
          }
          if is_camera(p)
          else p,
        #products is the input data
        products
      )
    )
    # save json_to_write to the product_index.
    # the python client will automatically batch each 1000 objects.
    # we will use autoGenerateObjectIDIfNotExist to generate unique IDs

    index.save_objects(json_to_write, {"autoGenerateObjectIDIfNotExist":True})

