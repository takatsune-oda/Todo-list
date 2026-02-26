from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
import models


app = Flask(__name__)
app.secret_key = "secret_key"


@app.route("/", methods=["GET", "POST"])
def todo_list():
    if request.method == "POST":
        name = request.form.get("name", "").strip()

        if not name:
            flash("タスクを入力してください", "error")
            return redirect(url_for("todo_list"))
        
        models.add_task(name)
        flash("タスクが追加されました", "success")
        return redirect(url_for("todo_list"))
    
    tasks = models.get_task()
    return render_template("index.html", tasks=tasks)


@app.route("/delete/<int:id>", methods=["POST"])
def delete_task(id):
    models.delete_task(id)

    return redirect(url_for("todo_list"))


@app.route("/done/<int:id>", methods=["POST"])
def tasks_done(id):
    models.toggle_done(id)

    return redirect(url_for("todo_list"))
    

if __name__ == "__main__":
    app.run(debug=True)
