import logging

from flask import Flask
from celery import Celery

import config
from app.extensions import db
from logging.handlers import RotatingFileHandler
from app.custom_log import CustomJsonFormatter
from config import configuration

logger = logging.getLogger(__name__)
celery = Celery(__name__, broker=config.Config.CELERY_BROKER_URL)
celery.config_from_object(config)


def create_app(config_class="default"):
    """ Create the flask app """
    app = Flask(__name__)

    app.config.from_object(configuration[config_class])

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logHandler = RotatingFileHandler(config.LOG_FILE_PATH, maxBytes=10 * 1024 * 1024, backupCount=5)
    formatter = CustomJsonFormatter(config.LOG_FORMAT, json_indent=4)
    logHandler.setFormatter(formatter)
    app.logger.addHandler(logHandler)

    db.init_app(app)

    with app.app_context():
        celery.conf.update(app.config)

        from app.urls import research_routes
        app.register_blueprint(research_routes)

        return app
