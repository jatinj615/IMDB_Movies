from trainman.celery import app
from movies.movie_script import get_movies
from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)


@app.task
def store_movies_data(url):
    get_movies(url)
    logger.info('Stored all movies')
    return True
    