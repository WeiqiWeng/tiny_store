from tiny_store import tiny_store_app
from tiny_store.models import ProductModel

from .constants import DB_CONFIG, GRID_PER_ROW

from flask import request, render_template, flash, abort, url_for, redirect, session, Flask, g

import math


def divide_products_into_rows(products):

    num_rows = int(math.ceil(len(products) / GRID_PER_ROW))
    return [products[i * GRID_PER_ROW : (i + 1) * GRID_PER_ROW] for i in range(num_rows)]

@tiny_store_app.route('/product', methods=['GET'])
def product():

    default_products = session['default_products']

    with ProductModel(DB_CONFIG) as product_model:
        personalized_products = product_model.get_personalized_products_by_user_id(session['user_id'])

    personalized_products_divided_into_rows = divide_products_into_rows(personalized_products)
    default_products_divided_into_rows = divide_products_into_rows(default_products)

    return render_template(
        'user_dash_board.html', 
        default_products=default_products_divided_into_rows, 
        personalized_products=personalized_products_divided_into_rows)
                
