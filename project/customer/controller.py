from flask import Flask, jsonify, request
from flask_restx import Namespace, Resource
namespace = Namespace('cust', description='cutomer information')

customer_ino = []


@namespace.route('')
class Customer(Resource):
    def get(self):
        return jsonify(customer_ino)

    def post(self):
        data = request.json
        customer_ino.append(data)
        return {"message": "data poasted"}, 200


@namespace.route('/<string:id>')
class CustomerById(Resource):
    def get(self, id):
        for cust in customer_ino:
            if str(cust['id']) == id:
                return cust
