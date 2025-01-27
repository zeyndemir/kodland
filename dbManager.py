import pymysql

class DBManager:
    def __init__(self, dbname, user, password, host, port):
        try:
            self.conn = pymysql.connect(
                host=host,
                user=user,
                password=password,
                database=dbname,
                port=port
            )
            self.cursor = self.conn.cursor()
            print("Database connected.")
        except Exception as e:
            print(f"Error , can't connect database {e}")
            raise

    def cr_table(self):

        try:
            query = """
            CREATE TABLE IF NOT EXISTS quiz_results (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(100),
                color VARCHAR(10),
                animal VARCHAR(10),
                hobbies text
            );
            """
            self.cursor.execute(query)
            self.conn.commit()

        except Exception as e:
            print(f"Error  {e}")
            raise

    def insert(self, username, color, animal, hobbies):

        try:
            query = "INSERT INTO quiz_results (username, color, animal, hobbies) VALUES (%s, %s, %s, %s)"
            values = (username, color, animal, hobbies)
            self.cursor.execute(query, values)
            self.conn.commit()

        except Exception as e:
            print(f"Error  {e}")
            raise

    def __del__(self):

        try:
            self.cursor.close()
            self.conn.close()

        except Exception as e:
            print(f"Database couldn't closed {e}")
