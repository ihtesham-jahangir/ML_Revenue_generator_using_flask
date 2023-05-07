import pickle
from flask import Flask , request , render_template

app = Flask(__name__)
model = pickle.load(open('model1.pkl','rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict' , methods = ['POST','GET'])
def predict():
    prediction = model.predict([[float(request.form['Temprature'])]])
    output = round(prediction[0],2)
    print(output)
    return render_template('index.html' , prediction_text = f'Generate Revenue RS {output}-/')


if __name__ =='__main__':
    app.run(debug = True)


