# Learning Flask.

This repo was created to document the steps followed in the flask tutorial.
The objective is to create a first flask-app and then a first flask-api or microservice.

[Flask official documentation](https://flask.palletsprojects.com/en/3.0.x/)

#### Steps to install flask in windows.
---
1-Create a virtual environment

    -Create a project folder and a .venv folder within:

```shell
> mkdir myproject
> cd myproject
> py -3 -m venv .venv
```

2- Activate the environment 
    
    -Before you work on your project, activate the corresponding environment:

```shell
> .venv\Scripts\activate
```
-Your shell prompt will change to show the name of the activated environment.

Note:if you are using visual studio code editor you may follow this [tutorial](https://code.visualstudio.com/docs/python/python-tutorial#_prerequisites) to setup your virtual environment and activate it in windows.

3- Install Flask using pip
    
    -Within the activated environment, use the following command to install Flask:

```shell
> python -m pip install flask
```
Flask is now installed.

