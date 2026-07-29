// Upload Trend Chart

const uploadChart = document.getElementById("uploadChart");

if (uploadChart) {

    new Chart(uploadChart, {

        type: "line",

        data: {

            labels: [
                "Mon",
                "Tue",
                "Wed",
                "Thu",
                "Fri",
                "Sat",
                "Sun"
            ],

            datasets: [{

                label: "Uploads",

                data: [12, 18, 15, 25, 20, 28, 35],

                borderColor: "#2563EB",

                backgroundColor: "rgba(37,99,235,.15)",

                fill: true,

                tension: 0.4

            }]

        },

        options: {

            responsive: true,

            plugins: {

                legend: {

                    display: false

                }

            }

        }

    });

}


// File Types Chart

const fileTypeChart = document.getElementById("fileTypeChart");

if (fileTypeChart) {

    new Chart(fileTypeChart, {

        type: "doughnut",

        data: {

            labels: [

                "CSV",
                "Excel",
                "JSON",
                "SQL"

            ],

            datasets: [{

                data: [

                    42,
                    28,
                    18,
                    12

                ],

                backgroundColor: [

                    "#2563EB",
                    "#06B6D4",
                    "#22C55E",
                    "#F59E0B"

                ]

            }]

        },

        options: {

            responsive: true,

            plugins: {

                legend: {

                    position: "bottom"

                }

            }

        }

    });

}