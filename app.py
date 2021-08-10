from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
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

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)