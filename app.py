from flask import Flask, json, request, jsonify
from flask_socketio import SocketIO
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from dotenv import dotenv_values
from models import db, Lobby, Player

config = dotenv_values(".env")

app = Flask(__name__)
app.secret_key = config['FLASK_SECRET_KEY']
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)

db.init_app(app)

@app.get('/')
def index():
    return 'Puberry backend challenge'

@app.get('/lobbies')
def get_lobbies():
    lobbies = Lobby.query.all()
    return [lobby.to_dict() for lobby in lobbies]

@app.get('/players')
def get_players():
    players = Player.query.all()
    return [player.to_dict() for player in players]

@app.post('/create-player')
def create_player():
    username = request.json.get('username')
    
    existing_player = Player.query.filter_by(username=username).first()
    if existing_player:
        return jsonify({'message': 'Username already exists. Please choose a different username.'}), 400
    
    new_player = Player(username=username)
    db.session.add(new_player)
    db.session.commit()

    socketio.emit('player_created', {'id': new_player.id, 'username': new_player.username})

    return jsonify({'message': f'Player {username} created successfully'}), 201

@app.post('/create-lobby')
def create_lobby():
    details = request.json.get('details')  # Get lobby details from request
    new_lobby = Lobby(details=details) # Create new lobby instance 
    db.session.add(new_lobby)
    db.session.commit()

    socketio.emit('lobby_created', {'id': new_lobby.id, 'details': details})

    return jsonify({'message': 'Lobby created successfully'}), 201

@app.post('/join-lobby/<lobby_id>')
def join_lobby(lobby_id):
    lobby = Lobby.query.get(lobby_id)
    if not lobby:
        return jsonify({'message': 'Lobby not found'}), 404
    
    player_id = request.json.get('player_id')
    player = Player.query.get(player_id)
    if not player:
        return jsonify({'message': 'Player not found'}), 404
    
    lobby.players.append(player)
    db.session.commit()

    # Emit a Socket.IO event to notify that a player has joined a lobby
    socketio.emit('player_joined_lobby', {'player_id': player.id, 'lobby_id': lobby.id})

    # Check if the lobby has reached 2 players
    if len(lobby.players) == 2:
        # Emit a socket event to notify that the game has started
        print('game starts!')
        socketio.emit('game_started', {'message': f'2 players have joined Lobby {lobby.id}. Game has started!'})
        
    return jsonify({'message': f'Player {player.username} joined lobby {lobby.id} successfully'}), 200

@app.post('/leave-lobby/<lobby_id>/<player_id>')
def leave_lobby(lobby_id, player_id):
    lobby = Lobby.query.get(lobby_id)
    if not lobby:
        return jsonify({'message': 'Lobby not found'}), 404

    player = Player.query.get(player_id)
    if not player:
        return jsonify({'message': 'Player not found'}), 404

    if player not in lobby.players:
        return jsonify({'message': 'Player is not in the lobby'}), 400

    lobby.players.remove(player)
    db.session.commit()

    # Emit a Socket.IO event to notify that a player has left a lobby
    socketio.emit('player_left_lobby', {'player_id': player.id, 'lobby_id': lobby.id})

    return jsonify({'message': f'Player {player.username} left lobby {lobby.id} successfully'}), 200

if __name__ == '__main__':
    app.run(port=5555, debug=True)

