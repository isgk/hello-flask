# Convert Krutidev to Unicode



## Getting Started


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
pip install -r requirements.txt
cd hello-flask
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

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Flask](http://flask.pocoo.org/) - The web framework used

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc

