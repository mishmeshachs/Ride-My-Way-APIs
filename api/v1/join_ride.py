from flask import Flask, jsonify,request
app = Flask(__name__)
rides =[
    {'rideId':'aab','name of driver':'Allan','Title':'Around Town','Price':'2000','Destination': 'Mulago','Action': '[]'},
    {'rideId':'abc','name of driver':'Charity','Title':'Up Country','Price':'10000','Destination': 'Jinja','Action': '[]'},
    {'rideId':'acb','name of driver':'David','Title':'Around Town','Price':'4000','Destination': 'Bukoto','Action': '[]'},
]

@app.route('/joinride', methods =['POST'])
def joinride():
    request_data = request.get_json()
    new_ride = {[{'rideId':request.json['rideId']}, {'name of driver':request.json['name']}, {'Title':request.json['Title']},
     {'Price':request.json['Price']},{'Destination':request.json['Destination']}]}
    rides.append(new_ride)
    return jsonify(new_ride)
if __name__ == '__main__':
    app.run()