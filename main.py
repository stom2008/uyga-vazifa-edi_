from flask import Flask, render_template,\
    redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///datebase.db"
db = SQLAlchemy(app)

class Tasks(db.Model):
    id =db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

@app.route("/")
def index():
    tasks = Tasks.query.all()
    return render_template("index.html", tasks=tasks)

@app.route("/task_create", methods=["POST"])
def task_create():
    task_name = request.form.get("task_name")
    task = Tasks(
        title=task_name
    )
    db.session.add(task)
    db.session.commit()

    return redirect(url_for("index"))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

