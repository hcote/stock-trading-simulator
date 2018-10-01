from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method=='POST':
    ticker = request.form['ticker']
    return render_template('index.html', ticker = ticker)
  
if __name__ == "__main__":
    app.run()

