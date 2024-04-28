from flask import Flask, render_template, request, redirect, url_for, session
from random import randint
from zxc import get_question_after
#from requests import *
app = Flask(__name__)
import sqlite3
"""posts = '''<form method="POST">\
            <input type="submit" value="Submit">\
        </form>'''

q = 0
l = 0
@app.route("/")
def index():
    global q, l
    q = 1
    return '<a href="/test">Тест</a>'
@app.route("/test", methods=['GET', 'POST'])
def test():
    global l, q
    res = get_question_after(l, q)
    if request.method == 'POST':
        l = 0
        q = 1
        return '<p>' + str(q) + str(res) + '</p>' + '</br>' + '<a href="/test">Next</a>' + '</br>' + posts
    if res is None or len(res) == 0:
        return redirect(url_for('result'))
    else:
        l = res[0]
        return '<p>' + str(q) + str(res) + '</p>' + '</br>' + '<a href="/test">Next</a>' + '</br>' + posts

@app.route("/result")
def result():
    global l, q
    l = 0
    q = 1
    return '<p>qwe</p>'
app.config['SECRET_KEY'] = 'VeryStrongKey'



"""
@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        return render_template("qwe.html",name=name, password=password)
    return render_template("zxc.html")
a = """
        <form method="POST">\
            <input type="text" name="name">\
            <input type="text" name="password">\
            <input type="submit" value="Submit">\
        </form>
"""
@app.route('/', methods=['GET', 'POST'])
def form_example():
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        if name == 'misha' and password == '123':
            return '<h1> Вход выполнен </h1>'
        else:
            return '<h1> Вход не выполнен </h1>'
    return a



if __name__ == "__main__":
    app.run(debug=True)
"""    
@app.route("/<int:id>")
def get_page_about(id):
    rand_num = map(str,range(randint(5,10)))
    return render_template("base.html", title='Название', id=id,colorf = (randint(0,255),randint(0,255),randint(0,255)),rand_num=rand_num)
"""