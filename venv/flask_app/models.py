from db import get_db_connection


# タスクの追加
def add_task(name):
    con = get_db_connection()
    cur = con.cursor()
    cur.execute(
        "INSERT INTO tasks(name) VALUES(?)", (name,)
    )
    con.commit()
    con.close()


# タスクの取得
def get_task():
    con = get_db_connection()
    cur = con.cursor()
    cur.execute(
        "SELECT id, name, done FROM tasks"
    )
    tasks = cur.fetchall()
    con.commit()
    con.close()

    return tasks


# タスクの削除
def delete_task(id):
    con = get_db_connection()
    cur = con.cursor()
    cur.execute(
        "DELETE FROM tasks WHERE id = ?", (id,)
    )
    con.commit()
    con.close()


# 完了タスクのトグル処理
def toggle_done(id):
    con = get_db_connection()
    cur = con.cursor()
    cur.execute(
        "SELECT done FROM tasks WHERE id = ?", (id,)
    )
    done = cur.fetchone()[0]
    new_done = 1 if done == 0 else 0
    cur.execute(
        "UPDATE tasks SET done = ? WHERE id = ?", (new_done, id)
    )
    con.commit()
    con.close()
