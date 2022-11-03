# Installation
In order to use the Flask application, you need to install the flask and yaml libraries, using the package manager pip.
```commandline
pip install -r requirements.txt
```
## Usage
To run the Flask application in order to have access to the routes, you need to run it.
```commandline
flask --app main run
```
Now the application is up and running, you can GET one of the following routes:
- /education
- /personal
- /work

Moreover, you can use the CLI commands. They are grouped under "data", so you need to run them as:
```commandline
flask --app main data [COMMAND]
```