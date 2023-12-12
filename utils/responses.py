from flask import jsonify

def response_message(state,message):
    return jsonify({
        "ok": state,
        "msg": message
    })