from datetime import datetime
from flask import render_template, session, redirect, url_for, flash
from . import main
from .forms import NameForm
import pygsheets
from .contexts import *

#authorization

gc = pygsheets.authorize(service_file=GOOGLE_SERVICE_KEY)
sh = gc.open(GOOGLE_SPREADSHEET_NAME)
wks = sh.worksheet('title', GOOGLE_WORKSHEET)

@main.route('/', methods=['GET', 'POST'])
def index():
	list=wks.get_row(row=2)[1:21]
	if int(list[5])>50:
		flash("Air is not so good")
		

	return render_template('index.html', list=list,url_for=url_for,
							current_time=datetime.utcnow())
