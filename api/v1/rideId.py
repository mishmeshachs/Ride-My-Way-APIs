from flask import Flask, jsonify,request
app = Flask(__name__)
rides =[
    {'rideId':'aab','name of driver':'Allan','Title':'Around Town','Price':'2000','Destination': 'Mulago'},
    {'rideId':'abc','name of driver':'Charity','Title':'Up Country','Price':'10000','Destination': 'Jinja'},
    {'rideId':'acb','name of driver':'David','Title':'Around Town','Price':'4000','Destination': 'Bukoto'},
]

@app.route('/rides/<string:rideId>', methods =['GET'])
def returnOne(rideId):
    rideIds =[ridesId for ridesId in rides if ridesId['rideId']== rideId]
    return jsonify({'ridesId':rideIds[0]})

if __name__ == '__main__':
    app.run()