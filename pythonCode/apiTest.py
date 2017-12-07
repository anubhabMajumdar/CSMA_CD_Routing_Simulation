from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask.json import jsonify
from flask import render_template
from flask_cors import CORS
import WAN

# db_connect = create_engine('sqlite:///chinook.db')
app = Flask(__name__)
CORS(app)
api = Api(app)

count = 0
# class Employees(Resource):
#     def get(self):
#         statuses = ["Ready", "Ready"]
#         return jsonify(statuses)


# class Tracks(Resource):
#     def get(self):
#         conn = db_connect.connect()
#         query = conn.execute("select trackid, name, composer, unitprice from tracks;")
#         result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
#         return jsonify(result)

# class Employees_Name(Resource):
#     def get(self, employee_id):
#         conn = db_connect.connect()
#         query = conn.execute("select * from employees where EmployeeId =%d "  %int(employee_id))
#         result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
#         return jsonify(result)

@app.route("/", methods=['GET'])
def hello():
	wan = WAN.runCodeRun()
	d = {}
	for i in range(4):
		d[wan.lan1.nodeList[i].id] = {"status": wan.lan1.nodeList[i].status, "to": wan.lan1.nodeList[i].curReceiver}
		d[wan.lan2.nodeList[i].id] = {"status": wan.lan2.nodeList[i].status, "to": wan.lan2.nodeList[i].curReceiver}
	return jsonify(d)

@app.route('/signup')
def signUp():
	return render_template('signUp.html')


# api.add_resource(Employees, '/employees') # Route_1
# api.add_resource(Tracks, '/tracks') # Route_2
# api.add_resource(Employees_Name, '/employees/<employee_id>') # Route_3


if __name__ == '__main__':
	 app.run(port=5002)