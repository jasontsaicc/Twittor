from flask import render_template, redirect, url_for, request
from flask_login import login_user, current_user, logout_user, login_required
from twittor.forms import LoginForm
from twittor.models import User, Tweet

@login_required
def index():
    # name = {'username':current_user.username}
    posts = [
        {
            'author':{'username':'root'},
            'body':"hi i'm roots!"
        }, {
            'author':{'username':'test'},
            'body':"hi i'm test!"
        },
    ]
    return render_template('index.html',posts=posts
                           )


def login():
    if current_user.is_authenticated:
        return redirect(url_for('index')) 
    form = LoginForm()
    if form.validate_on_submit():
        # msg = "username={}, password={}, remember_me={}".format(
        #     form.username.data,
        #     form.password.data,
        #     form.remember_me.data,
        # )
        # print(msg)
        u = User.query.filter_by(username=form.username.data).first()
        if u is None or not u.check_password(form.password.data):
            print('invalid username or password')
            return redirect(url_for('login'))
        login_user(u, remember=form.remember_me.data)
            # if u.check_password(form.password.data):
        
        next_page=request.args.get('next')
        if next_page:
            return redirect(next_page) 
        return redirect(url_for('index')) 
    return render_template('login.html', title="Sign In", form=form)

def logout():
    logout_user()
    return redirect(url_for('login'))

def register():
    return render_template('register.html', title='Registration')