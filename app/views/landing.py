from flask import Blueprint, render_template

landing = Blueprint("landing", __name__)


@landing.route("/")
def index():
    return render_template("/landing/home.html")


@landing.route("/login")
def login():
    return render_template("/landing/login.html")


@landing.route("/signup")
def signup():
    return render_template("/landing/signup.html")


@landing.route("/forget")
def forget():
    return render_template("/landing/forget.html")


@landing.route("/contact")
def contact():
    return render_template("/landing/contact.html")


@landing.route("/contactform")
def contactform():
    return render_template("/landing/contactform.html")
