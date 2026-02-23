import sqlite3


DB_NAME = "todo.db"

# DBの作成
def init_db() -> None:
    with sqlite3.connect(DB_NAME) as con:
        cur = con.cursor()
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks(
            id INTEGER PRIMARY KEY AUTOCREMENT,
            name TEXT)
            """
        )
        con.commit()
        con.close()


# DBへの接続
def get_db_connection():
    con = sqlite3.connect(DB_NAME)
    con.row_factory = sqlite3.Row
    return con


if __name__ == "__main__":
    app.run(debug=True)
