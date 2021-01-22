from flask import jsonify, make_response, request


PERSONE = [
    {
        "Alessandro": {
            "eta": 22,
            "fname": "Alessandro",
            "lname": "Mancini"
        }
    },
    {
        "Mario": {
            "eta": 30,
            "fname": "Mario",
            "lname": "Rossi"
        }
    }
]


def read():
    return PERSONE


def read_byid(id):
    return PERSONE[id]


def delete(id):
    PERSONE.pop(id)

    return jsonify(PERSONE)


def put(id):
    put_request = request.get_json()  # {  'nome': { 'eta': x, 'fname':'ab', 'lname':'ab' } }
    target = PERSONE[id]

    try:
        new_key = list(put_request.keys())[0]  # [ 'nome' ] => 'nome'

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
    target[actual_key]['eta'] = put_request[list(target.keys())[0]].get('eta', target[actual_key]['eta'])
    target[actual_key]['fname'] = put_request[list(target.keys())[0]].get('fname', target[actual_key]['fname'])
    target[actual_key]['lname'] = put_request[list(target.keys())[0]].get('lname', target[actual_key]['lname'])

    return jsonify(PERSONE)


def post():
    post_request = request.get_json() # { 'nome': { 'eta': x, 'fname':'ab', 'lname':'ab' } }
    PERSONE.append(post_request)

    print(PERSONE)
    return jsonify(PERSONE)
