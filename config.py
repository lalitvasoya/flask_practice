import os

# SCRAPING_QUEUE_URL = os.getenv("SCRAPING_QUEUE_URL", "")

# SCRAPING_QUEUE_NAME = os.getenv("SCRAPING_QUEUE_NAME", "scraping_queue")
# LANDSCAPE_SEARCH_KEYWORD_QUEUE_NAME = os.getenv("LANDSCAPE_SEARCH_KEYWORD_QUEUE_NAME", "landscape_search_keyword_ueue")
# LANDSCAPE_SEARCH_KEYWORD_QUEUE_URL = os.getenv("LANDSCAPE_SEARCH_KEYWORD_QUEUE_URL", "")

# MAX_NUM_QUEUE_MESSAGES = os.getenv("MAX_NUM_QUEUE_MESSAGES", 1)

# URLS_GROUP_SIZE = os.getenv("URLS_GROUP_SIZE", 10)

LOG_FILE_PATH = os.getenv("LOG_FILE_PATH",
                          "/app.log")

LOG_FORMAT = '%(timestamp)s %(level)s %(msecs)d %(process)d %(threadName)s %(levelname)s ' \
             '%(filename)s:%(lineno)s %(name)s %(message)s'

POSTGRES_URI = os.getenv("POSTGRES_URI", "postgres+psycopg2://postgres:postgres@localhost:5432/immedia_migrations")
# ARTICLE_DOWNLOAD_MAX_TIME_TIMEOUT = int(os.getenv("ARTICLE_DOWNLOAD_MAX_TIME_TIMEOUT", 10))
# ARTICLE_DOWNLOAD_SLEEP_TIME = int(os.getenv("ARTICLE_DOWNLOAD_SLEEP_TIME", 2))

# SCRAPING_QUEUE_SLEEPING_TIME = int(os.getenv("SCRAPING_QUEUE_SLEEPING_TIME", 60))
# LANDSCAPE_SEARCH_KEYWORD_QUEUE_SLEEPING_TIME = int(os.getenv("LANDSCAPE_SEARCH_KEYWORD_QUEUE_SLEEPING_TIME", 60))

# ARTICLE_SUMMARY_RATIO = int(os.getenv("ARTICLE_SUMMARY_RATIO", 0.5))
# ARTICLE_SUMMARY_WORDS = int(os.getenv("ARTICLE_SUMMARY_WORDS", 100))



class Config:
    DEBUG = False
    TESTING = False

    SQLALCHEMY_DATABASE_URI = os.getenv("POSTGRES_URI", "postgres+psycopg2://postgres:postgres@localhost:5432/immedia_migrations")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Celery setting
    CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL", "redis://localhost:6379")
    CELERY_BACKEND = os.getenv("CELERY_BROKER_URL", "db+postgresql://postgres:postgres@localhost/celerydemo")


class ProductionConfig(Config):
    pass


class StagingConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:postgres@localhost:5432/test_immedia_ml"


configuration = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'staging': StagingConfig,
    'default': DevelopmentConfig
}
