from flask import Flask, jsonify, request
import requests, json

app = Flask(__name__)

url = "https://api.chucknorris.io/jokes/"
headers = { "Content-Type": "application/json" }

methods = ['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH']
categories = ["animal", "career", "celebrity", "dev", "explicit", "fashion", "food", "history", "money", "movie", "music", "political", "religion", "science", "sport", "travel"]


def get_json_items(data):
    joke = data.get('value')
    categories = data.get('categories')
    id = data.get('id')
    return {'joke':joke, 'categories':categories, 'id':id}


@app.route('/', methods=methods)
def default():
    if request.method == 'GET':
        return "This is a Chuck Norris Jokes API, have fun!", 200
    else:
        return jsonify(message="The method " + request.method + " is not allowed for the requested URL"), 405

@app.route('/api/jokes/random', methods=methods)
def random():
    if request.method == 'GET':
        res = requests.get(url + "/random", headers=headers).json()
        return jsonify(get_json_items(res))
    else:
        return jsonify(message="The method " + request.method + " is not allowed for the requested URL"), 405

@app.route('/api/jokes/categories', methods=methods)
def categories():
    if request.method == 'GET':
        res = requests.get(url + "/categories", headers=headers).json()
        return jsonify(res)
    else:
        return jsonify(message="The method " + request.method + " is not allowed for the requested URL"), 405


@app.route('/api/jokes/filter', methods=methods)
def by_search():
    if request.method == 'POST':
        list = []
        search = request.form.get('search')
        limit = request.form.get('limit')
        query = url + f"search?query={search}"

        if not search or not limit:
            return jsonify(message="the fields 'search' and 'limit' is required"), 500

        jokes = requests.get(query, headers=headers).json().get('result')
        if jokes:
            if int(limit) > len(jokes):
                limit = len(jokes)

            for i in range(int(limit)):
                list.append(get_json_items(jokes[i]))

            return jsonify(total=limit,result=list), 200
        else:
            return jsonify(message="A joke with '" + search + "' was not found"), 404
    else:
        return jsonify(message="The method " + request.method + " is not allowed for the requested URL"), 405


@app.route('/api/jokes/<string:category>', methods=methods)
def by_category(category):
    if request.method == 'POST':
        if category in categories:
            res = requests.get(url + "random?category=" + category, headers=headers).json()
            return jsonify(get_json_items(res))
        else:
            return jsonify(message="The category '" + category + "' was not found"), 404
    else:
        return jsonify(message="The method " + request.method + " is not allowed for the requested URL"), 405

@app.route('/api/jokes/id/<string:id>', methods=methods)
def by_id(id):
    if request.method == 'POST':
        res = requests.get(url + id, headers=headers).json()
        if res.get('value'):
            return jsonify(get_json_items(res))
        else:
            return jsonify(message="The id '" + id + "' was not found"), 404
    else:
        return jsonify(message="The method " + request.method + " is not allowed for the requested URL"), 405
