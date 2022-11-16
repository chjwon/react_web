# app.py
from flask import Flask, render_template, request
from flask_cors import CORS
from xai.Diabetes_Health_Indicators.model import dh_model
# from ..xai.Heart_disease.model import hd_model

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


@app.route('/heartdisease/data',methods=["POST"])
def heartdisease_data():
  data = request.get_json()
  print(data)
  return data

@app.route('/diabete/data',methods=["GET"])
def diabete_result():
  temp = [0.0,2.0,0.0,1.0,26.0,0.0,0.0,0.0,1.0,0.0,1.0,0.0,1.0,0.0,3.0,5.0,30.0,0.0,1.0,4.0,6.0,8.0]
  result = dh_model(temp)
  print("aaaaaaaaaaa",result)
  return result

if __name__=="__main__":
  #app.run(debug=True)
  app.run(host="127.0.0.1", port="5000", debug=True)