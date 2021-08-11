from flask import render_template, redirect, url_for
from twittor.forms import LoginForm
from twittor.models import User, Tweet

def index():
    name = {'username':'root'}
    posts = [
        {
            'author':{'username':'root'},
            'body':"hi i'm roots!"
        }, {
            'author':{'username':'test'},
            'body':"hi i'm test!"
        },
    ]
    return render_template('index.html',name=name,posts=posts
                           )


def login():
    form = LoginForm(csrf_enabled=False)
    if form.validate_on_submit():
        msg = "username={}, password={}, remember_me={}".format(
            form.username.data,
            form.password.data,
            form.remember_me.data,
        )
        print(msg)
        return redirect(url_for('index'))
    return render_template('login.html', title="Sign In", form=form )