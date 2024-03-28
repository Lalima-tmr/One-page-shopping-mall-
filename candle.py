#importing necessary functions from dotenv library

from flask import Flask, render_template, jsonify, request

from pymongo import MongoClient

client = MongoClient('Your mongoDB Atlas URL here')
db = client.dbhomework

app = Flask(__name__)

## HTML
@app.route('/')
def homework():
    return render_template('candle.html')


# POST API
@app.route('/order', methods=['POST'])
def save_order():
    name = request.form['name']
    count = request.form['count']
    address = request.form['address']
    phone = request.form['phone']
    print(name,count,address,phone)

    db.homework.insert_one ({
        'name': name,
        'count': count,
        'address': address,
        'phone': phone
    })

    return jsonify({'result': 'success'})


# Read API
@app.route('/order', methods=['GET'])
def view_orders():
    orders = list(db.homework.find({}, {'_id': False}))
    return jsonify({'result': 'success', 'orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
