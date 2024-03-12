from datetime import datetime
from flask import Flask, request, jsonify
from models import db, Users, Rooms, Reservations, Occupied
from sqlalchemy import func
import json
import yaml
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACef499b454b3b86e4c86292125acd9f74"
# Your Auth Token from twilio.com/console
auth_token = "90dd7a6be00d5d41def211caf5fca549"

client = Client(account_sid, auth_token)

db_info = yaml.safe_load(open('db.yaml'))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://{dbuser}:{dbpass}@{server}/{dbname}".format(
    dbuser=db_info['user'],
    dbpass=db_info['password'],
    server=db_info['server'],
    dbname=db_info['name']
)

db.init_app(app)

@app.route('/api/notifyUsersEvent', methods=['GET'])
def notify_users_event():
    ID = request.args.get('eventId')
    reservations = Reservations.query.filter_by(reservationId=ID).filter_by(isEvent=1).all()

    matching_room = Rooms.query.filter_by(roomId=reservations[0].roomId).all()
    room_code = str(matching_room[0].roomBuilding) + str(matching_room[0].roomNumber)

    users = Users.query
    for user in users:
        client.messages.create(to=user.userPhoneNum, from_="+15075011716",
                               body="An event will be happening today in " + room_code + " between " +
                                    "15:00" + " and " + "17:00" + "! \nPlease visit our website for further details!")

    return jsonify({'message': "Notifications for event {ID} were sent successfully".format(ID=ID)}), 200


@app.route('/api/notifyUsersReservation', methods=['GET'])
def notify_users_reservation():
    reservationID = request.args.get('reservationId')
    userID = request.args.get('userId')
    reservations = Reservations.query.filter_by(reservationId=reservationID).filter_by(userId=userID).all()

    matching_room = Rooms.query.filter_by(roomId=reservations[0].roomId).all()
    room_code = str(matching_room[0].roomBuilding) + str(matching_room[0].roomNumber)

    users = Users.query.filter_by(userId=userID).all()
    for user in users:
        client.messages.create(to=user.userPhoneNum, from_="+15075011716",
                               body="Your reservation for " + room_code + " between " +
                                    "15:00" + " and " + "17:00" + " is coming up! \nPlease visit our website for further details!")

    return jsonify({'message': "A Notification for reservation {resID} was sent successfully to user {useID}!".format(resID=reservationID, useID=userID)}), 20


@app.route('/api/notifyUsers', methods=['GET'])
def notify_users():
    ID = request.args.get('eventId')
    reservations = Reservations.query.filter_by(reservationId=ID).filter_by(isEvent=1).all()

    matching_room = Rooms.query.filter_by(roomId=reservations[0].roomId).all()
    room_code = str(matching_room[0].roomBuilding) + str(matching_room[0].roomNumber)

    users = Users.query
    for user in users:
        client.messages.create(to=user.userPhoneNum, from_="+15075011716",
                               body="An event will be happening today in " + room_code + " between " +
                                    "15:00" + " and " + "17:00" + "! \nPlease visit our website for further details!")

    return jsonify({'message': "Notifications for event with id {ID} were sent successfully".format(ID=ID)}), 200


@app.route('/api/addUser', methods=['POST'])
def add_user():
    data = request.get_json()
    PhoneNum = data.get('phone')
    Email = data.get('email')
    UserName = data.get('username')
    Password = data.get('password')
    YearOfStudy = data.get('yos')

    new_user = Users(PhoneNum, Email, UserName, Password, YearOfStudy)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User added successfully'}), 201


@app.route('/api/getUser', methods=['GET'])
def get_user():
    ID = request.args.get('ID')
    PhoneNum = request.args.get('phone')
    Email = request.args.get("email")
    UserName = request.args.get('username')
    YearOfStudy = request.args.get('yos')

    users = Users.query
    if ID:
        users = users.filter_by(userId=ID)
    if PhoneNum:
        users = users.filter_by(userPhoneNum=PhoneNum)
    if Email:
        users = users.filter_by(userEmail=Email)
    if UserName:
        users = users.filter_by(userName=UserName)
    if YearOfStudy:
        users = users.filter_by(userYearOfStudy=YearOfStudy)

    temp = []

    for v in users:
        value = v.encode()
        value.pop("_sa_instance_state", None)
        temp.append(value)

    return jsonify(temp)


@app.route('/api/addRoom', methods=['POST'])
def add_room():
    data = request.get_json()
    RoomNumber = data.get('number')
    RoomBuilding = data.get('building')
    RoomFloor = data.get('floor')
    RoomCapacity = data.get('capacity')
    RoomOccupancy = data.get('occupancy')

    new_room = Rooms(RoomNumber, RoomBuilding, RoomFloor, RoomCapacity, RoomOccupancy, None)
    db.session.add(new_room)
    db.session.commit()
    return jsonify({'message': 'Room added successfully'}), 201


