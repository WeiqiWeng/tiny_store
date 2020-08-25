from tiny_store import tiny_store_app
from tiny_store.models import AdminModel

from .constants import ADMIN_USERTYPE, DEFAULT_USERTYPE, DB_CONFIG_KEYS, MIN_PASSWORD_LENGTH, DB_CONFIG

from flask import request, render_template, flash, abort, url_for, redirect, session, Flask, g

import re


@tiny_store_app.route('/admin', methods=['GET'])
def admin():

    if 'logged_in' in session and session['logged_in'] and session['usertype'] == ADMIN_USERTYPE:

        with AdminModel(DB_CONFIG) as admin_model:
            all_products = admin_model.get_all_products()
            all_groups = admin_model.get_all_groups()
            all_users = admin_model.get_all_ordinary_users()

            session['all_products'] = all_products
            session['all_groups'] = all_groups
            session['all_users'] = all_users
            
        return render_template(
            'admin_dash_board.html', 
            all_products=all_products, 
            all_groups=all_groups, 
            all_users=all_users)
    else:
        return redirect(url_for('land'))


@tiny_store_app.route('/admin/add_product_to_group', methods=['POST'])
def add_product_to_group():

    msg = ''

    if 'logged_in' in session and session['logged_in'] and session['usertype'] == ADMIN_USERTYPE:

        product_id = int(request.form['product_id'])
        group_id = int(request.form['group_id'])

        admin_model = AdminModel(DB_CONFIG)
        dulication = admin_model.check_duplicated_product_id_to_group_id_mapping(group_id, product_id)

        if dulication:
            msg = "重复添加"        
        else:
            result = admin_model.add_product_id_to_group_id_mapping(group_id, product_id)       
            msg = "添加成功" if result else "添加失败"

        admin_model.close()
            
        return render_template(
            'admin_dash_board.html', 
            all_products=session['all_products'], 
            all_groups=session['all_groups'], 
            add_product_to_group_msg=msg)

    return redirect(url_for('dashboard'))

@tiny_store_app.route('/admin/add_product_group', methods=['POST'])
def add_product_group():

    if 'logged_in' in session and session['logged_in'] and session['usertype'] == ADMIN_USERTYPE:
        
        msg = ''
        group_description = request.form['group_description']
        
        for group in session['all_groups']:
            if group['description'] == group_description:
                msg = "该注释组别已存在"
                break

        if msg:
            return render_template(
                'admin_dash_board.html', 
                all_products=session['all_products'], 
                all_groups=session['all_groups'], 
                add_product_group_msg=msg)

        with AdminModel(DB_CONFIG) as admin_model:
            result = admin_model.add_product_group(group_description)
            all_groups = admin_model.get_all_groups()
            session['all_groups'] = all_groups
            msg = "添加成功" if result else "添加失败"

        return render_template(
            'admin_dash_board.html', 
            all_products=session['all_products'], 
            all_groups=session['all_groups'], 
            add_product_group_msg=msg)

    return redirect(url_for('dashboard'))

@tiny_store_app.route('/admin/add_user_to_group', methods=['POST'])
def add_user_to_group():

    msg = ''

    if 'logged_in' in session and session['logged_in'] and session['usertype'] == ADMIN_USERTYPE:

        user_id = request.form['user_id']
        group_id = int(request.form['group_id'])

        admin_model = AdminModel(DB_CONFIG)
        dulication = admin_model.check_duplicated_user_id_to_group_id_mapping(group_id, user_id)

        if dulication:
            msg = "重复添加"        
        else:
            result = admin_model.add_user_id_to_group_id_mapping(group_id, user_id)       
            msg = "添加成功" if result else "添加失败"

        admin_model.close()
            
        return render_template(
            'admin_dash_board.html',          
            all_products=session['all_products'], 
            all_groups=session['all_groups'],
            all_users=session['all_users'],
            add_user_to_group_msg=msg)

    return redirect(url_for('dashboard'))

    
