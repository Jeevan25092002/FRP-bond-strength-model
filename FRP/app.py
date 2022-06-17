import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open(r'C:\Users\JEEVANRAJENDRAN\Desktop\intern pro2\end_t0_end 4\model\model1.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index2.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    # output = round(prediction[0], 2)

    return render_template('index2.html', prediction_text=' bond strength{} KN'.format(int(prediction)))

if __name__ == "__main__":
    app.run(debug=True)