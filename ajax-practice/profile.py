import random

from flask import Flask, request, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    """Show index page."""

    return render_template("index.html")


@app.route('/api/profile', methods=['POST'])
def profile():
    """Return results from profile form."""

    fullname = request.json['name']
    age = request.json['age']
    job = request.json['job']
    salary = request.json['salary']
    edu = request.json['edu']
    state = request.json['state']
    city_type = request.json['cityType']
    does_garden = request.json['doesGarden']
    tv_hours = request.json['tvHours']

    return jsonify({
        'fullname': fullname,
        'age': age,
        'job': job,
        'salary': salary,
        'edu': edu,
        'state': state,
        'cityType': city_type,
        'doesGarden': does_garden,
        'tvHours': tv_hours
        })





if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
