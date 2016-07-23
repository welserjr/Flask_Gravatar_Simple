__author__ = 'WelserJr'

from flask import Flask, render_template
import forms
import requests
import json
from hashlib import md5

app = Flask(__name__)
app.secret_key = "sdnslkdjlkdmlk"


@app.route("/", methods=['GET', 'POST'])
def index():
    data = {}
    form = forms.EmailForm()
    if form.validate_on_submit():
        email_code = md5(form.email.data.encode('utf-8')).hexdigest()
        # d = 'retro'
        # s = 100
        # r = 'g'
        # url = 'http://www.gravatar.com/avatar/{}?d={}&s={}&r={}'.format(email_code, d, s, r)
        url_json = 'http://www.gravatar.com/{}.json'.format(email_code)
        # print(url)
        print(url_json)
        response = requests.get(url_json)
        data_response = json.loads(response.text)
        d = data_response['entry'][0]
        data = {
            'username': validate(d, 'preferredUsername'),
            'img': validate(d, 'thumbnailUrl'),
            'name': '{} {}'.format(validate(d['name'], 'givenName'), validate(d['name'], 'familyName')),
            'full_name': validate(d['name'], 'formatted'),
            'city': validate(d, 'currentLocation')
        }
        # print(data)
        # print(data['entry'])
    return render_template('index.html', form=form, data=data)


def validate(d, key):
    if key in d:
        return d[key]
    else:
        return ""

if __name__ == "__main__":
    app.run(debug=True)
