from flask import Blueprint, render_template

user_dashboard = Blueprint('user_dashboard', __name__)

@user_dashboard.route('/')
def dashboard():
    return render_template('/user/dashboard.html')
