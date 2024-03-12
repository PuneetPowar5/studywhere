from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Users(db.Model):
    userId = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    userPhoneNum = db.Column(db.Text, nullable=True)
    userEmail = db.Column(db.Text, nullable=True)
    userName = db.Column(db.Text)
    userPassword = db.Column(db.Text)
    userYearOfStudy = db.Column(db.Integer, nullable=True)

    def __init__(self, PhoneNum, Email, UserName, Password, YearOfStudy):
        self.userPhoneNum = PhoneNum
        self.userEmail = Email
        self.userName = UserName
        self.userPassword = Password
        self.userYearOfStudy = YearOfStudy

    def encode(self):
        return self.__dict__

    def __repr__(self):
        return f"Users, {self.UserName}, {self.ID}"


class Rooms(db.Model):
    roomId = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    roomNumber = db.Column(db.Text)
    roomBuilding = db.Column(db.Text)
    roomFloor = db.Column(db.Text, nullable=True)
    roomCapacity = db.Column(db.Integer, nullable=True)
    roomOccupancy = db.Column(db.Integer, nullable=True)
    roomImage = db.Column(db.String(80), nullable=True)

    def __init__(self, number, building, floor, image, capacity, occupancy):
        self.roomNumber = number
        self.roomBuilding = building
        self.roomFloor = floor
        self.roomImage = image
        self.roomCapacity = capacity
        self.roomOccupancy = occupancy

    def encode(self):
        return self.__dict__


class Reservations(db.Model):
    reservationId = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    userId = db.Column(db.Integer, db.ForeignKey('users.userId'))
    roomId = db.Column(db.Integer, db.ForeignKey('rooms.roomId'))
    beginTime = db.Column(db.DateTime)
    endTime = db.Column(db.DateTime)
    day = db.Column(db.Integer)
    isEvent = db.Column(db.Boolean)

    def __init__(self, userId, roomId, beginTime, endTime, isEvent):
        self.roomId = roomId
        self.userId = userId
        self.beginTime = beginTime
        self.endTime = endTime
        self.isEvent = isEvent

    def encode(self):
        return self.__dict__


class Occupied(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    room_id = db.Column(db.Integer, db.ForeignKey('rooms.roomId'))
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    day = db.Column(db.Integer)

    def __init__(self, room_id, start_time, end_time, day):
        self.room_id = room_id
        self.start_time = start_time
        self.end_time = end_time
        self.day = day

    def encode(self):
        return self.__dict__
