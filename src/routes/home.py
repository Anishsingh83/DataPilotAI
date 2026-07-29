from flask import Blueprint, render_template, request, current_app
from werkzeug.utils import secure_filename
import os

home_bp = Blueprint("home", __name__)

@home_bp.route("/")
def home():
    return render_template("index.html")

@home_bp.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@home_bp.route("/upload", methods=["GET", "POST"])
def upload():

    if request.method == "POST":

        file = request.files.get("dataset")

        if file and file.filename != "":

            filename = secure_filename(file.filename)

            upload_path = os.path.join(
                current_app.config["UPLOAD_FOLDER"],
                filename
            )

            file.save(upload_path)

            return render_template(
                "upload.html",
                success=f"{filename} uploaded successfully!"
            )

    return render_template("upload.html")
