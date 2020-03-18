$(".copy").on("click",function(){
    var copiedText = $("#short_url"); 
    if(copiedText != ""){
    /* Selecting text field */
    copiedText.select(); 
    document.execCommand("copy"); 
    alert("Copied");
    }
    else{
        alert("Copying Failed");
    }
})
$(".clear").on("click",function(){
    $('#long_url').val("");
    $("#short_url").val("");
})


document.getElementById('paste').addEventListener('click', ()=>{
  let pasteArea = document.getElementById('long_url');
  pasteArea.value = '';

  navigator.clipboard.readText()
  .then((text)=>{
      pasteArea.value = text;
  });
});


$(document).ready(function() {
    M.updateTextFields();
  });

  $('.popover-dismiss').popover({
    trigger: 'focus'
  })
/*popup*/
$(function () {
    //  enable popovers everywhere
    $('[data-toggle="popover"]').popover()
  })
  
  moveButton = function() {
      $("#toggle").css('left', "100px")
  }
  
  var x
  window.setInterval(function() {
      newx = $("#toggle").css('left')
    if (newx != x) {
       $("#toggle").popover('update')
       x = newx
    }
  }, 100);
  
  
  
  $("[data-toggle=popover][data-container=body]").each(function(i, obj) {
  
  $(this).popover({
    html: true,
    //trigger: 'focus', //  close on click elsewhere
    //PROBLEM: clicking button again doesn't close.
    content: function() {
      var id = $(this).attr('data-popover-content')
      return $('#popover-content-' + id).html();
    }
  });
  
  });
  /*Footer */
  var d = new Date();
document.getElementById("year").innerHTML = d.getFullYear();