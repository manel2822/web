loadData();

function loadData() {
    httpRequest = new XMLHttpRequest();
    httpRequest.open('GET', '/api/data');
    httpRequest.onreadystatechange = function() {
        if (httpRequest.readyState === 4 && httpRequest.status === 200) {
            jsonData1 = JSON.parse(httpRequest.response);
            update_mixed(jsonData1);
        }
    };
    httpRequest.send();


    httpRequest1 = new XMLHttpRequest();
    httpRequest1.open('GET', '/api/data1');
    httpRequest1.onreadystatechange = function() {
        if (httpRequest1.readyState === 4 && httpRequest1.status === 200) {
            jsonData1 = JSON.parse(httpRequest1.response);
            update_doughnut(jsonData1);
        }
    };
    httpRequest1.send();


    httpRequest2 = new XMLHttpRequest();
    httpRequest2.open('GET', '/api/data2');
    httpRequest2.onreadystatechange = function() {
        if (httpRequest2.readyState === 4 && httpRequest2.status === 200) {
            jsonData1 = JSON.parse(httpRequest2.response);
            update_Lines(jsonData1);
        }
    };
    httpRequest2.send();

    httpRequest3 = new XMLHttpRequest();
    httpRequest3.open('GET', '/api/data3');
    httpRequest3.onreadystatechange = function() {
        if (httpRequest3.readyState === 4 && httpRequest3.status === 200) {
            jsonData1 = JSON.parse(httpRequest3.response);
            update_multi_Lines(jsonData1);
        }
    };
    httpRequest3.send();

    httpRequest4 = new XMLHttpRequest();
    httpRequest4.open('GET', '/api/data4');
    httpRequest4.onreadystatechange = function() {
        if (httpRequest4.readyState === 4 && httpRequest4.status === 200) {
            jsonData1 = JSON.parse(httpRequest4.response);
            update_number(jsonData1);
        }
    };
    httpRequest4.send();

    httpRequest5 = new XMLHttpRequest();
    httpRequest5.open('GET', '/api/data5');
    httpRequest5.onreadystatechange = function() {
        if (httpRequest5.readyState === 4 && httpRequest5.status === 200) {
            jsonData1 = JSON.parse(httpRequest5.response);
            update_bar(jsonData1);
        }
    };
    httpRequest5.send();
    httpRequest6 = new XMLHttpRequest();
    httpRequest6.open('GET', '/api/data6');
    httpRequest6.onreadystatechange = function() {
        if (httpRequest6.readyState === 4 && httpRequest6.status === 200) {
            jsonData1 = JSON.parse(httpRequest6.response);
            update_Line(jsonData1);
        }
    };
    httpRequest6.send();
}


function update_mixed(jsonData) {
    var labels = jsonData.years;
    for (d of jsonData.datasets) {

        d.borderColor = '#' + Math.floor(Math.random() * 16777215).toString(16);
        d.borderWidth = 3;
    }

    var data = jsonData.datasets;
    new Chart(document.getElementById("mixed-chart"), {
        type: 'bar',
        data: {
            labels: labels,
            datasets: data
        },
        options: {
            responsive: false,
            maintainAspectRatio: true,
            title: {
                display: true,
                text: 'Analysis of admitted and failed student',
                position: 'bottom'
            },

            legend: { display: false },
            scales: {
                yAxes: [{
                    ticks: {
                        min: 0,
                        max: 400,

                    },
                    scaleLabel: {
                        display: true,

                        labelString: "number of students"
                    }
                }]
            }

        }
    });
}




function update_doughnut(jsonData) {

    var labels = jsonData.map(function(e) {
        return e.specialite;
    });

    var data = jsonData.map(function(e) {
        return e.failed;
    });

    new Chart(document.getElementById("doughnut-chart"), {
        type: 'doughnut',
        data: {

            labels: labels,
            datasets: [{
                backgroundColor: ["#aaaaaa", "#cc00ea", "#c44444", "#3cd37f", "#ffbc00", "#29edcb", "#f98363"],
                data: data
            }]
        },
        options: {

            responsive: false,
            maintainAspectRatio: true,
            legend: {
                display: false,
            },
            title: {
                display: true,
                text: ' The number of students failing in 2021 in each specialty',
                position: 'bottom'

            },

        }




    });


}






function update_Lines(jsonData) {
    var labels = jsonData.years;

    for (d of jsonData.datasets) {
        d.fill = 1;
        d.borderColor = '#' + Math.floor(Math.random() * 16777215).toString(16);
        d.borderWidth = 2;
        d.radius = 1;
    }

    var data = jsonData.datasets;

    new Chart(document.getElementById("line-chart"), {
        type: 'line',
        data: {
            labels: labels,
            datasets: data
        },
        options: {
            responsive: false,
            maintainAspectRatio: true,
            title: {
                display: true,
                text: 'The evolution of the means of specialties in each year'
            },
            legend: {
                position: 'right'
            }
        }
    });
}

function update_multi_Lines(jsonData) {
    var labels = jsonData.label;

    var data = jsonData.datasets;

    new Chart(document.getElementById("bar-chart-grouped"), {
        type: 'bar',
        data: {

            labels: labels,
            datasets: data
        },
        options: {
            responsive: false,
            maintainAspectRatio: true,
            title: {
                display: true,
                text: 'Analysis of the number of M & F in each specialty',
                font: {
                    size: 20
                }
            },
            legend: {
                position: 'right'
            }
        }
    });
}

function update_number(jsonData) {

    var i = 1;
    for (d of jsonData) {
        specialite = document.getElementById("sp" + i);
        label = specialite.getElementsByClassName("spLabel")[0];
        pop = specialite.getElementsByClassName("spPor")[0];

        label.innerText = d["specialite"];
        pop.innerText = d["total"] + "%";

        i++;
    }

}

function update_bar(jsonData) {
    var labels = jsonData.years;


    var data = jsonData.datasets;

    console.log(data)

    new Chart(document.getElementById("bar-chart"), {
        type: 'bar',
        data: {

            labels: labels,
            datasets: [{
                label: "Population in each year",
                backgroundColor: ["#3e95cd", "#8e5ea2", "#3cba9f"],
                data: data
            }]
        },
        options: {
            responsive: false,
            maintainAspectRatio: true,
            legend: { display: false },
            title: {
                display: true,
                text: 'The Analysis of the number of students in each year',
                position: 'bottom'
            },
            scales: {
                yAxes: [{
                    ticks: {
                        min: 0,
                        max: 490,

                    },
                    scaleLabel: {
                        display: true,

                        labelString: "student of numbers"
                    }
                }]
            }
        }
    });
}


function update_Line(jsonData) {
    var labels = jsonData.years;
    for (d of jsonData.datasets) {
        d.fill = 0;
        d.borderColor = '#' + Math.floor(Math.random() * 16777215).toString(16);
        d.borderWidth = 2;
        d.radius = 1;
    }

    var data = jsonData.datasets;

    new Chart(document.getElementById("linechart"), {
        type: 'line',
        data: {
            labels: labels,
            datasets: data
        },
        options: {
            responsive: false,
            maintainAspectRatio: true,
            title: {
                display: true,
                text: 'The evolution of the number of students in each specialty'
            },
            legend: {
                position: 'right'
            }
        }
    });
}