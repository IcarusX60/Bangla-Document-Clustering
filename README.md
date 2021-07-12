# Bangla Document Clustering
 A news website created using django web framework that performs clustering task on news articles and predicts clusters for given input text.
 
 ## Preparation
 
 Install the requirements from requirements.txt
 
 
 From mysite/views.py file change the paths to the required files as per your system.
 run python manage.py makemigrations
 python manage.py migrate
 python manage.py runserver
 
 modify and run scraper.py file within blog folder to crawl prothom alo news using selenium and request (optional)
 
## Usage

localhost/clustering - to generate clusters
localhost/prothomalo - to cluster prothomalo news

