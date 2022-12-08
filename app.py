from flask import Flask, jsonify, request
import requests, json

# Create flask instance with the name
# of the file application.
app = Flask(__name__)

root_url = "https://api.chucknorris.io/jokes/"
headers = { "Content-Type": "application/json" }

methods = ['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH']
categories = [ "animal", "career", "celebrity", "dev", "explicit", "fashion", "food", "history", "money", "movie", "music", "political", "religion", "science", "sport", "travel"]


# Get items and return a json
def get_json_items(data):

    joke = data.get('value')
    category = data.get('categories')
    id = data.get('id')

    return {'joke':joke, 'categories':category, 'id':id}


# Welcome message
@app.route('/', methods=methods)
def default():
    if request.method == 'GET': # Only accept GET method
        # Return json with status
        return jsonify("This is a Chuck Norris Jokes API, have fun!"), 200
    else:
        # Other methods will throw a 405 error
        return jsonify(message="The method " + request.method + " is not allowed for the requested URL"), 405

# Random joke
@app.route('/api/jokes/random', methods=methods)
def random():
    if request.method == 'GET':
        url = root_url + "/random" # Random url
        res = requests.get(url, headers=headers).json() # Get API response

        # Return response object
        return jsonify(get_json_items(res))
    else:
        return jsonify(message="The method " + request.method + " is not allowed for the requested URL"), 405

# List all categories
@app.route('/api/jokes/categories', methods=methods)
def all_categories():
    if request.method == 'GET':
        url = root_url + "/categories"
        res = requests.get(url, headers=headers).json()
        return jsonify(res)
    else:
        return jsonify(message="The method " + request.method + " is not allowed for the requested URL"), 405


# Seach joke by keyword and limit
@app.route('/api/jokes/filter', methods=methods)
def by_search():
    if request.method == 'POST': # Only accept POST method
        list = []
        search = request.form.get('search')
        limit = request.form.get('limit')
        query = root_url + f"search?query={search}"

        # If search or limit is empty throw 500 error
        if not search or not limit:
            return jsonify(message="the fields 'search' and 'limit' is required"), 500

        jokes = requests.get(query, headers=headers).json().get('result')
        if jokes:
            # If the limit exceeds the amount of jokes found, show all results
            if int(limit) > len(jokes):
                limit = len(jokes)

            # Put all jokes by limit range on list
            for i in range(int(limit)):
                list.append(get_json_items(jokes[i]))

            return jsonify(total=limit,result=list), 200
        else:
            return jsonify(message="A joke with '" + search + "' was not found"), 404
    else:
        return jsonify(message="The method " + request.method + " is not allowed for the requested URL"), 405


# Random joke by categories
@app.route('/api/jokes/<string:category>', methods=methods)
def by_category(category):
    if request.method == 'POST':
        if category in categories:
            url = root_url + "random?category=" + category
            res = requests.get(url, headers=headers).json()
            return jsonify(get_json_items(res))
        else:
            return jsonify(message="The category '" + category + "' was not found"), 404
    else:
        return jsonify(message="The method " + request.method + " is not allowed for the requested URL"), 405

# Joke by ID
@app.route('/api/jokes/id/<string:id>', methods=methods)
def by_id(id):
    if request.method == 'POST':
        url = root_url + id
        res = requests.get(url, headers=headers).json()
        if res.get('value'):
            return jsonify(get_json_items(res))
        else:
            return jsonify(message="The id '" + id + "' was not found"), 404
    else:
        return jsonify(message="The method " + request.method + " is not allowed for the requested URL"), 405
