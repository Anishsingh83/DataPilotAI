
// Initialize


document.addEventListener("DOMContentLoaded", () => {

    loadNumericalSummary();

    loadDatasetPreview();

    loadHeatmap();

});


// Numerical Summary


async function loadNumericalSummary() {

    try {

        const response = await fetch(
            "/eda/numerical-summary"
        );

        if (!response.ok) {

            throw new Error(
                "Unable to load numerical summary."
            );

        }

        const data = await response.json();

        const tbody = document.querySelector(
            "#numericalSummary tbody"
        );

        tbody.innerHTML = "";

        data.forEach(column => {

            tbody.innerHTML += `

                <tr>

                    <td>${column.column}</td>

                    <td>${column.mean}</td>

                    <td>${column.median}</td>

                    <td>${column.std}</td>

                </tr>

            `;

        });

    }

    catch (error) {

        console.error(error);

        showError(
            "Unable to load numerical summary."
        );

    }

}


// Dataset Preview


async function loadDatasetPreview() {

    try {

        const response = await fetch(
            "/eda/dataset-preview"
        );

        if (!response.ok) {

            throw new Error(
                "Unable to load dataset preview."
            );

        }

        const html = await response.text();

        document.getElementById(
            "datasetPreview"
        ).innerHTML = html;

    }

    catch (error) {

        console.error(error);

        showError(
            "Unable to load dataset preview."
        );

    }

}

// Generate Histogram

const histogramBtn = document.getElementById(
    "generateHistogramBtn"
);

histogramBtn?.addEventListener("click", async () => {

    const column = document.getElementById(
        "histogramColumn"
    ).value;

    if (!column) {

        showWarning(
            "Please select a numerical column."
        );

        return;

    }

    histogramBtn.disabled = true;

    histogramBtn.innerHTML = `

        <i class="fa-solid fa-spinner fa-spin"></i>

        Generating...

    `;

    try {

        const response = await fetch(

            "/eda/generate-histogram",

            {

                method: "POST",

                headers: {

                    "Content-Type": "application/json"

                },

                body: JSON.stringify({

                    column

                })

            }

        );

        if (!response.ok) {

            throw new Error(
                "Failed to generate histogram."
            );

        }

        const result = await response.json();

        if (!result.success) {

            throw new Error(
                result.message
            );

        }

        const graph = JSON.parse(
            result.graph
        );

        graph.layout = {

            ...graph.layout,

            autosize: true,

            height: 420,

            margin: {

                l: 50,

                r: 20,

                t: 50,

                b: 50

            },

            paper_bgcolor: "#FFFFFF",

            plot_bgcolor: "#FFFFFF"

        };

        Plotly.react(

            "histogramChart",

            graph.data,

            graph.layout,

            {

                responsive: true,

                displaylogo: false,

                displayModeBar: true

            }

        );

        showSuccess(
            "Histogram generated successfully."
        );

    }

    catch (error) {

        console.error(error);

        showError(

            error.message ||

            "Unable to generate histogram."

        );

    }

    finally {

        histogramBtn.disabled = false;

        histogramBtn.innerHTML = `

            <i class="fa-solid fa-chart-column"></i>

            Generate Histogram

        `;

    }

});

// Load Correlation Heatmap

async function loadHeatmap() {

    try {

        const response = await fetch(
            "/eda/correlation-heatmap"
        );

        if (!response.ok) {

            throw new Error(
                "Unable to load heatmap."
            );

        }

        const result = await response.json();

        if (!result.success) {

            throw new Error(
                result.message
            );

        }

        const graph = JSON.parse(
            result.graph
        );

        graph.layout = {

            ...graph.layout,

            autosize: true,

            height: 500,

            margin: {

                l: 50,

                r: 20,

                t: 50,

                b: 50

            },

            paper_bgcolor: "#FFFFFF",

            plot_bgcolor: "#FFFFFF"

        };

        Plotly.react(

            "heatmap",

            graph.data,

            graph.layout,

            {

                responsive: true,

                displaylogo: false,

                displayModeBar: true

            }

        );

    }

    catch (error) {

        console.error(error);

        showError(
            "Unable to load heatmap."
        );

    }

}

// Download Report

const downloadBtn = document.getElementById(
    "downloadReportBtn"
);

downloadBtn?.addEventListener("click", () => {

    showInfo(
        "Preparing report..."
    );

    window.location.href =
        "/eda/download-report";

});


// Handle Window Resize

window.addEventListener("resize", () => {

    const histogram = document.getElementById(
        "histogramChart"
    );

    const heatmap = document.getElementById(
        "heatmap"
    );

    if (histogram) {

        Plotly.Plots.resize(
            histogram
        );

    }

    if (heatmap) {

        Plotly.Plots.resize(
            heatmap
        );

    }

});