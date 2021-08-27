from flask import Blueprint ,render_template, request, url_for ,abort, flash, redirect , send_file ,make_response , send_from_directory
from flask import session 
from flask import jsonify 



from models import db
from models import User 

from flask_login import login_user, logout_user 

from werkzeug.utils import secure_filename
from flask import current_app

from werkzeug.security import generate_password_hash, check_password_hash

from config import config


from functools import wraps

import requests
import jwt
import re 
import random 
import string 
from datetime import datetime , timedelta
import os 




def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        

       


        try:
            if not session['t0k3n'] :
            	print ("Error No t0k3n found")
            	return jsonify({"status": "error","message": {"token": "Токен истёк"}})
            else :
                data = jwt.decode( session['t0k3n'] , current_app.config['SECRET_KEY'] , algorithms="HS256")
                if data['usr'] == session['usr']:
                    return  f( *args, **kwargs)
                
                else:
                	return redirect(url_for('ui.home'))
                    

        except :
        	return redirect(url_for('ui.home'))


        
        return  f( *args, **kwargs)
  
    return decorated






ui = Blueprint('ui', __name__, static_folder='static', static_url_path='/static/ui', template_folder='templates')



@ui.route('/')
@ui.route('/home' , methods=['GET'])
def home():
	''' display users info for loged in users  '''
	all_users = User.query.all()
	return render_template('home.html', all_users=all_users )


    


@ui.route('/logout')
def logout():
	''' logout and remove session values ''' 
	session.pop('token', None )
	session.pop('email', None )
	return redirect(url_for('ui.home'))




@ui.route('/signup', methods=['POST', 'GET'])
def signup():
	



    if request.method == 'POST':

    	## GRAB VALUES FROM FORM
    	usr_name = request.form['usr']
    	passwrd = request.form['pass']
    	bday = datetime.strptime(request.form['bday'] , '%Y-%m-%d')

    	usr = User.query.filter_by(username=usr_name).first()

    	if not usr:
    		new_usr = User(username=usr_name , password=generate_password_hash(passwrd, method='sha256') , birth_day=bday )
    	
    		
    		db.session.add(new_usr)
    		db.session.commit()

    		return redirect(url_for('ui.login'))

    	else:

    		flash(f"User with name {usr_name} is already registered ")
    		return render_template('signup.html')
    else:
    	return render_template('signup.html')



    

@ui.route('/reset', methods=['GET', 'POST'])
def reset():
	''' This part is for password reset with an email letter  ''' 

	if request.form == 'POST':

		usr_email = request.form['email']




		return render_template('reset.html')



	else:

		return render_template('reset.html')
	


















@ui.route('/login', methods=['GET' , 'POST'])
def login():
	''' basic login authentication process  ''' 

	if request.method == "POST":

		if request.form.get('rememberMe') :
			usr_name = session['usr']

		else:

			usr_name = request.form['usrname']
		passwrd = request.form['passwrd']
		
		
		check_usr = User.query.filter_by(username=usr_name).first()

		if check_usr and check_password_hash(check_usr.password , passwrd ): 
			flash("Loggin in ... ")

			session['usr'] = usr_name
			payload_data = {"usr":f"{usr_name}",
							"exp":datetime.utcnow() + timedelta(minutes=1440)}
			
			token = jwt.encode(payload_data , current_app.config['SECRET_KEY'], algorithm="HS256" )

			
			session['t0k3n'] = token
			





			return redirect(url_for('ui.home'))


		else:

			flash("Wrong credintails ")
		
			return redirect(url_for('ui.login'))



	else:

		return render_template('login.html')








@ui.route('/remove/<id>' , methods=['GET', 'POST'])
@token_required
def remove(id):
	''' delete this user's account  ''' 

	rm_usr = User.query.get(id)
	if request.method == 'POST':

		if rm_usr.username == session['usr'] :

			usr = request.form['rm_usr']
			pass_wrd = request.form['pass']

			


			if check_password_hash(rm_usr.password , pass_wrd) :
				User.query.filter(User.id == id).delete()
				db.session.commit()



				return redirect(url_for('ui.logout'))
			else:
				return redirect(url_for('ui.home'))


			return render_template('delete.html')
	else:

		return render_template('delete.html')





def get_nums():

	all_nums = User.query.all()

	phones = [ usr.phone_number for usr in all_nums ]

	return phones 






@ui.route('/edit/<id>', methods=['GET','POST'])
@token_required
def edit(id):




	usr = User.query.get(id)

	if request.method == 'POST':
		## check if the same user trying to make changes
		if usr.username == session['usr'] :

			## check for a phone number or a name change to edit this info 

			phone_num = request.form['phoneNumber']

			if phone_num not in get_nums():
				usr.phone_number = phone_num
				db.session.commit()
				return redirect(url_for('ui.home'))

			else:
				flash( f"This phone number belongs to another user ")
				return render_template('edit.html')


		else:
			flash('Wrong username or invalid token ')

			return render_template('edit.html')





	else:
		return render_template('edit.html')






@ui.route('/filter/<letters>')
def filt(letters):
	''' filter users based on letters in each button '''
	all_users = User.query.all()

	filtered = [] 

	for item in all_users:

		if str(item.username[0]).upper() in list(letters):
			filtered.append(item)


	return render_template ('home.html' , all_users=filtered)

