const fillMissingBtn = document.getElementById("fillMissingBtn");
const removeDuplicateBtn = document.getElementById("removeDuplicateBtn");
const dropColumnsBtn = document.getElementById("dropColumnsBtn");
const renameColumnBtn = document.getElementById("renameColumnBtn");
const changeTypeBtn = document.getElementById("changeTypeBtn");
const downloadDatasetBtn = document.getElementById("downloadDatasetBtn");


            // Helpers


function showLoading(button, text = "Processing...") {

    button.dataset.originalText = button.innerHTML;

    button.disabled = true;

    button.innerHTML = `
        <i class="fa-solid fa-spinner fa-spin"></i>
        ${text}
    `;
}

function hideLoading(button) {

    button.disabled = false;

    button.innerHTML = button.dataset.originalText;
}

async function sendRequest(url, payload, button) {

    showLoading(button);

    try {

        const response = await fetch(url, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(payload)
        });

        const result = await response.json();

        if (result.success) {

            showSuccess(result.message);

            setTimeout(() => {

                location.reload();

            }, 500);

        }
        
        else {

            showError(result.message || "Operation failed.");

        }

    }

    catch (error) {

        console.error(error);

        showError("Server error. Please try again.");

    }

    finally {

        hideLoading(button);

    }

}


        // Fill Missing Values


fillMissingBtn?.addEventListener("click", () => {

    const strategy = document.getElementById("fillStrategy").value;

    sendRequest(
        "/cleaning/fill-missing",
        {
            strategy
        },
        fillMissingBtn
    );

});


        // Remove Duplicates


removeDuplicateBtn?.addEventListener("click", () => {

    if (!confirm("Remove all duplicate rows?")) return;

    sendRequest(
        "/cleaning/remove-duplicates",
        {},
        removeDuplicateBtn
    );

});


            // Drop Columns


dropColumnsBtn?.addEventListener("click", () => {

    const select = document.getElementById("dropColumns");

    const columns = [...select.selectedOptions].map(col => col.value);

    if (columns.length === 0) {

        showWarning("Please select at least one column.");

        return;

    }

    sendRequest(
        "/cleaning/drop-columns",
        {
            columns
        },
        dropColumnsBtn
    );

});


            // Rename Column


renameColumnBtn?.addEventListener("click", () => {

    const oldColumn = document.getElementById("oldColumn").value.trim();

    const newColumn = document.getElementById("newColumn").value.trim();

    if (!oldColumn || !newColumn) {

        showWarning("Please enter both column names.");

        return;

    }

    sendRequest(
        "/cleaning/rename-column",
        {
            old_column: oldColumn,
            new_column: newColumn
        },
        renameColumnBtn
    );

});


        // Change Data Type


changeTypeBtn?.addEventListener("click", () => {

    const column = document.getElementById("dtypeColumn").value;

    const dtype = document.getElementById("dtype").value;

    sendRequest(
        "/cleaning/change-dtype",
        {
            column,
            dtype
        },
        changeTypeBtn
    );

});


        // Download Dataset


downloadDatasetBtn?.addEventListener("click", () => {

    showLoading(downloadDatasetBtn, "Preparing Download...");

    setTimeout(() => {

        window.location.href = "/cleaning/download";

        hideLoading(downloadDatasetBtn);

    }, 300);

});




