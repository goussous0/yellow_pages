# CS50 Final Project - Yellow pages

A public phone book for users from all around the globe using Flask simple and straight to use 

Technologies used:

- Flask 
- pyjwt
- javascript
- 

## How the webpage works?

The idea is simple, go to the registration page, then During registration you need to enter these fields:

- Username
- password
- confirmation : it is checked to match, 
- Checkbox to show passowrd 

### Routing

The public routes are:
- register 
- login 
- homepage 
The private routes are:
- edit
- remove 

### Sessions
Using pyjwt when you login in you will be given a token with 1440 minutes life time, then you have to log in again 
### Database

The data base contains the birthday , name , phone number and ofcourse the index for each user registered in the web app 

## Possible improvements

As all applications this one can also be improved. Possible improvements
- choosing language for non russian speakers 
- adding social media links and profile names 
- lookup webpage for a phone number or user name 

## How to launch application

1. ```pip3 install -r requirements.txt``` to install packages
2. ```python3 app.py initdb``` to create the database
3. ```python3 app.py runserver --host 0.0.0.0 --port 8080``` to host on local machine with ip 0.0.0.0 and port 8080
