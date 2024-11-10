from flask import Flask, render_template

app = Flask(__name__) # It is a constructor that creates an instance of the Flask class. 
                      # The argument __name__ is a Python predefined variable, which is set to the name of the module in which it is used.

# @app.route('/') # This is a decorator that creates a mapping between the URL and the function hello_world.
# def hello_world():
#     return '<h1> Hello my World !sha </h1>'

# @app.route('/about') # This is a decorator that creates a mapping between the URL and the function about. This will be used to display the about page.
# def about_page():
#     return '<h1> About Page </h1>'

# @app.route('/about/<username>') # This is a decorator that creates a mapping between the URL and the function about. This will be used to display the about page.
# def about_page(username):
#     return f'<h1> This is about page of {username} </h1>'

@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html') # This function returns the home.html file. The render_template function is used to render the HTML file.

# We should use /home or / in the URL to access the home page. ( above code )

@app.route("/market")
def market_place():
    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    ]
    return render_template('market.html', items=items) # This function returns the market.html file. The render_template function is used to render the HTML file. 
