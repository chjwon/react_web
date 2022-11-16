# app.py
from flask import Flask, render_template, request
from flask_cors import CORS
from xai.Diabetes_Health_Indicators.model import dh_model
from xai.Heart_Disease.model import hd_model

app = Flask(__name__)
CORS(app)

@app.route('/') 
def index():
  return render_template('index.html')


@app.route('/heartdisease/data',methods=["POST"])
def heartdisease_data():
  data = request.get_json()["data"]
  result = hd_model(data)
  return {"result" : result}

@app.route('/diabete/data',methods=["POST"])
def diabete_result():
  data = request.get_json()["data"]
  result = dh_model(data)
  return {"result" : result}


if __name__=="__main__":
  #app.run(debug=True)
  app.run(host="127.0.0.1", port="8000", debug=True)