import xmlrpc.client

db = "vauxoo"
user = "admin"
password = "admin"
host = "localhost"
port = 8069

root = "http://%s:%d/xmlrpc/" % (host, port)


def create_session(args):
    session_id = sock.execute(db, uid, password, "session", "create", args)
    print(f"Session '{args['name']}' created with id: {session_id}\n")


def read_sessions(filter, fields):
    sessions = sock.execute(db, uid, password, "session", "search_read", filter, fields)
    print("Session List:\n", sessions)


if __name__ == "__main__":
    uid = xmlrpc.client.ServerProxy(root + "common").login(db, user, password)
    print("Logged in as %s (uid: %d)\n" % (user, uid))

    args = {
        "name": "Test RPC",
        "duration": 240.0,
        "number_of_seats": 15,
        "instructor_id": 1,
        "course_id": 1,
        "attendee_ids": [8, 9, 10],
    }

    fields = ["name", "instructor_id", "course_id", "attendees_count"]

    sock = xmlrpc.client.ServerProxy(root + "object")
    create_session(args)
    read_sessions([], fields)
