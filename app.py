from flask import Flask,render_template,request,session
import functions

    
app=Flask(__name__)

@app.route("/login", methods=["GET", "POST"])
def login ():
    if request.method=="GET":
        return render_template('login.html')
    button = request.form["b"]
    if button == "Login":
        username = request.form["username"]
        password = request.form["password"]
        if functions.authenticate(username,password):
            session['username'] = username
            return  redirect(url_for('home'))
    if button == "Register":
        return redirect(url_for('register'))
    else:
        return redirect(url_for('home'))

@app.route("/register")
def register():
    if request.method=="GET":
        return render_template('register.html', message = "")
    else:
        password = request.form["password"]
        confirm = request.form["confirm_password"]
        button = request.form["b"]
        if (password == confirm and button == "Register"):
            username = request.form["username"]
            name = request.form["name"]
            #check if existing username
            #add user
            return redirect(url_for('home'))
        else:
            return render_template('register.html', message = "passwords don't match")

@app.route("/")
@app.route("/home")
def home():
    if 'username' not in session:
        return render_template('home.html',name=None)
    else:
        return render_template('home.html',name=session['username'])

@app.route("/logout")
def logout():
    session.pop("n",None)
    return redirect("/")


if __name__ == "__main__":
    app.debug=True
    app.run()
