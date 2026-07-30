from flask import Blueprint, render_template, redirect, url_for
from flask import request, jsonify

from src.services.session_service import SessionService
from src.services.cleaning_service import CleaningService

cleaning_bp = Blueprint("cleaning", __name__)


@cleaning_bp.route("/cleaning")
def cleaning():

    dataset = SessionService.get_current_dataset()

    if not dataset["dataset_path"]:
        return redirect(url_for("home.upload"))

    summary = CleaningService.dataset_summary(
        dataset["dataset_path"]
    )

    return render_template(
        "cleaning.html",
        dataset=dataset,
        summary=summary
    )


@cleaning_bp.route("/cleaning/remove-duplicates", methods=["POST"])
def remove_duplicates():

    dataset = SessionService.get_current_dataset()

    CleaningService.remove_duplicates_from_file(
        dataset["dataset_path"]
    )

    return jsonify({
        "success": True,
        "message": "Duplicate rows removed successfully."
    })


@cleaning_bp.route("/cleaning/drop-missing", methods=["POST"])
def drop_missing():

    dataset = SessionService.get_current_dataset()

    CleaningService.drop_missing_from_file(
        dataset["dataset_path"]
    )

    return jsonify({
        "success": True,
        "message": "Missing rows removed successfully."
    })


@cleaning_bp.route("/cleaning/fill-missing", methods=["POST"])
def fill_missing():

    data = request.get_json()

    value = data.get("value", 0)

    dataset = SessionService.get_current_dataset()

    CleaningService.fill_missing_from_file(
        dataset["dataset_path"],
        value
    )

    return jsonify({
        "success": True,
        "message": "Missing values filled successfully."
    })


@cleaning_bp.route("/cleaning/drop-columns", methods=["POST"])
def drop_columns():

    data = request.get_json()

    columns = data.get("columns", [])

    dataset = SessionService.get_current_dataset()

    CleaningService.drop_columns_from_file(
        dataset["dataset_path"],
        columns
    )

    return jsonify({
        "success": True,
        "message": "Columns removed successfully."
    })


@cleaning_bp.route("/cleaning/rename-column", methods=["POST"])
def rename_column():

    data = request.get_json()

    old_name = data["old_name"]
    new_name = data["new_name"]

    dataset = SessionService.get_current_dataset()

    CleaningService.rename_column_in_file(
        dataset["dataset_path"],
        old_name,
        new_name
    )

    return jsonify({
        "success": True,
        "message": "Column renamed successfully."
    })


@cleaning_bp.route("/cleaning/change-dtype", methods=["POST"])
def change_dtype():

    data = request.get_json()

    column = data["column"]
    dtype = data["dtype"]

    dataset = SessionService.get_current_dataset()

    CleaningService.change_dtype_in_file(
        dataset["dataset_path"],
        column,
        dtype
    )

    return jsonify({
        "success": True,
        "message": "Data type updated successfully."
    })