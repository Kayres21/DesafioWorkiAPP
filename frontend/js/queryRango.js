$(document).ready(function(){

    const cantidad = $('#cantidad');
    $.ajax({
        type: 'GET',
        url: 'http://localhost:3000/encuestas',
        crossDomain: true,
        beforeSend: function(xhr){
            xhr.withCredentials = true;
      },
        success: function (response) {
            $.each(response, function (indexInArray, valueOfElement) { 
                 $cantidad.append('<li>cantidad'+ valueOfElement.count + '</li>');
            });
        }
    });
  });