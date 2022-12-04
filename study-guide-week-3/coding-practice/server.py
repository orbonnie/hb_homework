"""A simple Flask app."""

from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)
app.secret_key = "RANDOM SECRET KEY"

mood_db = {
    "cheery": "positively",
    "honest": "genuinely",
    "dreary": "pessimistically..."
}

@app.route('/')
def show_homepage():
    """Show homepage."""

    if session.get('name'):
        return redirect('/form')

    return render_template('homepage.html')

###############################
#                             #
# 1) Finish the routes below. #
#                             #
###############################


@app.route('/form')
def show_form():
    """Show form with message options."""
    return render_template('form.html')

@app.route('/results')
def show_results():
    """Show resulting message."""

    choices = request.args.getlist('mood')
    moods = [mood_db[m] for m in choices]
    print(moods)

    return render_template('results.html',moods = moods)

@app.route('/save-name')
def get_name():
    session['name'] = request.args.get('name')

    return redirect('/')



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=3000)
