# CandidateFinder
This service returns the best candidates for a specific job

## Overview
This service is designed to help you find the best candidates for a job position. You will be able to view your best candidates using
GET request in postman or just paste the service url in your browser. The service will analyze criteria such as job's title and skills required for the job. It is recommended to install the dubugger tool.

## Installation

1. Clone Git Repository To Your Local Environment
```
git clone git@github.com:GuyShefer/CandidateFinder.git
```

2. Navigate to The Root Directory
```
cd CandidateFinder
```

3. Install Dependencies
```
pip install django
```
```
pip install djangorestframework
```
```
pip install django-debug-toolbar
```

4. Run The Server
```
python manage.py runserver
```

## Use Candidate Finder
Perfom a GET request to:
```
# you can try ids 1-4
http://localhost:8000/api/best_candidates/<ID>
```
### Admin Interface
 username: admin <br />
 password: 1234

 ## Debugger Tool
 open app in the browser and the debug toolbar will appear on the project's page, providing various useful information about execution time, SQL, static files, signals, etc.



 ![dubugger](https://user-images.githubusercontent.com/54041968/129382006-74a2aa8b-ecde-4e6d-8955-ced13e89957c.png)



