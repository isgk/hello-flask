from flask import Flask, escape, request, jsonify
from krutidev2unicode import kru2uni

app = Flask(__name__)

'''
How to run - FLASK_APP=hello.py flask run

Need to escape " from string with backslash.

Post application/jSON to http://localhost:5000
{
    "krutidev": "egkjk\"Vz jkT; Hkwlaiknu iqfLrdkizek.ks rDrk"
}

Response
{
    "krutidev": "egkjk\"Vz jkT; Hkwlaiknu iqfLrdkizek.ks rDrk",
    "unicoded": "महाराष्ट्र राज्य भूसंपादन पुस्तिकाप्रमाणे तक्ता"
}

'''
@app.route("/", methods=['POST'])
def convert_krutidev_to_unicode():
    json_dict = {}
    json_dict['krutidev'] = request.json['krutidev']
    json_dict['unicoded'] = kru2uni(json_dict['krutidev'])
    return jsonify(json_dict)
