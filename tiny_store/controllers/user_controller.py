from tiny_store import tiny_store_app
from tiny_store.models import UserModel

from .constants import ADMIN_USERTYPE, DEFAULT_USERTYPE, DB_CONFIG_KEYS, MIN_PASSWORD_LENGTH

from flask import request, render_template, flash, abort, url_for, redirect, session, Flask, g

import re


DB_CONFIG = {key: tiny_store_app.config[key] for key in DB_CONFIG_KEYS}

@tiny_store_app.route('/login', methods=['GET', 'POST'])
def login():

    msg = ' '

    if request.method == 'POST':
        if 'username' in request.form and 'password' in request.form:
            username = request.form['username']
            password = request.form['password']

            with UserModel(DB_CONFIG) as user_model:
                account_info = user_model.get_login_account_info(username, password)

            if account_info and account_info.get('id', None) is not None:
                session['logged_in'] = True
                session['id'] = account_info['id']
                session['username'] = account_info['username']
                session['usertype'] = account_info['usertype']
                
                return redirect(url_for('dashboard'))                   
            else:
                msg = '用户名/密码有误'                

    return render_template('index.html', msg=msg)

@tiny_store_app.route('/dashboard', methods=['GET'])
def dashboard():

    if 'logged_in' in session and session['logged_in']:
        if session['usertype'] == ADMIN_USERTYPE:
            return render_template('user/admin_dash_board.html', username=session['username'])
        elif session['usertype'] == DEFAULT_USERTYPE:
            return render_template('user/user_dash_board.html', username=session['username'])

    return redirect(url_for('login'))

def check_email_address(email_string):

    return re.match(r'[^@]+@[^@]+\.[^@]+', email_string)

def check_username(username):

    return username.isalnum()

def check_password_length(password):

    return (len(password) > MIN_PASSWORD_LENGTH)    


@tiny_store_app.route('/register', methods=['GET', 'POST'])
def register():

    msg = ' '

    if request.method == 'POST':
        if 'username' in request.form and 'password' in request.form and 'email' in request.form:
            username = request.form['username']
            password = request.form['password']
            email = request.form['email']  

            if (not username) or (not password) or (not email):
                msg = '请输入用户名、密码和邮箱'
                return render_template('user/register.html', msg=msg)              

            if not check_email_address(email):
                msg = '无效邮箱'
                return render_template('user/register.html', msg=msg)

            if not check_username(username):
                msg = '用户名仅可包含字母和数字'
                return render_template('user/register.html', msg=msg)

            if not check_password_length(password):
                msg = '密码至少6位'
                return render_template('user/register.html', msg=msg)                  

            user_model = UserModel(DB_CONFIG)
            duplication = user_model.check_duplicated_username(username)

            if duplication:
                msg = '用户名已存在'
            else:
                success = user_model.register_ordinary_user(username, password, email)
                if success:
                    return redirect(url_for('dashboard'))
                else:
                    msg = '注册失败，请重试'
                    return render_template('user/register.html', msg=msg)  
        else:
            msg = '请输入用户名、密码和邮箱'
                
    return render_template('user/register.html', msg=msg)

@tiny_store_app.route('/logout', methods=['GET'])
def logout():
    
    session.pop('logged_in', None)
    session.pop('id', None)
    session.pop('username', None)
    session.pop('usertype', None)
   
    return redirect(url_for('login'))


                
