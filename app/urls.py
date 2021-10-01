from flask import Blueprint

from app.views import ApiTest

research_routes = Blueprint('research_routes', __name__)

research_routes.add_url_rule('/status', view_func=ApiTest.as_view('status'))
