from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    jsonify,
    request
)

from src.services.session_service import SessionService
from src.services.eda_service import EDAService


eda_bp = Blueprint("eda", __name__)


# EDA Dashboard

@eda_bp.route("/eda")
def eda():

    dataset = SessionService.get_current_dataset()

    if not dataset["dataset_path"]:

        return redirect(
            url_for("home.upload")
        )

    summary = EDAService.dataset_summary(
        dataset["dataset_path"]
    )

    return render_template(
        "eda.html",
        dataset=dataset,
        summary=summary
    )
    
# Numerical Summary

@eda_bp.route("/eda/numerical-summary")
def numerical_summary():

    dataset = SessionService.get_current_dataset()

    summary = EDAService.numerical_summary(

        dataset["dataset_path"]

    )

    return jsonify(summary)


# Dataset Preview

@eda_bp.route("/eda/dataset-preview")
def dataset_preview():

    dataset = SessionService.get_current_dataset()

    preview = EDAService.dataset_preview(

        dataset["dataset_path"]

    )

    return preview.to_html(

        classes="summary-table",

        index=False

    )
    
# Generate Histogram

@eda_bp.route(

    "/eda/generate-histogram",

    methods=["POST"]

)
def generate_histogram():

    try:

        data = request.get_json()

        column = data["column"]

        dataset = SessionService.get_current_dataset()

        graph = EDAService.generate_histogram(

            dataset["dataset_path"],

            column
            

        )
        print(graph[:500])

        return jsonify({

            "success": True,

            "graph": graph

        })

    except Exception as e:

        return jsonify({

            "success": False,

            "message": str(e)

        }), 400
        
        
    # Correlation Heatmap

@eda_bp.route("/eda/correlation-heatmap")
def correlation_heatmap():

    try:

        dataset = SessionService.get_current_dataset()

        graph = EDAService.generate_heatmap(

            dataset["dataset_path"]

        )

        return jsonify({

            "success": True,

            "graph": graph

        })

    except Exception as e:

        return jsonify({

            "success": False,

            "message": str(e)

        }), 400    
        
        
# Download Report

@eda_bp.route("/eda/download-report")
def download_report():

    return jsonify({

        "success": False,

        "message": "EDA Report will be available soon."

    })    