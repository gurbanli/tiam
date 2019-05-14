from flask import Flask, flash, redirect, render_template, request, abort, session , url_for
from database import Database
app = Flask(__name__)

@app.route('/')
def index():
    return redirect("/register")

@app.route('/register', methods = ['GET','POST'])
def register():
    try:
        if request.method == "POST":
            name = request.form ['name']
            gender = request.form ['gender']
            email = request.form ['email']
            phone = request.form ['phone']
            field = request.form ['field']
            uni = request.form ['uni']
            spec = request.form ['spec']
            return send_database(name,gender,email,phone,field,uni,spec)
        return render_template("index.html")
    except Exception as e:
        flash(e)
        abort(401)
def send_database(name,gender,email,phone,field,uni,spec):
    try:
        db = Database()
        db.add_student(name,gender,email,phone,field,uni,spec)
        return render_template("index.html",bool="True")
    except Exception as e:
        flash(e)
        return render_template("index.html",bool="False")

@app.route('/admin',methods = ['GET','POST'])
def admin():
    error = ""
    if 'username' in session:
        return redirect(url_for('dashboard'))
    try:
        if request.method == 'POST':
            attempted_username = request.form['username']
            attempted_password = request.form['password']
            if validate_user(attempted_username,attempted_password):
                session['username'] = attempted_username
                return redirect(url_for('dashboard'))
            else:
                error = "Username or password is incorrect"
        return render_template("admin.html",error=error)
    except Exception as e:
        flash(e)
        error = "Something went wrong. Please try again!"
        return render_template("admin.html",error=error)
def validate_user(username,password):
    db = Database()
    return db.check_admin(username,password)

@app.route('/dashboard')
def dashboard():
    if not 'username' in session:
        return redirect(url_for("admin"))
    return render_template("dashboard.html",name=session.get('username'),Students=get_Students())
def get_Students():
    db = Database()
    return db.get_students()

@app.route('/logout')
def logout():
   session.pop('username', None)
   return redirect(url_for('admin'))

if __name__ == "__main__":
    app.config['SECRET_KEY']='LdB79m#auth'
    app.run(host='0.0.0.0', port=4000)