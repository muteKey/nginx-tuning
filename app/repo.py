from app.db import get_db

class Repository:
    def fetch_users(self):
        cursor = get_db().cursor()
        cursor.execute("SELECT * FROM user")
        rows = cursor.fetchall()
        results = []

        for row in rows:
            result = self.__dict_from_row(row)
            results.append(result)

        return results if len(results) else None

    def __dict_from_row(self, row):
        return dict(zip(row.keys(), row))
