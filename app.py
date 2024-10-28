from os import environ
from flask import Flask, render_template, redirect, request, session
import sqlite3
import os
conn = sqlite3.connect(os.path.join('/tmp', 'users.db'))
c=conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS Profiles (name VARCHAR(20), email VARCHAR(50), password VARCHAR(20))')
conn.commit()
c.close()

app=Flask(__name__)

app.secret_key = '1234'

@app.route('/login', methods=['GET','POST'])
def login():
    conn=sqlite3.connect('users.db')
    c=conn.cursor()
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        c.execute("SELECT * FROM Profiles WHERE email=? AND password=?",(email,password))
        data=c.fetchone()
        c.close()
        if data:
            session['username']=data[0]
            return redirect('/')
        else:
            err='Invalid credentials. Please try again.'
            return render_template('Login.html',error=err)
    else:
        return render_template('Login.html')

@app.route('/signup', methods=['GET','POST'])
def signup():
    conn=sqlite3.connect('users.db')
    c=conn.cursor()
    if request.method == 'POST':
        username = request.form['username']
        email=request.form['email']
        pwd = request.form['pwd']
        cpwd = request.form['cpwd']
        if pwd==cpwd:
            c.execute("SELECT * FROM Profiles WHERE email=?",(email,))
            data=c.fetchall()
            if not data:
                c.execute("INSERT INTO Profiles VALUES(?,?,?)",(username,email,cpwd))
                conn.commit()
                session['username']=username
                return redirect('/')
            else:
                err='User already exists'
                return render_template('Signup.html',error=err)
        else:
            err='Pasword did not match'
            return render_template('Signup.html',error=err)
    else:
        return render_template('Signup.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')

@app.route('/')
def home():
    if 'username' in session:
        return render_template('home.html', username=session['username'])
    else:
        return redirect('/login')

@app.route('/games')
def games():
    if 'username' in session:
        return render_template('Gamepage.html', username=session['username'])
    else:
        return redirect('/login')

@app.route('/movies')
def movies():
    if 'username' in session:
        return render_template('Moviepage.html', username=session['username'])
    else:
        return redirect('/login')

@app.route('/series')
def series():
    if 'username' in session:
        return render_template('Seriespage.html', username=session['username'])
    else:
        return redirect('/login')

if __name__=='__main__':
    port = int(environ.get("PORT", 3000))  # Use the PORT environment variable or default to 3000
    app.run(host="0.0.0.0", port=port)
