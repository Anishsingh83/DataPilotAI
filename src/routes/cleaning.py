from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    request,
    jsonify,
    send_file
)

from src.services.session_service import SessionService
from src.services.cleaning_service import CleaningService


cleaning_bp = Blueprint("cleaning", __name__)



# Cleaning Dashboard


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



# Remove Duplicates


@cleaning_bp.route("/cleaning/remove-duplicates", methods=["POST"])
def remove_duplicates():

    try:

        dataset = SessionService.get_current_dataset()

        CleaningService.remove_duplicates_from_file(
            dataset["dataset_path"]
        )

        return jsonify({
            "success": True,
            "message": "Duplicate rows removed successfully."
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "message": str(e)
        }), 400



# Drop Missing Rows


@cleaning_bp.route("/cleaning/drop-missing", methods=["POST"])
def drop_missing():

    try:

        dataset = SessionService.get_current_dataset()

        CleaningService.drop_missing_from_file(
            dataset["dataset_path"]
        )

        return jsonify({
            "success": True,
            "message": "Missing rows removed successfully."
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "message": str(e)
        }), 400



# Fill Missing Values


@cleaning_bp.route("/cleaning/fill-missing", methods=["POST"])
def fill_missing():

    try:

        data = request.get_json()

        strategy = data["strategy"]

        dataset = SessionService.get_current_dataset()

        CleaningService.fill_missing_from_file(
            dataset["dataset_path"],
            strategy
        )

        return jsonify({
            "success": True,
            "message": "Missing values handled successfully."
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "message": str(e)
        }), 400



# Drop Columns


@cleaning_bp.route("/cleaning/drop-columns", methods=["POST"])
def drop_columns():

    try:

        data = request.get_json()

        columns = data.get("columns", [])

        dataset = SessionService.get_current_dataset()

        CleaningService.drop_columns_from_file(
            dataset["dataset_path"],
            columns
        )

        return jsonify({
            "success": True,
            "message": "Selected columns removed successfully."
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "message": str(e)
        }), 400



# Rename Column


@cleaning_bp.route("/cleaning/rename-column", methods=["POST"])
def rename_column():

    try:

        data = request.get_json()

        old_name = data["old_column"]
        new_name = data["new_column"]

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

    except Exception as e:

        return jsonify({
            "success": False,
            "message": str(e)
        }), 400



# Change Data Type


@cleaning_bp.route("/cleaning/change-dtype", methods=["POST"])
def change_dtype():

    try:

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

    except Exception as e:

        return jsonify({
            "success": False,
            "message": str(e)
        }), 400



# Download Dataset


@cleaning_bp.route("/cleaning/download")
def download_dataset():

    dataset = SessionService.get_current_dataset()

    return send_file(
        dataset["dataset_path"],
        as_attachment=True
    )