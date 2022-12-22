# Flask Portfolio Site

A portfolio site made with HTML5, Bootstrap, Python, and Flask with templating by Jinja.

## Installation

Make sure you have python3 and pip installed

Create and activate virtual environment using virtualenv
```bash
$ python -m venv python3-virtualenv
$ source python3-virtualenv/bin/activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all dependencies!

```bash
pip install -r requirements.txt
```

## Usage

Create a .env file using the example.env template (make a copy using the variables inside of the template)

Start flask development server
```bash
$ export FLASK_ENV=development
$ flask run
```

You should get a response like this in the terminal:
```
❯ flask run
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

You'll now be able to access the website at `localhost:5000` or `127.0.0.1:5000` in the browser! 

*Note: The portfolio site will only work on your local machine while you have it running inside of your terminal. To run it for any host to connect to, do the following*

```bash
$ export FLASK_ENV=production
$ flask run --host=0.0.0.0
```

## Contributions:
Contributions are welcome. Fork the repo, make your changes, create a diff file, and email the diff file and your GitHub username to luis@moraguez.com. If the changes are approved, you will be added as a contributor to the repo.

## Donations:
If this utility helped you with a project you're working on and you wish to make a donation, you can do so by clicking the donate button that follows. Thank you for your generosity and support!

<noscript><a href="https://liberapay.com/z3d6380/donate"><img alt="Donate using Liberapay" src="https://liberapay.com/assets/widgets/donate.svg"></a></noscript>
