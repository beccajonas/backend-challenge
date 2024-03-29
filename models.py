from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin
from dotenv import load_dotenv
from sqlalchemy.orm import relationship
import requests

load_dotenv()

metadata = MetaData(
    naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }
)
db = SQLAlchemy(metadata=metadata)

association_table = db.Table('association', db.Model.metadata,
    db.Column('player_id', db.Integer, db.ForeignKey('players.id')),
    db.Column('lobby_id', db.Integer, db.ForeignKey('lobbies.id'))
)

class Lobby(db.Model, SerializerMixin):
    __tablename__ = 'lobbies'
    serialize_rules = ['-players.lobbies']
    id = db.Column(db.Integer, primary_key=True)
    details = db.Column(db.String)
    players = db.relationship('Player', secondary=association_table, back_populates='lobbies')

class Player(db.Model, SerializerMixin):
    __tablename__ = 'players'
    serialize_rules = ['-lobbies.players']
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    lobbies = db.relationship('Lobby', secondary=association_table, back_populates='players')
