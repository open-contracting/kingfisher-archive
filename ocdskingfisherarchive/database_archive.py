import sqlite3


class DataBaseArchive:
    def __init__(self, database):
        self.conn = sqlite3.connect(database)
        self.cursor = self.conn.cursor()

        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='collections'")
        if not self.cursor.fetchone():
            self.cursor.execute(
                "CREATE TABLE collections (collection_id INTEGER PRIMARY KEY NOT NULL, state TEXT NOT NULL)"
            )
            self.conn.commit()

    def get_state_of_collection_id(self, collection_id):
        state = 'UNKNOWN'
        self.cursor.execute(
            "SELECT state FROM collections WHERE collection_id=:collection_id",
            {"collection_id": collection_id}
        )
        r = self.cursor.fetchone()
        if r:
            state = r[0]
        return state

    def set_state_of_collection_id(self, collection_id, state):
        self.cursor.execute(
            "REPLACE INTO collections (collection_id, state) VALUES (:collection_id, :state)",
            {"collection_id": collection_id, "state": state}
        )
        self.conn.commit()
