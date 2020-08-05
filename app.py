from flask import Flask
from flask import Flask, render_template, request
import pickle

app = Flask('stock_pricer')
model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def show_predict_stock_form():
    return render_template("home.html")

@app.route('/result',methods = ['POST'])
def result():
	a = request.form["V/Vc"]
	b = request.form["Cross_Section"]
	c = request.form["Sediment_Gradation"]
	d = request.form["size_of_grain"]
	e = request.form["Time_of_experiment"]
	arr = [[a,b,c,d,e]]
	prediction = model.predict(arr)
	return render_template("home.html",prediction_text = "predected scour depth is {}".format(prediction))