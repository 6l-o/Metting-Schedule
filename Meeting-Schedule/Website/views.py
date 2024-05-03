from flask import Blueprint, render_template, request, flash, jsonify,redirect, url_for
from flask_login import login_required, current_user
from .models import User
from . import db


views = Blueprint('views', __name__)
  


@views.route('/Dashboard', methods=['GET', 'POST'])
@login_required

def Dashboard():
       
    return render_template('Dashboard.html', user=current_user)

@views.route('/calendar', methods=['GET', 'POST'])
@login_required
def calendar():
    if request.method == 'POST':
        
        pass

    return render_template('calendar.html', user =current_user)

@views.route('/Availibility', methods=['GET', 'POST'])
@login_required
def Availibility():

    return render_template('Availibility.html', user =current_user)

@views.route('/Events', methods=['GET', 'POST'])
@login_required
def Events():

    return render_template('Events.html', user =current_user)

@views.route('/schedule_meeting', methods=['POST'])
@login_required
def schedule_meeting():
    meeting_data = request.get_json()
    # Extract meeting details from meeting_data
    # Save the meeting details in your database
    # You can use a Python ORM like SQLAlchemy for this
    # After saving the meeting details, return a success response
    return {"message": "Meeting scheduled successfully"}, 201