@app.route('/api/getRoom', methods=['GET'])
def get_room():
    ID = request.args.get('ID')
    number = request.args.get('number')
    building = request.args.get('building')
    floor = request.args.get('floor')
    capacity = request.args.get('capacity')
    occupancy = request.args.get('occupancy')

    rooms = Rooms.query
    if ID:
        rooms = rooms.filter_by(roomID=ID)
    if number:
        rooms = rooms.filter_by(roomNumber=number)
    if building:
        rooms = rooms.filter_by(roomBuilding=building)
    if floor:
        rooms = rooms.filter_by(roomFloor=floor)
    if capacity:
        rooms = rooms.filter_by(roomCapacity=capacity)
    if occupancy:
        rooms = rooms.filter_by(roomOccupancy=occupancy)

    temp = []

    for v in rooms:
        value = v.encode()
        value.pop("_sa_instance_state", None)
        temp.append(value)

    return jsonify(temp)


@app.route('/api/addReservation', methods=['POST'])
def add_reservation():
    data = request.get_json()
    userID = data.get('UserID')
    roomID = data.get('RoomID')
    beginTime = data.get('BeginTime')
    endTime = data.get('EndTime')
    type = data.get('Type')

    new_reservation = Rooms(userID, roomID, beginTime, endTime, type)
    db.session.add(new_reservation)
    db.session.commit()
    return jsonify({'message': 'Room added successfully'}), 201


@app.route('/api/getReservation', methods=['GET'])
def get_reservation():
    ID = request.args.get('ID')
    userID = request.args.get('UserID')
    roomID = request.args.get('RoomID')
    beginTime = request.args.get('BeginTime')
    endTime = request.args.get('EndTime')
    type = request.args.get('Type')

    reservations = Reservations.query
    if ID:
        reservations = reservations.filter_by(reservationId=ID)
    if userID:
        reservations = reservations.filter_by(userId=userID)
    if roomID:
        reservations = reservations.filter_by(roomId=roomID)
    if beginTime:
        reservations = reservations.filter_by(beginTime=beginTime)
    if endTime:
        reservations = reservations.filter_by(endTime=endTime)
    if type:
        reservations = reservations.filter_by(isEvent=type)

    temp = []

    for v in reservations:
        value = v.encode()
        value.pop("_sa_instance_state", None)
        temp.append(value)

    return jsonify(temp)

@app.route('/api/fillClassesFromLocalCrawler', methods=['GET'])
def fill_classes_from_local_crawler():
    json_file = open('out.json', 'r')
    data = json.load(json_file)

    for key, value in data.items():
        # Extract the room ID, day, start time, and end time from the JSON data
        building_name = value['BuildingName']
        room_number = value['RoomNumber']
        class_code = value['classCode']
        day = value['Day']

        room = Rooms.query.filter_by(roomNumber=room_number, roomBuilding=building_name).first()

        if not room:
            # If the room doesn't exist, create it
            room = Rooms(number=room_number, building=building_name, floor=None, image=None, capacity=None, occupancy=None)
            db.session.add(room)

        start_time = datetime.strptime(f"{day} {value['Time'][0]}", "%w %H.%M")
        end_time = datetime.strptime(f"{day} {value['Time'][1]}", "%w %H.%M")

        room = Rooms.query.filter_by(roomNumber=room_number, roomBuilding=building_name).first()
        occupied = Occupied(room_id=room.roomId, start_time=start_time, end_time=end_time, day=day)
        db.session.add(occupied)

    db.session.commit()
    response = jsonify({'message': 'Success'})
    return response, 200


@app.route('/api/getRoomAvailability', methods=['GET'])
def getRoomAvailability():
    """
    Given a date and a building code e.g. 'DH', return all the rooms with a list their occupied times
    """

    building_code = request.args.get('building')
    date = request.args.get('date')
    date_obj = datetime.strptime(date, '%Y-%m-%d')
    day_of_week = date_obj.strftime('%w')
    rooms = Rooms.query.filter_by(roomBuilding=building_code).all()
    busy_periods = {}

    for room in rooms:
        if room.roomId not in busy_periods:
            busy_periods[room.roomId] = [str(x.start_time.time()) for x in Occupied.query.filter_by(room_id=room.roomId, day=day_of_week).all()]
            busy_periods[room.roomId] += [str(x.beginTime.time()) for x in Reservations.query.filter_by(roomId=room.roomId).filter(func.date(Reservations.beginTime)==date_obj).all()]
        else:
            busy_periods[room.roomId] += [str(x.start_time.time()) for x in Occupied.query.filter_by(room_id=room.roomId, day=day_of_week)]
            busy_periods[room.roomId] += [str(x.beginTime.time()) for x in Reservations.query.filter_by(roomId=room.roomId).filter(func.date(Reservations.beginTime)==date_obj).all()]

    return jsonify(busy_periods), 200



if __name__ == '__main__':
    app.run()

