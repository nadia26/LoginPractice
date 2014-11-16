from flask import Flask,render_template,request,session, redirect
import functions

    
app=Flask(__name__)

@app.route("/login", methods=["GET", "POST"])
def login ():
    if request.method=="GET":
        return render_template('login.html',logged=None,message="")
    button = request.form["b"]
    if button == "Login":
        username = request.form["username"]
        password = request.form["password"]
        if username=="" or password=="":
            return render_template('login.html',logged=None, message="Please complete all fields.")
        if functions.authenticate(username,password):
            session['username'] = username
            session['name'] = functions.getName(username)
            return  redirect('home')
        else:
            return render_template('login.html',logged=None, message="Incorrect username/password")
    if button == "Register":
        return redirect('register')

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method=="GET":
        return render_template('register.html', message = "",logged=None)
    button = request.form["b"]
    if button == "Register":
        password = request.form["password"]
        confirm = request.form["confirm_password"]
        username = request.form["username"]
        name = request.form["name"]      
        if password=="" or confirm=="" or username=="" or name=="":
            return render_template('register.html', message = "Please complete all fields.",logged=None)
        if (password != confirm):
            return render_template('register.html', message = "Passwords don't match.", logged=None)
        if functions.check(username):
            return render_template('register.html', message = "Sorry, that username is already taken.",logged=None)
        functions.add_user(username, name, password)
        session['username']=username
        session['name']=name
        return redirect('home')

@app.route("/")
@app.route("/home")
def home():
    if 'username' not in session:
        return render_template('home.html',name=None, logged=False)
    else:
        return render_template('home.html',name=session['name'],logged=True)


@app.route("/s1")
def s1():
    if 'username' not in session:
        return redirect('home')
    else:
        return render_template('s1.html', name=session['username'],logged=True,special=True)

@app.route("/s2")
def s2():
    if 'username' not in session:
        return redirect('home')
    else:
        return render_template('s2.html', name=session['username'],logged=True,special=True)

@app.route("/logout")
def logout():
    session.pop("username",None)
    return redirect("/")


if __name__ == "__main__":
    app.secret_key = "superdupersecret"
    app.debug=True
    app.run()
