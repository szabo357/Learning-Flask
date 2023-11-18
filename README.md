# Learning Flask.

This repo was created to be a tutorial that documents the steps followed in the  development of a first flask-app, flask-api or flask-microservice.
By the creation of the repo Flask version is 3.0.0. We are going to be following [Official Flask documentation](https://flask.palletsprojects.com/en/3.0.x/)
for this version of the package.

Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions. However, Flask supports extensions that can add application features as if they were implemented in Flask itself. Extensions exist for object-relational mappers, form validation, upload handling, various open authentication technologies and several common framework related tools.


#### Steps to install flask in windows.
---
1-Create a virtual environment

-Create a project folder and a .venv folder within:

```shell
mkdir myproject
cd myproject
py -3 -m venv .venv
```

2- Activate the environment 
    
-Before you work on your project, activate the corresponding environment:

```shell
.venv\Scripts\activate
```
-Your shell prompt will change to show the name of the activated environment.

Note: If you are using visual studio code editor you may follow this [tutorial](https://code.visualstudio.com/docs/python/python-tutorial#_prerequisites) to setup your virtual environment and activate it in windows.

3- Install Flask using pip
    
-Within the activated environment, use the following command to install Flask:

### Quickstart

A Minimal Application looks like this:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_flask():
    return "<p>Hello, Flask!</p>"
```
So what did that code do?

1. First we imported the **Flask** class. An instance of this class will be our WSGI application.

2. Next we create an instance of this class. The first argument is the name of the application’s module or package. **__name__** is a convenient shortcut for this that is appropriate for most cases. This is needed so that Flask knows where to look for resources such as templates and static files.

3. We then use the **route()** decorator to tell Flask what URL should trigger our function.

4. The function returns the message we want to display in the user’s browser. The default content type is HTML, so HTML in the string will be rendered by the browser.

5. Save it as **hello_flask.py** or something similar. **Make sure to not call your application ***flask.py*** because this would conflict with Flask itself.**

To run the application, use the flask command: 
```shell
python -m pip install flask
```

#### Beginning of the Tutorial.