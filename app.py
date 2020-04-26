from algoliasearch.search_client import SearchClient
import requests
from flask import Flask, request, jsonify, abort, Response, redirect, url_for

client = SearchClient.create('1BX7OOMK9J', '8304543235ddfbb93d342a7f32b5da57')
index = client.init_index('food_details')

# Init app
app = Flask(__name__)

@app.route('/ingredient', methods=['POST', 'PUT', 'DELETE'])
def ingredient(): # function to handle ingredients in algolia
    # get request data
    data = request.get_json()
    response = jsonify(data=[])
    
    if request.method == 'POST': # add new ingredients to Algolia
        index.save_object(data, {'autoGenerateObjectIDIfNotExist': True})
        return response, 204
    elif request.method == 'PUT': # update existing ingredients in Algolia (just needs objectID)
        #Create an object
        index.partial_update_object(data)
        return response, 204
    elif request.method == 'DELETE': # delete an existing ingredient in Algolia delete just requires 'objectID'
        index.delete_object(data['objectID'])
        return response, 204

# Run Server
if __name__ == '__main__':
    app.run()