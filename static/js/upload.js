const fileInput = document.getElementById("dataset");
const fileName = document.getElementById("file-name");

if (fileInput) {

    fileInput.addEventListener("change", function () {

        if (this.files.length > 0) {

            fileName.textContent = this.files[0].name;

        } else {

            fileName.textContent = "No file selected";

        }

    });

}