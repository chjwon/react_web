# app.py
from flask import Flask, render_template, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/') 
def index():
  return render_template('index.html')

@app.route('/test1', methods = ['GET']) 
def test1():
  print(request.args.get('testVal'))
  return {"result" : "Test result alpha"}

@app.route('/test2', methods = ['GET']) 
def test2():
  print(request.args.get('testVal'))
  return {"result" : "Test result beta"}

if __name__=="__main__":
  #app.run(debug=True)
  app.run(host="127.0.0.1", port="5000", debug=True)