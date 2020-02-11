# FeedBackSystem

This is a Web App For Recording Review and Feedbacks Provided By a User .  


## Installation

Use the [requirements.yaml]() file to install all required Dependencies At Once.
```anaconda prompt
conda env create -f  requirements.yaml
```
Activate The Envoirment 
```anaconda prompt
activate login
```

## Usage
change directory to web app
```bash
py manage.py migrate
py manage.py makemigrations test1
```

Create SuperUser for your admin site
```
py manage.py createsuperuser
```
Type UserName and Password 
##Run Server
```python
py manage.py runserver
```
open your browser and go to [The Hosted Server](http://localhost:8000/)