function render()
{
    var method = 'POST';
//    var host_url = document.getElementById('host_url').value;
    var host_url = 'http://localhost:8000';
    var fullurl = host_url + '/render/';
    var objects = document.getElementById('objects').value;
    var morphisms = document.getElementById('morphisms').value;
    var data = {'objects': objects, 'morphisms': morphisms};

    var req = new XMLHttpRequest();

    req.open(method, fullurl, true);

    req.onload = function () {
        json_response = JSON.parse(this.responseText);
        if (json_response['status'] == 'success')
            document.getElementById('render').innerHTML = '<img src="' + json_response['render'] +'">';
    };


    req.onreadystatechange = function() {
        if(req.readyState == 4 && req.status == 200) {
            //alert(req.responseText);
        }
    }

    req.send(JSON.stringify(data));
}
