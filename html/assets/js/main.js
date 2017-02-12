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











$(document).ready(function(){

	$('form').on('submit', function(e){
		// console.log($('form').serializeArray());
		performSearch(e);
	});



});