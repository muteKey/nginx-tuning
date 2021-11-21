from flask import (
    Blueprint, request, render_template
)
import logging

from .repo import Repository

bp = Blueprint('views', __name__, url_prefix='/')

repository = Repository()

@bp.route('/')
def index():
    users = repository.fetch_users()
    return render_template("base.html", results=users)
