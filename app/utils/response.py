from flask import jsonify


class Response:
    @staticmethod
    def create(response, status_code: int):
        return jsonify({
            'status_code': status_code,
            'response': response
        })
