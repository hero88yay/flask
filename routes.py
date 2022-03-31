from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/Buy')
def buy():
    items=[
         {'id': 1, 'name': 'ferrari_458', 'car_id':'123456', 'price': 350000},
         {'id': 2, 'name': 'nissan_gtr', 'car_id':'1234567', 'price': 582000},
         {'id': 3, 'name': 'nissan_skyline', 'car_id':'12345678', 'price': 220000},
         {'id': 4, 'name': 'lamborghini_gallardo', 'car_id':'12345659', 'price': 250000},
         {'id': 5, 'name': 'bmw_m8', 'car_id':'12345625', 'price': 120000},]

    return render_template('buy.html', items=items)



   