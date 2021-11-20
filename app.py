from flask import Flask, render_tempalte, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import stories

app = Flask(__name__)
app.configp["SECRET_KEY"] = 'supersecret'

debug = DebugToolbarExtension(app)

@app.route('/')
def ask_questions():
    """Generate and show form to ask words"""

    prompts = story.prompts

    return render_template('questions.html', prompts=prompts)

@app.route('/story')
def show_story():
    """Show the result of story"""

    text = story.generate(request.args)

    return render_template('story.html', text=text)