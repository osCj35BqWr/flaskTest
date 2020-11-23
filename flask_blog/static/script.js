function getImg(obj) {
    var idx = obj.selectedIndex;
    var value = obj.options[idx].value;
    var plotdata = document.getElementById('s3img');

    var eventDataBaseUrl = "{{ url_for('img', 'DUMMY_VALUE') }}"
    var actualDataUrl = eventDataBaseUrl.replace('DUMMY_VALUE', value)
    alert(actualDataUrl)

    $.get(actualDataUrl, function(data) {
        plotdata.src = "data:image/jpeg;base64," + data;
    });
};
