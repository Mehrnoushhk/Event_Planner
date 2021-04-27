import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required


def db_connect(dbname):
    connection = sqlite3.connect(dbname)
    cursor = connection.cursor()
    return (connection, cursor)


def db_disconnect(connection):
    connection.commit()
    connection.close()


class User:
    """
    User data model to work with database
    """

    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def get_by_id(cls, _id):
        connection, cursor = db_connect("data.db")
        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (_id,)).fetchone()
        db_disconnect(connection)
        if result:
            user = cls(*result)
            return user
        return None

    @classmethod
    def get_by_name(cls, name):
        connection, cursor = db_connect("data.db")
        query = "SELECT * FROM users WHERE name=?"
        result = cursor.execute(query, (name,)).fetchone()
        db_disconnect(connection)
        if result:
            user = cls(*result)
            return user
        return None


def authenticate(username, password):
    connection, cursor = db_connect("data.db")
    query = "SELECT * FROM users WHERE username=?"
    result = cursor.execute(query, (username,)).fetchone()
    db_disconnect(connection)
    if result:
        user = User(*result)
    else:
        user = None
    return user


def identity(payload):
    _id = payload["identity"]
    query = "SELECT * FROM users WHERE id=?"
    result = cursor.execute(query, (_id,)).fetchone()
    db_disconnect(connection)
    if result:
        user = User(*result)
    else:
        user = None
    return user


class UserRegister(Resource):
    """
    Resource for API
    """

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("username", type=str, required=True)
        parser.add_argument("password", type=str, required=True)
        data = parser.parse_args()
        connection, cursor = db_connect("data.db")
        query = "INSERT INTO users VALUES(?,?,?)"
        try:
            cursor.execute(query, (None, data["username"], data["password"]))
            db_disconnect(connection)
            return {"message": "User registered successfuly"}, 201
        except sqlite3.IntegrityError as e:
            db_disconnect(connection)
            return {"message": str(e)}

    @jwt_required()
    def get(self):
        connection, cursor = db_connect("data.db")
        query = "SELECT * FROM users"
        results = cursor.execute(query).fetchall()
        return {"Users": results}
