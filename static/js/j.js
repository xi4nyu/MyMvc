$(function(){
    $("#btnclick").click(post);
});


function post() {
    var cond = {"condition": {"name": "jack", "age": 20}};
    cond = JSON.stringify(cond);
    $.post("/jquery", {"post_data": cond}, function(r) {
	console.log(r);
    });
}

function remove() {
    $(this).parent().parent().remove();
}
