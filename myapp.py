from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import numpy as np
import pickle
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template ('login.html')

@app.route('/predict',methods = ['POST'])
def get_result():
    poly = pickle.load(open('Poly.pkl','rb'))
    model = pickle.load(open('model.pkl','rb'))
    query = [[float(request.form['exp'])]]
    X_query = poly.transform(query)
    sal = model.predict(X_query)
    return 'Dear'+request.form ['name']+'your predict salary '+request.form['exp']+'Experience'+str(sal)

if __name__=='__main__':
     app.run(debug=True)