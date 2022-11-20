from flask import Flask,render_template,jsonify
from boston_app.utils import Boston
import config

app = Flask(__name__)

@app.route("/")
def welcome():
    return "welcome to the boston price prediction"

@app.route("/predict")
def predict_price():
    CRIM      =   0.05724
    ZN         =  0.00000
    INDUS      =  4.24000
    CHAS       =  0.00000
    NOX        =  0.46000
    RM         =  6.33300
    AGE       = 15.20000
    DIS        =  7.21460
    RAD        =  2.00000
    TAX       = 450.00000
    PTRATIO    = 17.90000
    B          =370.21000
    LSTAT      =  8.34000    
    bos_child = Boston(CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B, LSTAT)
    price = bos_child.get_price()

    return jsonify({"return": f"predicted price is : {price}"})

if __name__ == "__main__":

    app.run()
