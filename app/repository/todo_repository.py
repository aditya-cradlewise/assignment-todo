from app.db.connection import get_connection
from datetime import datetime, timedelta

class TodoRepository:
    #lists:

    # CREATE
    def create_list(self, title):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO todo_lists (title) VALUES (%s) RETURNING id;",
            (title,)
        )
        list_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return list_id

    # READ ALL
    def get_lists(self):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, title, is_archived FROM todo_lists;")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows

    # READ ONE
    def get_list(self, list_id):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "SELECT id, title, is_archived FROM todo_lists WHERE id = %s;",
            (list_id,)
        )
        row = cur.fetchone()
        cur.close()
        conn.close()
        return row

    # UPDATE
    def update_list(self, list_id, title):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "UPDATE todo_lists SET title=%s WHERE id=%s;",
            (title, list_id)
        )
        conn.commit()
        cur.close()
        conn.close()

    # DELETE
    def delete_list(self, list_id):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM todo_lists WHERE id=%s;", (list_id,))
        conn.commit()
        cur.close()
        conn.close()

    # ARCHIVE
    def archive_list(self, list_id):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "UPDATE todo_lists SET is_archived=TRUE WHERE id=%s;",
            (list_id,)
        )
        conn.commit()
        cur.close()
        conn.close()


    # Items:

    # CREATE ITEM
    # def create_item(self, list_id, title, due_date=None, expiry=None):
    #     conn = get_connection()
    #     cur = conn.cursor()
    #     cur.execute("""
    #         INSERT INTO todo_items (list_id, title, due_date, expiry)
    #         VALUES (%s, %s, %s, %s)
    #         RETURNING id;
    #     """, (list_id, title, due_date, expiry))
    #     item_id = cur.fetchone()[0]
    #     conn.commit()
    #     cur.close()
    #     conn.close()
    #     return item_id

    def create_item(self, list_id, title, due_date=None, expiry=None):
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO todo_items (list_id, title, due_date, expiry)
            VALUES (%s, %s, %s, %s)
            RETURNING id;
        """, (list_id, title, due_date, expiry))

        item_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()

        return item_id

    # GET ITEMS BY LIST
    def get_items_by_list(self, list_id):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT id, list_id, title, completed, due_date, expiry, archived
            FROM todo_items
            WHERE list_id = %s;
        """, (list_id,))
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows

    # GET ONE ITEM
    def get_item(self, item_id):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT id, list_id, title, completed, due_date, expiry, archived
            FROM todo_items
            WHERE id = %s;
        """, (item_id,))
        row = cur.fetchone()
        cur.close()
        conn.close()
        return row

    # MARK COMPLETE
    def mark_complete(self, item_id):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "UPDATE todo_items SET completed = TRUE WHERE id = %s;",
            (item_id,)
        )
        conn.commit()
        cur.close()
        conn.close()

    def archive_item(self, item_id):
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            UPDATE todo_items
            SET archived = TRUE
            WHERE id = %s
        """, (item_id,))

        conn.commit()
        cur.close()
        conn.close()

    # DELETE ITEM
    def delete_item(self, item_id):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "DELETE FROM todo_items WHERE id = %s;",
            (item_id,)
        )
        conn.commit()
        cur.close()
        conn.close()

    # ARCHIVE EXPIRED ITEMS
    def archive_expired_items(self):
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            UPDATE todo_items
            SET archived = TRUE
            WHERE expiry IS NOT NULL
              AND expiry < NOW()
              AND archived = FALSE;
        """)

        conn.commit()
        cur.close()
        conn.close()