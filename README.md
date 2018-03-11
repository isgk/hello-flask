# Convert Krutidev to Unicode

### Prerequisites

What things you need to install the software and how to install them

```
python3 with venv module installed
flask
```

### Installing

A step by step series of examples that tell you have to get a development env running


```
git clone https://github.com/isgk/hello-flask.git
python3 -m venv hello-flask-venv
source ./hello-flask-venv/bin/activate
cd hello-flask
pip install -r requirements.txt
```

Run server

```
FLASK_APP=hello.py flask run
```


## Post Json

Don't forget to escape double quote with backslash.

### Post Json request

Don't forget to set contentType as 'application/json'

```
{
    "krutidev": "egkjk\"Vz jkT; Hkwlaiknu iqfLrdkizek.ks rDrk"
}
```

### Json Response


```
{
    "krutidev": "egkjk\"Vz jkT; Hkwlaiknu iqfLrdkizek.ks rDrk",
    "unicoded": "महाराष्ट्र राज्य भूसंपादन पुस्तिकाप्रमाणे तक्ता"
}
```

## Built With

* [Flask](http://flask.pocoo.org/) - The web framework used

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
