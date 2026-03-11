def list_entity(row):
    return {
        "id": row[0],
        "title": row[1],
        "is_archived": row[2],
    }

def item_entity(row):
    return {
        "id": row[0],
        "list_id": row[1],
        "title": row[2],
        "completed": row[3],
        "due_date": row[4],
        "expiry": row[5],
        "archived": row[6],
    }
