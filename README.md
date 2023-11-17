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

```shell
python -m pip install flask
```
Flask is now installed.

