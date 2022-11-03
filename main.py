from flask import Flask
from yaml import safe_load
from commands import bp

app = Flask(__name__)

with open('cv.yml') as f:
    yml_data = safe_load(f.read())


@app.get('/personal')
def personal():
    return {
        'name': yml_data.get('name'),
        'mail': yml_data.get('mail'),
        'phone': yml_data.get('phone'),
        'experience': yml_data.get('experience')
    }


@app.get('/work')
def work():
    return yml_data.get('work', [])


@app.get('/education')
def education():
    return yml_data.get('education', [])


app.register_blueprint(bp)
