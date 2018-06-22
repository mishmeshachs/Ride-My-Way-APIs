"""YOU SHALL BE ABLE TO SEE ALL THE RIDE OFFERS IN JSON FORM. I USED DICTIONARIES AND LIST AS
MY DATA STRUCTURES"""
from flask import Flask, jsonify,request
app = Flask(__name__)
rides =[
    {'name of driver':'Allan','Title':'Around Town','Price':'2000','Destination':'Mulago'},
    {'name of driver':'Charity','Title':'Up Country','Price':'10000','Destination':'Jinja'},
    {'name of driver':'David','Title':'Around Town','Price':'4000','Destination':'Bukoto'},
]

@app.route('/rides', methods =['GET'])
def returnAll():
    return jsonify ({'rides':rides})

if __name__ == '__main__':
    app.run()