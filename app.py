from flask import Flask,render_template,request

app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")



@app.route('/predection')
def predections():
    return render_template("prediction.html")



if  __name__ == '__main__':
    app.run(debug=True)