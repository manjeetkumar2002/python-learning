from flask import Flask, request, redirect, Response, session, url_for

app = Flask(__name__)
app.secret_key = "supersecret"

# WELCOME PAGE
@app.route("/")
def welcome():
    if "user" in session:
        return f'''
            <h2>WELCOME, {session["user"]}!</h2>
            <a href="{url_for('logout')}">Logout</a>
        '''
    else:
        return redirect(url_for('login'))

@app.route("/login", methods=["GET", "POST"])
def login():
    # THIS WILL EXECUTE WHEN USER SUBMIT THE FORM
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # IF CREDENTIALS ARE VALID REDIRECT THE USER TO WELCOME PAGE
        if username == "admin" and password == "123":
            # store the user in session
            session["user"] = username
            return redirect(url_for("welcome"))
        else:
            return "INVALID CREDENTIALS"

    # THIS WILL SHOW ON GET REQUEST
    return '''
        <h2>LOGIN PAGE</h2>
        <form method="POST">
            username: <input type="text" name="username"><br>
            password: <input type="password" name="password"><br>
            <input type="submit" value="login">
        </form>
    '''

@app.route("/logout")
def logout():
    session.pop("user", None)  # Use None as default to avoid KeyError
    return redirect(url_for("login"))