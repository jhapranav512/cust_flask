from flask import Blueprint
from flask_restx import Namespace, Resource
print("root namespace created")
namespace = Namespace('root', description='Root Operation')


@namespace.route('')
class Root(Resource):
    def get(self):
        return {'status': 'OK'}
