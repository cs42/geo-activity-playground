from flask import Blueprint
from flask import render_template

from ...core.activities import ActivityRepository
from .controller import SummaryController


def make_summary_blueprint(repository: ActivityRepository) -> Blueprint:
    summary_controller = SummaryController(repository)
    blueprint = Blueprint("summary", __name__, template_folder="templates")

    @blueprint.route("/")
    def index():
        return render_template("summary/index.html.j2", **summary_controller.render())

    return blueprint
