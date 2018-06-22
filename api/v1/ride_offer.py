from flask import Flask, jsonify,request
app = Flask(__name__)
rides =[{'rideId':'aab','name of driver':'Allan','Title':'Around Town','Price':'2000','Destination': 'Mulago'},
{'rideId':'abc','name of driver':'Charity','Title':'Up Country','Price':'10000','Destination': 'Jinja'},
{'rideId':'acb','name of driver':'David','Title':'Around Town','Price':'4000','Destination': 'Bukoto'},
]

@app.route('/rides', methods =['GET'])
def returnAll():
    return jsonify ({'rides':rides})

@app.route('/rides', methods =['POST'])
def addOne():
    ride =[{'rideId':request.json['rideId']}, {'name of driver':request.json['name']}, {'Title':request.json['Title']}, {'Price':request.json['Price']},{'Destination':request.json['Destination']}]
    rides.append(ride)
    return jsonify ({'rides':rides})

if __name__ == '__main__':
    app.run()