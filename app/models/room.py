from app.db import get_connection


def get_all_rooms():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(
        "SELECT id, name, building, room_type, capacity FROM rooms ORDER BY name"
    )
    rooms = cursor.fetchall()
    cursor.close()
    conn.close()
    return rooms