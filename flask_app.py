from flask import Flask, render_template, request
from model import dtc_model

app = Flask(__name__)
@app.route('/',methods=['GET','POST'])

def weather():
    if request.method == 'GET':
        print("Get Request Received")
        return render_template('weather.html')
    elif request.method == 'POST':
            print("Post Request Received")
            temperature = float(request.form.get('temperature'))
            humidity = float(request.form.get('humidity'))
            wind_speed = float(request.form.get('wind_speed'))
            prediction = dtc_model.predict([[temperature, humidity, wind_speed]])

            k = prediction[0]
            if k == "Rainy":
                result = "Rainy"
            elif k == "Sunny":
                result = "Sunny"
            elif k == "Cloudy":
                result = "Cloudy"
            return render_template('weather.html',result=result)

if __name__ == '__main__':
    app.run(debug=True)
