from flask import Flask, render_template, request, redirect, url_for
import sqlite3


app = Flask(__name__)

con = sqlite3.connect("todo.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS tasks(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")
# カラム追加用
# cur.execute("ALTER TABLE tasks ADD COLUMN done INTEGER DEFAULT 0")
con.commit()
con.close()


@app.route("/", methods=["GET", "POST"])
def todo_list():
    if request.method == "POST":
        name = request.form.get("name")

        con = sqlite3.connect("todo.db")
        cur = con.cursor()
        cur.execute("INSERT INTO tasks(name) VALUES(?)", (name,))
        con.commit()
        con.close()

        return redirect(url_for("todo_list"))
    else:
        con = sqlite3.connect("todo.db")
        cur = con.cursor()
        cur.execute("SELECT id, name, done FROM tasks")
        tasks = cur.fetchall()
        con.close()

        return render_template("index.html", tasks=tasks)


@app.route("/delete/<int:id>", methods=["POST"])
def delete_task(id):
    con = sqlite3.connect("todo.db")
    cur = con.cursor()
    cur.execute("DELETE FROM tasks WHERE id = ?", (id,))
    con.commit()
    con.close()

    return redirect(url_for("todo_list"))


@app.route("/done/<int:id>", methods=["POST"])
def tasks_done(id):
    con = sqlite3.connect("todo.db")
    cur = con.cursor()
    cur.execute("SELECT done FROM tasks WHERE id = ?", (id,))
    done = cur.fetchone()[0]
    new_done = 1 if done == 0 else 0
    cur.execute("UPDATE tasks SET done = ? WHERE id = ?", (new_done, id))
    con.commit()
    con.close()

    return redirect(url_for("todo_list"))
    


if __name__ == "__main__":
    app.run(debug=True)