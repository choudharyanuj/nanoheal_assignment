window.onload = function() {
    var xhr = new XMLHttpRequest();
    xhr.open('GET','http://127.0.0.1:5000/home')
    xhr.send()
    xhr.onload = function(){
        if(xhr.data !== null) {
            var datas = JSON.parse(xhr.response)
            console.log(datas)
        }
        else{
            console.log("Data Not Found")
        }
        datas.map(function(element){
            $("#display").append(
                "<div id ='allmovie'>" + 
                    "<h1>Name:" + element.name +"</h1>" + 
                    "<h2>Category: " + element.category + "</h2>" +
                    "<h5 class='description'>Description: " +element.description+ "</h5>" + 
                    "<hr></hr>" +
                "</div>"
            );
        });
    }
}

function search() {
    var data = document.getElementById('data').value
    console.log(data)
    var xhrsearch = new XMLHttpRequest();
    var url ='http://127.0.0.1:5000/search'
    var params = 'data'
    xhrsearch.open('POST',url)
    xhrsearch.send()
    xhrsearch.onload = function(){
        if(xhrsearch.data !== null) {
            var datas = JSON.parse(xhrsearch.response)
            console.log(datas)
        }
        else{
            alert("Data Not Found")
        }
        if (datas.length == 0) {
            $("#display").append(
                "<div id ='allmovie'>" + 
                    "<h1>No DATA FOUND" +"</h1>" + 
                    "<hr></hr>" +
                "</div>"
            );
        }
        else {
            datas.map(function(element){
                $("#display").append(
                    "<div id ='allmovie'>" + 
                        "<h1>Name:" + element.name +"</h1>" + 
                        "<h2>Category: " + element.category + "</h2>" +
                        "<h5 class='description'>Description: " +element.description+ "</h5>" + 
                        "<hr></hr>" +
                    "</div>"
                );
            });
        }
    }
}
function add() {
    alert("Will Update Shortly")
}
function edit() {
    alert("Will Update Shortly")
}
function deletedata() {
    alert("Will Update Shortly")
}