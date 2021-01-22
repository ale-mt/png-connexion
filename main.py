from flask import jsonify
import connexion


app = connexion.App(__name__, specification_dir='open_api/')
app.add_api('my_api.yaml')


@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"


@app.route('/home')
def home():
    return "<h1>Home page</h1>"




# @app.route('/api/get/', defaults={'var': None, 'id': None}, methods=['GET'])
# @app.route('/api/get/<var>/', defaults={'id': None}, methods=['GET'])
# @app.route('/api/get/<var>/<int:id>/', methods=['GET'])
# def get(var, id):
#     if var and id:
#         print(someData.get(var).get(id))
#         return jsonify(data=someData.get(var).get(id))
#
#     if var:
#         return jsonify(data=someData.get(var))
#
#     else:
#         return jsonify(data=[someData.get("Alimenti"), someData.get("Beni")])
