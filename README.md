# CS50 Final Project - Yellow pages
#### Video Demo:  [video](https://icedrive.net/0/9c1qM5EccI)
#### Description:
A public phone book for users from all around the globe using Flask simple and straight to use, users are welcomed with the homepage which lists all the users already registered in the webapp, in the top left you can see 4 options (homepage, login , logout, register) the login page requires you to enter the username and the password below the submit button you can see the show password tick box and the remember me one, next the register page which has 4 fields the first one is for the username the other two to check for password match the last one is for the birth dates of the user trying to register a new account, finally we get to the logout page which simply redirects to the homepage 

After creating an account you can press on the name and it will redirect you to the private route ```edit/<id>``` where id is your id in the database, then you will see an input field for a phone number if you want to add your phone number, if you discide to decide to delete your account you can press the delete word in the hompage which will take your to the private webpage which contains a field where you will be asked to enter your password to delete the account from the database 

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
