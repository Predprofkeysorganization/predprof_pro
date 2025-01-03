from flask import *
import logging


# logging.basicConfig(level=logging.WARNING)
app = Flask(__name__)


@app.route('/')
def base_admin():
    return render_template("base.html")


@app.route('/registration_user')
def registration():
    return render_template("templates_registration/registration_base.html")


@app.route('/registration_admin')
def registration_admin():
    return render_template("templates_registration/registration_admin.html")


if __name__ == '__main__':
    app.run()