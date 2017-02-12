function performSearch(e){

	// $("form").on('submit', function (e) {
   //ajax call here
   // console.log($('form').serializeArray());
   var formArray = $('form').serializeArray();
   // console.log(form)
   //stop form submission
   e.preventDefault();
   // console.log(e.serializeArray());

	alert("Code to make AJAX Call");
 //  	return false;
}


function post1(url, jdescrip, resume, callback){
	$.post(url,
    {
        job_description: jdescrip,
        file: resume
    },
    function(data, status){
        alert("Data: " + data + "\nStatus: " + status);
    });
}

var rico = "";
var url_form_data= "";
var names = ["Sam", "Dillon", "Caleb", "Solo", "Viraj", "Harsha", "Sri", "Roshni", "Alex", "Karen"];
var names_url = "";
var location_url = [];
function post(url, results){

	// $.ajax({
	//   type: "POST",
	//   url: url,
	//   data: data,
	//   success: success,
	//   dataType: dataType
	// });

	var formData = new FormData();
	formData.append('file', $('#file')[0].files[0]);
	formData.append('job_description', $('textarea').val());
	// console.log($('textarea').val());
	$.ajax({
	       url : 'http://3fac7b01.ngrok.io/score',
	       type : 'POST',
	       data : formData,
	       processData: false,  // tell jQuery not to process the data
	       contentType: false,  // tell jQuery not to set contentType
	       success : function(data) {
	           // console.log(JSON.stringify(data));
	           console.log(data);
	           // console.log(data[0]['resume'].score);
	           url_form_data += "?";
	           for (var i = 0; i < data.length; i++) {
	           	if (0 < i && i< data.length) {
	           		// console.log("i is " + i);
	           		names_url += "&";
	           	}
	           	rico += "&";
	           	location_url+= "&";
	           	location_url += "Atlanta,GA";
	           	names_url += "name=" + names[i];
	           	rico += "score=" + Math.round(data[i]['resume'].score * 100);
	           }
	           url_form_data += names_url + rico + data.length;
	           console.log(url_form_data);
	           showThis(url_form_data);
	           // alert(data);
	       }
	});	

	

	






	// $.post( url,{}, function( data ) {
	//   // $( results ).html( data );
	//   console.log(data);
	// });
}

function showThis(params){
	// $('iframe.search').attr('src','results.html');
	window.location.href = "results.html" + params;
}





$(document).ready(function(){
	console.log(window.location.href);
	var text = window.location.href;
	var html = "";
	for (var i = 0; i < text.substring((text.length - 1), text.length); i++) {
		
	}
	// $('iframe.search').attr('src','results.html');

	$('form').on('submit', function(e){
		// console.log($('form').serializeArray());
		post("http://51de23df.ngrok.io/score","#");
		e.preventDefault();

		// showThis();

		// $('.container').html('<iframe class="results" src="results.html"></iframe>');

		// console.log("success");


		// performSearch(e);
	});

	$('.details').on('click', function(){
		$('#details_popup').css('display', 'block');
		$('#details_popup').animate({
			opacity: 1
		}, 200);
	});

	$('#x_button').on('click', function(){
		$('#details_popup').animate({
			opacity: 0
		}, 200);

		setTimeout(function(){
			$('#details_popup').css('display', 'none');
		},200);
	});
});