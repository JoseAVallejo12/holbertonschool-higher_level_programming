/* delete any class name and set classname to green */
$('header').removeClass($('header').attr('class')).addClass('green');
/* Toggle between red and green name class en onclick event */
$('#toggle_header').click(() => {
  if ($('header').hasClass('green')) {
    $('header').removeClass('green').addClass('red');
  } else {
    $('header').removeClass('red').addClass('green');
  }
});
