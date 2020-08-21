from tiny_store import tiny_store_app

from flask import request, render_template, flash, abort, url_for, redirect, session, Flask, g


@tiny_store_app.route('/')
def land():

	return render_template('index.html')
	            
