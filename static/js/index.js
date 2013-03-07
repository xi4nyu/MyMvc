$(function(){
    $("#msg").text("jQuery init ...");

});


function get_url(url) {
    $.get(url, function(r) {
	alert(r);
    });

}


function post_url(ulr) {
    $.post(url, function(r) {
	alert("post");
    });
}


function ajax_url(url) {
    var option = {
	url: url,
	method: "GET",
	crossDomain: true,
	success: function(r) {
	    alert("success");
	},
	error: function(r) {
	    alert("error");
	}
    };


    $.ajax(option);
	
	
}

