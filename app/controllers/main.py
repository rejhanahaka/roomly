from flask import Blueprint, render_template
from app.models.room import get_all_rooms

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    rooms = get_all_rooms()
    return render_template("index.html", rooms=rooms)