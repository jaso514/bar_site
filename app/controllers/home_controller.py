from flask import Blueprint, render_template, send_from_directory, request, redirect, url_for
from datetime import datetime

bp = Blueprint('home', __name__, url_prefix='/')

@bp.route('/')
def index():
    current_year = datetime.now().year
    return render_template("index.html", current_year=current_year)