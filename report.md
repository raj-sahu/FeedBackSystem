# Rating System

It is a Web App for Recording Ratings and FeedBack Provided By Users using A Group Of Products and Services.


## Installation

Use the [requirements.yaml](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) file  to Install All Dependencies at Once.

```bash
conda env create -f requirements.yaml
```
[activate](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) the envoirment
```python
activate login
```
## Usage
Migrate Models
```python
py manage.py migrate
py manage.py makemigrations test1 
```
Create SuperUser 
```python
py manage.py createsuperuser
```
enter username and password for super usert you want to create and proceed as instructed.
##Running Server
```
py manage.py runserver
```
open browser and go to [http://localhost:8000/](http://localhost:8000/) to go to homepage of hosted website.

---
![home page](images/logo.png)
>Click on register button to add a new user

![register page](images/register.png)

>Fill The Form Correctly And Register

![register page1](images/register1.png)

>Go to Login Page and login

![login page](images/logo1.png)

>make Entries on the Service You Use 

![response page](images/register2.png)

---
##ADMIN SITE
if you are an admin you can go to admin site
![response page](images/register3.png)

>if You are not logged in Log in

![admin page](images/register4.png)

>once login as admin admin:

![admin page](images/register8.png)

>In the features area we have a question section to add Existing Questions.

![admin page](images/register6.png)

>In the festures area we also have a rating section to veiw ratings provided by user.

![admin page](images/register7.png)

>Question Section

![admin page](images/1.png)

>Ratings Section

![admin page](images/2.png)

>one can logout of the site through logout button in navigation bar. 
---

##Technology Used to Build


- Html
- Css
- Python-Django
-  Argon2 Hasher
-  Bcrypt Hasher

---



