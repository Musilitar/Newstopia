// JavaScript Document

function setDate() {
    var months = [
    'Januari', 'Februari', 'Maart', 'April', 'Mei', 'Juni', 'Juli',
    'Augustus', 'September', 'Oktober', 'November', 'December'
    ];
    var tomorrow = new Date();
    document.getElementById('date').innerHTML = tomorrow.getDate() + " " + months[tomorrow.getMonth()] + " " + tomorrow.getFullYear();
}

window.onload = setDate;