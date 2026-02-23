from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import models


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def todo_list():
    if request.method == "POST":
        name = request.form.get("name")
        models.add_task(name)

        return redirect(url_for("todo_list"))
    else:
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