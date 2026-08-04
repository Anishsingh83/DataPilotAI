// 
//    DATAPILOT AI - GLOBAL ALERT SYSTEM

const alertBox = document.getElementById("customAlert");
const alertTitle = document.getElementById("alertTitle");
const alertMessage = document.getElementById("alertMessage");
const alertIcon = document.getElementById("alertIcon");
const closeAlertBtn = document.getElementById("closeAlert");

let alertTimeout = null;


//    SHOW ALERT
   
// 
function showAlert({
    type = "success",
    title = "Success",
    message = "",
    duration = 4000
}) {

    if (!alertBox) return;

    clearTimeout(alertTimeout);

    alertBox.classList.remove("success", "error", "warning", "info", "show");

    const icons = {
        success: "fa-circle-check",
        error: "fa-circle-xmark",
        warning: "fa-triangle-exclamation",
        info: "fa-circle-info"
    };

    alertBox.classList.add(type);

    alertTitle.textContent = title;
    alertMessage.textContent = message;

    alertIcon.className = `fa-solid ${icons[type] || icons.success}`;

    void alertBox.offsetWidth;

    alertBox.classList.add("show");

    alertTimeout = setTimeout(() => {
        hideAlert();
    }, duration);
}
// 

//    HIDE ALERT
   

function hideAlert() {

    if (!alertBox) return;

    alertBox.classList.remove("show");
}
// 

//    CLOSE BUTTON
   

if (closeAlertBtn) {

    closeAlertBtn.addEventListener("click", () => {

        clearTimeout(alertTimeout);

        hideAlert();
    });

}
// 

//    SHORTCUT FUNCTIONS
   

function showSuccess(message, title = "Success") {

    showAlert({
        type: "success",
        title,
        message
    });

}

function showError(message, title = "Error") {

    showAlert({
        type: "error",
        title,
        message
    });

}

function showWarning(message, title = "Warning") {

    showAlert({
        type: "warning",
        title,
        message
    });

}

function showInfo(message, title = "Information") {

    showAlert({
        type: "info",
        title,
        message
    });

}