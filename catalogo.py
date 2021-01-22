from flask import request, jsonify, make_response

CATALOGO = [
    {
        "Tavolo": {
            "h": 100,
            "l": 10,
            "w": 20
        }
    },
    {
        "Porta": {
            "h": 250,
            "l": 50,
            "w": 25
        }
    }
]


def read():
    # return [list(articolo.keys()) for articolo in CATALOGO]
    return CATALOGO


def readid(id):
    return CATALOGO[id]


def create():
    post_request = request.get_json() # { 'nome': { 'h': x, 'l':y, 'w':z } }
    CATALOGO.append(post_request)

    print(CATALOGO)
    return jsonify(CATALOGO)


def delete(id):
    CATALOGO.pop(id)

    return jsonify(CATALOGO)


def put(id):
    put_request = request.get_json() # { 'nome': { 'h': x, 'l':y, 'w':z } }
    target = CATALOGO[id]

    try:
        new_key = list(put_request.keys())[0] # [ 'nome' ] => 'nome'

    except Exception:
        res = make_response("First key is invalid")
        res.status_code = 500
        return res

    old_key = list(target.keys())[0]

    if new_key != old_key:

        # cambia key al dizionario clonandolo ed elimina quello con la chiave obsoleta
        target[new_key] = target[old_key]
        del target[old_key]

    actual_key = list(target.keys())[0]
    target[actual_key]['h'] = put_request[list(target.keys())[0]].get('h', target[actual_key]['h'])
    target[actual_key]['l'] = put_request[list(target.keys())[0]].get('l', target[actual_key]['l'])
    target[actual_key]['w'] = put_request[list(target.keys())[0]].get('w', target[actual_key]['w'])

    return jsonify(CATALOGO)

