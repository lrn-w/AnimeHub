/*!
* Start Bootstrap - Modern Business v5.0.7 (https://startbootstrap.com/template-overviews/modern-business)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-modern-business/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project


$(document).ready(function(){

  $("#submit-button").click(function(event){
  event.preventDefault();

  var form = $("#order-form")[0]

  var data = new FormData(form);

  $.ajax( {
    type: "POST",
    enctype: 'multipart/form-data',
    url: "http://localhost:5000/order/new",
    data: data,
    processData: false,
    contentType: false,
    cache: false,
    timeout: 800000,
    success: function(data){
    $("#order-response").text(data);
      },
    error: function (err) {
    console.log("error occured");
    }
    });
  });
});

