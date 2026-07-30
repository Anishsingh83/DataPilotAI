const fillMissingBtn = document.getElementById("fillMissingBtn");
const removeDuplicateBtn = document.getElementById("removeDuplicateBtn");
const dropColumnsBtn = document.getElementById("dropColumnsBtn");
const renameColumnBtn = document.getElementById("renameColumnBtn");
const changeTypeBtn = document.getElementById("changeTypeBtn");
const downloadDatasetBtn = document.getElementById("downloadDatasetBtn");

/* ===========================
   Helpers
=========================== */

function showLoading(button, text = "Processing...") {

    button.dataset.original = button.innerHTML;

    button.disabled = true;

    button.innerHTML = `
        <i class="fa-solid fa-spinner fa-spin"></i>
        ${text}
    `;
}

function resetButton(button) {

    button.disabled = false;

    button.innerHTML = button.dataset.original;
}

async function postRequest(url, payload, button) {

    showLoading(button);

    try {

        const response = await fetch(url, {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(payload)

        });

        const data = await response.json();

        alert(data.message);

        if (data.success) {

            location.reload();

        }

    }

    catch (error) {

        console.error(error);

        alert("Something went wrong.");

    }

    finally {

        resetButton(button);

    }

}

/* ===========================
   Missing Values
=========================== */

fillMissingBtn?.addEventListener("click", () => {

    const strategy = document.getElementById("fillStrategy").value;

    postRequest(

        "/cleaning/fill-missing",

        {
            strategy: strategy
        },

        fillMissingBtn

    );

});

/* ===========================
   Remove Duplicates
=========================== */

removeDuplicateBtn?.addEventListener("click", () => {

    if (!confirm("Remove duplicate rows?")) return;

    postRequest(

        "/cleaning/remove-duplicates",

        {},

        removeDuplicateBtn

    );

});

/* ===========================
   Drop Columns
=========================== */

dropColumnsBtn?.addEventListener("click", () => {

    const select = document.getElementById("dropColumns");

    const columns = [...select.selectedOptions].map(option => option.value);

    if (columns.length === 0) {

        alert("Please select at least one column.");

        return;

    }

    postRequest(

        "/cleaning/drop-columns",

        {
            columns: columns
        },

        dropColumnsBtn

    );

});

/* ===========================
   Rename Column
=========================== */

renameColumnBtn?.addEventListener("click", () => {

    const oldColumn = document.getElementById("oldColumn").value.trim();

    const newColumn = document.getElementById("newColumn").value.trim();

    if (!oldColumn || !newColumn) {

        alert("Please enter both column names.");

        return;

    }

    postRequest(

        "/cleaning/rename-column",

        {
            old_column: oldColumn,
            new_column: newColumn
        },

        renameColumnBtn

    );

});

/* ===========================
   Change Data Type
=========================== */

changeTypeBtn?.addEventListener("click", () => {

    const column = document.getElementById("dtypeColumn").value;

    const dtype = document.getElementById("dtype").value;

    postRequest(

        "/cleaning/change-dtype",

        {
            column: column,
            dtype: dtype
        },

        changeTypeBtn

    );

});

/* ===========================
   Download Dataset
=========================== */

downloadDatasetBtn?.addEventListener("click", () => {

    window.location.href = "/cleaning/download";

});