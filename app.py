from flask import Flask, render_template
import requests
import datetime



app = Flask(__name__)


@app.route('/')
def hello_world():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    value = response.json()
    coordinates = str(value['iss_position']['latitude']) + ", " + str(value['iss_position']['longitude'])

    url = "http://api.positionstack.com/v1/reverse?access_key=5bb29b98d95be324b182a20fc9cb9f72&query=" + coordinates

    response = requests.get(url)
    address = response.json()
    location = address['data'][0]['label']

    timestamp = datetime.datetime.fromtimestamp(value['timestamp'])
    time = timestamp.strftime('%Y-%m-%d %H:%M:%S')
    return render_template("index.html", coordinates=coordinates, location=location, time=time)


if __name__ == '__main__':
    app.run(debug=True)
