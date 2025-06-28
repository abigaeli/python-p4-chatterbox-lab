from flask import Flask, request, make_response, jsonify
from flask_cors import CORS
from flask_migrate import Migrate

from .models import db, Message


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)
migrate = Migrate(app, db)

db.init_app(app)

from flask import request, jsonify, make_response

@app.route('/messages', methods=['GET', 'POST'])
def messages():
    if request.method == 'GET':
        messages = Message.query.order_by(Message.created_at.asc()).all()
        return jsonify([message.to_dict() for message in messages])
    elif request.method == 'POST':
        data = request.get_json()
        body = data.get('body')
        username = data.get('username')
        if not body or not username:
            return make_response(jsonify({'error': 'body and username are required'}), 400)
        new_message = Message(body=body, username=username)
        db.session.add(new_message)
        db.session.commit()
        return jsonify(new_message.to_dict()), 201

@app.route('/messages/<int:id>', methods=['PATCH', 'DELETE'])
def messages_by_id(id):
    message = Message.query.get_or_404(id)
    if request.method == 'PATCH':
        data = request.get_json()
        body = data.get('body')
        if not body:
            return make_response(jsonify({'error': 'body is required'}), 400)
        message.body = body
        db.session.commit()
        return jsonify(message.to_dict())
    elif request.method == 'DELETE':
        db.session.delete(message)
        db.session.commit()
        return make_response('', 204)

if __name__ == '__main__':
    app.run(port=5555)
