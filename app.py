from flask import Flask,request,jsonify,render_template
from utils import util
app=Flask(__name__)

@app.route('/')
def home():
    location=util.get_location_name()
    print(location)
    return render_template('app.html',location=location)
@app.route('/predict_house_price',methods=['GET','POST'])
def predict_house_price():
    if request.method == 'POST':
        print(request.form)
        sqft = float(request.form['Squareft'])
        bhk = float(request.form.get("allbhk"))
        bath = float(request.form.get('allbath'))
        location = request.form['selectedlocation']
        houseprice=util.get_estimated_price(location, sqft, bhk, bath)
        print(houseprice)
        houseprice=f"{houseprice} Lakhs"
        location = util.get_location_name()

        return render_template('app.html',houseprice= houseprice,location= location)

    else:
        location = util.get_location_name()
        return render_template('app.html', location=location)


if __name__=="__main__":
    print("lets start bangalore house price prediction")
    util.load_saved_modeldetails()
    print(util.__location)
    print(util.__data_columns)
    app.run(debug=True,port=5000)