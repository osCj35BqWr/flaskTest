function getImg(obj) {
    var idx = obj.selectedIndex;
    var value = obj.options[idx].value;
    var plotdata = document.getElementById('s3img');
    $.get("/img/" + value, function(data) {
        plotdata.src = "data:image/jpeg;base64," + data;
    });
};
