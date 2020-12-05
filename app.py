from flask import Flask, request, render_template, redirect
from stories import Story, stories
# from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)	
# app.config['SECRET_KEY'] = "secret"

# debug = DebugToolbarExtension(app)


# my original approach involved using a global story variable to store the instances which were in this file
# After looking at the answer code, storing this data in the instance maskes more sense
# story_global = None

@app.route('/')
def home_page():
    """Offer user choice of Madlib Games"""

    return render_template('index.html', stories=stories.values())


@app.route('/form')
def show_form():
    """Show Form for User Input"""

    story_title = request.args["madlib"]
    for story in stories.values():
        if story.title == story_title:
            story_for_form = story
    
    return render_template('form.html', s=story_for_form, story_title=story_title)


@app.route("/story")
def show_story():
    """Display Madlib Story"""

    answers = request.args
    story_title = request.args["story_title"]
    for story in stories.values():
        if story.title == story_title:
            story_to_gen = story
            
    return render_template("story.html", story_to_gen=story_to_gen, user_answers=answers)


@app.route('/play-again')
def play_again():
    """Redirect Home"""

    return redirect('/')
