from flask import Blueprint, render_template, session, redirect, url_for

from src.services.explorer_service import ExplorerService

explorer_bp = Blueprint("explorer", __name__)


@explorer_bp.route("/explorer")
def explorer():

    dataset_path = session.get("dataset_path")
    dataset_name = session.get("dataset_name")

    if not dataset_path:
        return redirect(url_for("home.upload"))

    df = ExplorerService.load_dataset(dataset_path)

    dataset_info = ExplorerService.get_dataset_info(df)

    table = ExplorerService.get_page(df)

    return render_template(
        "explorer.html",
        dataset_name=dataset_name,
        dataset_info=dataset_info,
        table=table
    )