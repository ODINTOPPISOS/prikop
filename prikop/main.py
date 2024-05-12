from flask import Flask, render_template, request, redirect, url_for, session
from random import randint
#from zxc import get_question_after
#from requests import *
import json
app = Flask(__name__)
import sqlite3



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
        bd = {}
        with open('bd.json', "w") as file1:
            bd[name] = password
            json.dump(bd, file1)
        return redirect('/login')
    return a


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        with open('bd.json', "r") as file:
            bd1 = json.load(file)
            if name in bd1.keys():
                if bd1[name] == password:
                    return '<h1>Ку</h1>'
        return '<h1>Не ку</h1>'
    return a
if __name__ == "__main__":
    app.run(debug=True)
"""    
@app.route("/<int:id>")
def get_page_about(id):
    rand_num = map(str,range(randint(5,10)))
    return render_template("base.html", title='Название', id=id,colorf = (randint(0,255),randint(0,255),randint(0,255)),rand_num=rand_num)
"""