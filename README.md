# IMDB_Movies


### To Install additional requirements
<code>pip install -r requirements.txt</code>


### Using Celery for Background Tasks and Redis as Broker
To Install Redis for mac - <code>brew install redis</code>

To Install Redis for linux - <code>sudo apt-get install redis-server</code>


#### Steps required to Run Periodic task
1. Start Redis service
2. Start celery worker - <code> celery -A trainman worker -l info</code>


### Test The API
Import Postman Collection JSON file from main directory
