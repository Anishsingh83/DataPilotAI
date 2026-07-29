from flask import Blueprint, render_template, request

from src.services.upload_service import UploadService
from src.services.dataset_service import DatasetService

home_bp = Blueprint("home", __name__)


# Home Page
@home_bp.route("/")
def home():
    return render_template("index.html")


# Dashboard Page
@home_bp.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# Upload Dataset
@home_bp.route("/upload", methods=["GET", "POST"])
def upload():

    preview = None
    summary = None
    success = None

    if request.method == "POST":

        file = request.files.get("dataset")

        if file and file.filename:

            filename, upload_path = UploadService.save_file(file)

            df = DatasetService.read_dataset(upload_path)

            preview = DatasetService.preview(df)

            summary = DatasetService.summary(df)

            success = f"{filename} uploaded successfully!"

    return render_template(
        "upload.html",
        success=success,
        preview=preview,
        summary=summary
    )