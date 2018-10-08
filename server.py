from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL

app = Flask (__name__)

# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'r60Q!lof$'
app.config['MYSQL_DB'] = 'stockTradingSimulator'

mysql = MySQL(app)

@app.route("/", methods=['GET'])
def index():
    # ticker = request.form['ticker']
    return render_template('index.html')

@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    print(request.environ)
    return jsonify({'ip': request.remote_addr}), 200
  
@app.route("/signup", methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        print(request)
        # fetch form data
        user_datails = request.form
        username = user_datails['username']
        password = user_datails['password']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO users(username, password) VALUES(%s, %s)', (username, password))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('signup.html')
  
# route to show users
@app.route("/users", methods=['GET'])
def users():
    cur = mysql.connection.cursor()
    results = cur.execute('SELECT * FROM users')
    if results > 0:
        user_details = cur.fetchall()
        return render_template('users.html', user_details = user_details)

# route to show stocks
@app.route("/stocks", methods=['GET'])
def stocks():
    cur = mysql.connection.cursor()
    results = cur.execute('SELECT * FROM stocks')
    if results > 0:
        all_stocks = cur.fetchall()
        return render_template('stocks.html', all_stocks = all_stocks)

# seeding db with stock data
# @app.route("/seeddata", methods=['GET'])
# def seeddata():
#     for 
#     cur = mysql.connection.cursor()
#     cur.execute('INSERT INTO stocks (id, ticker, name) VALUES(%s, %s, %s)', (username, password))
#     mysql.connection.commit()
#     cur.close()
#     return 'success'
# return render_template('signup.html')

if __name__ == "__main__":
    app.run()

