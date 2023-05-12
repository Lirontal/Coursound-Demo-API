from flask import Blueprint, current_app, jsonify
from app.models import User

bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    try:
        redis_client = current_app.extensions['redis']
        users = redis_client.get('users')

        if users is not None:
            # Assuming the users data is stored as a string representation of a list,
            # convert it to an actual list before returning
            users = eval(users.decode('utf-8'))

            return jsonify(users)

        users = User.query.all()
        user_list = [user.__dict__ for user in users]  # Convert User objects to dictionaries
        # Remove the unnecessary attributes added by SQLAlchemy
        user_list = [{key: user[key] for key in user.keys() if not key.startswith('_')} for user in user_list]
        redis_client.set('users', str(user_list))

        return jsonify(user_list)
    
    except Exception as e:
        # Handle the error and return an error response
        error_message = str(e)
        return jsonify({'error': error_message}), 500
