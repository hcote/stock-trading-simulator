from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask (__name__)

# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'stockTradingSimulator'

mysql = MySQL(app)

@app.route("/", methods=['GET'])
def index():
    # ticker = request.form['ticker']
    return render_template('index.html')
  
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
  
if __name__ == "__main__":
    app.run()

