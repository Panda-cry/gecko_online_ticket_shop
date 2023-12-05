from flask_jwt_extended import jwt_required, verify_jwt_in_request, get_jwt
from flask import jsonify
from typing import List


def check_role(role_types:  List):
    def decorator(fn):
        @jwt_required()
        def wrapper(*args, **kwargs):
            verify_jwt_in_request()
            current_claim_value = get_jwt().get('user_type')

            if current_claim_value not in role_types:
                return jsonify \
                    (message=f"Unauthorized. Expected user_type to be {role_types}."), 403

            return fn(*args, **kwargs)

        return wrapper

    return decorator
