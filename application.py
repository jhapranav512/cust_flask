from project import create_app
from flask_restx import Api
from project.blueprint import api_bp
from project.root.controller import namespace as root_ns
from project.customer.controller import namespace as cust_ns

protected_api = Api(
    api_bp,
    title="Customer API",
    description="Customer documentation and testing",
    version="1.0",
    authorizations={
        "Bearer": {
            "type": "apiKey",
            "in": "header",
            "name": "Authorization",
        }
    },
    doc='/swagger',
)
protected_api.add_namespace(root_ns, path='/')
protected_api.add_namespace(cust_ns, path='/customer')
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
