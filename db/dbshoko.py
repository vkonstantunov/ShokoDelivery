import sqlite3


conn = sqlite3.connect(f"db/database.db", check_same_thread=False)
cursor = conn.cursor()



def db_table_val(user_id: int, user_name: str):
	cursor.execute('INSERT INTO ShokoBot (user_id, user_name) VALUES (?, ?)', (user_id, user_name))
	conn.commit()



