document.addEventListener("DOMContentLoaded", function () {

    
    // DataTable Initialization
    

    const table = $('#datasetTable').DataTable({

        pageLength: 25,

        lengthChange: false,

        searching: true,

        ordering: true,

        paging: true,

        info: true,

        autoWidth: false,

        responsive: true,

        language: {

            emptyTable: "No data available.",

            info: "Showing _START_ to _END_ of _TOTAL_ entries",

            infoEmpty: "No entries found",

            zeroRecords: "No matching records found",

            paginate: {

                previous: "←",

                next: "→"

            }

        }

    });


    
    // Search Box
    

    $("#tableSearch").on("keyup", function () {

        table.search(this.value).draw();

    });


    
    // Show Entries
    

    $("#entriesSelect").on("change", function () {

        table.page.len(this.value).draw();

    });


    
    // Refresh Table
    

    $("#refreshBtn").on("click", function () {

        table.search("").draw();

        $("#tableSearch").val("");

        table.page.len(25).draw();

        $("#entriesSelect").val("25");

    });


    $("#reloadTable").on("click", function () {

        location.reload();

    });


    
    // Export CSV
    

    $("#downloadCSV").on("click", function () {

        let csv = [];

        const rows = document.querySelectorAll("#datasetTable tr");

        rows.forEach(row => {

            let rowData = [];

            row.querySelectorAll("th,td").forEach(cell => {

                rowData.push(
                    '"' +
                    cell.innerText.replace(/"/g, '""') +
                    '"'
                );

            });

            csv.push(rowData.join(","));

        });

        const csvFile = new Blob([csv.join("\n")], {

            type: "text/csv"

        });

        const downloadLink = document.createElement("a");

        downloadLink.download = "dataset.csv";

        downloadLink.href = window.URL.createObjectURL(csvFile);

        downloadLink.style.display = "none";

        document.body.appendChild(downloadLink);

        downloadLink.click();

        document.body.removeChild(downloadLink);

    });


    
    // Row Hover Highlight
    

    $("#datasetTable tbody").on("mouseenter", "tr", function () {

        $(this).addClass("active-row");

    });

    $("#datasetTable tbody").on("mouseleave", "tr", function () {

        $(this).removeClass("active-row");

    });


   
    // Double Click Row
    

    $("#datasetTable tbody").on("dblclick", "tr", function () {

        console.log($(this).data());

    });

});