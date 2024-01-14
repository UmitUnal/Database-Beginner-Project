from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)


def get_data_from_db(table_name):
    conn = psycopg2.connect(
        database="Sahibinden",
        user="postgres",
        password="klayvert",
        host="localhost",
        port="5432"
    )

    cur = conn.cursor()

    query = f"SELECT * FROM {table_name}"
    cur.execute(query)

    data = cur.fetchall()

    cur.close()
    conn.close()

    return data


@app.route('/')
def index():
    return render_template('anasayfa.html')


@app.route('/categories')
def categories():
    table_data = get_data_from_db('categories')
    return render_template('table_template.html', page_title='Categories Table',
                           table_headers=['Category ID', 'Category Name'], table_data=table_data)


@app.route('/comments')
def comments():
    table_data = get_data_from_db('comments')
    return render_template('table_template.html', page_title='Comments Table',
                           table_headers=['Comment ID', 'Product ID', 'User ID', 'Comment Date'], table_data=table_data)


@app.route('/favories')
def favories():
    table_data = get_data_from_db('favories')
    return render_template('table_template.html', page_title='Favories Table',
                           table_headers=['Favorite ID', 'User ID', 'Product ID'], table_data=table_data)


@app.route('/orders')
def orders():
    table_data = get_data_from_db('orders')
    return render_template('table_template.html', page_title='Orders Table',
                           table_headers=['Order ID', 'User ID', 'Product ID', 'Order Date', 'Total Cost'],
                           table_data=table_data)


@app.route('/payments')
def payments():
    table_data = get_data_from_db('payments')
    return render_template('table_template.html', page_title='Payments Table',
                           table_headers=['Payment ID', 'User ID', 'Card Number', 'Expiration Date', 'CVV Number'],
                           table_data=table_data)


@app.route('/products')
def products():
    table_data = get_data_from_db('products')
    return render_template('table_template.html', page_title='Products Table',
                           table_headers=['Product ID', 'User ID', 'Category ID', 'Price', 'Product Age', 'Date',
                                          'Product Status'], table_data=table_data)


@app.route('/users')
def users():
    table_data = get_data_from_db('users')
    return render_template('table_template.html', page_title='Users Table',
                           table_headers=['User ID', 'Name', 'Surname', 'Email', 'Password', 'Phone Number'],
                           table_data=table_data)


@app.route('/query', methods=['GET', 'POST'])
def query():
    if request.method == 'POST':
        query_text = request.form.get('query_text')
        if query_text:
            result = execute_query(query_text)
            return render_template('query_template.html', page_title='Query Result', query_text=query_text,
                                   result=result)

    return render_template('query_template.html', page_title='Query Page')


def execute_query(query):
    conn = psycopg2.connect(
        database="Sahibinden",
        user="postgres",
        password="klayvert",
        host="localhost",
        port="5432"
    )

    cur = conn.cursor()
    cur.execute(query)
    result = cur.fetchall()
    cur.close()
    conn.close()

    return result


if __name__ == '__main__':
    app.run(debug=True)
