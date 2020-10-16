from flask import Blueprint

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/get_data')
def get_data():
    return {'key': 'value'}
