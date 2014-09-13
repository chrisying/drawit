function debounce(func, wait, immediate) {
  var timeout;

  return function() {
    var context = this, args = arguments;
    clearTimeout(timeout);

    timeout = setTimeout(function() {
      timeout = null;
      if (!immediate) func.apply(context, args);
    }, wait);

    if (immediate && !timeout) func.apply(context, args);
  };
}

$(document).ready(function (){
  $.each(['#f00', '#ff0', '#0f0', '#0ff', '#00f', '#f0f', '#000', '#fff'],
    function() {
      $('.canvas-tool-container').append("<a class='color-tool' href='#main-canvas' data-color='" + this + "' style='background: " + this + ";'></a> ");
  });

  $.each([1, 2, 3, 5, 10, 15],
    function() {
      $('.canvas-tool-container').append("<a class='size-tool' id='size-tool-" + this + "' href='#main-canvas' data-size='" + this + "'><h3>" + this + "</h3></a> ");
  });

  var image_links = {'marker': 'assets/marker.png',
                     'eraser': 'assets/eraser.png'};
  $.each(['marker', 'eraser'],
    function() {
      $('.canvas-tool-container').append("<a class='function-tool' id='function-tool-" + this + "' href='#main-canvas' data-tool='" + this + "'><img src=" + image_links[this] + "></a> ");
  });
  $('.canvas-tool-container').append("<a class='submit-tool' id='submit-tool-submit'></a> ");

  $('#main-canvas').sketch({defaultColor: '#000',
                            defaultSize: 5,
                            defaultTool: 'marker'});

  var active_size_tool = 'size-tool-5';
  var active_function_tool = 'function-tool-marker';
  $('#size-tool-5').addClass('active');
  $('#function-tool-marker').addClass('active');

  $('.size-tool').click(function (e) {
    console.log(e);
    if (e.currentTarget.id !== active_size_tool) {
      $('#' + active_size_tool).removeClass('active');
      active_size_tool = e.currentTarget.id;
      $('#' + active_size_tool).addClass('active');
    }
  });

  $('.function-tool').click(function (e) {
    console.log(e);
    if (e.currentTarget.id !== active_function_tool) {
      $('#' + active_function_tool).removeClass('active');
      active_function_tool = e.currentTarget.id;
      $('#' + active_function_tool).addClass('active');
    }
  });

  $('.submit-tool').click(function (e) {
    var dataURL = $('#main-canvas')[0].toDataURL();

    $.ajax({
      type: 'POST',
      url: '/picture?title=butterfly&row=0&col=0',
      data: {
        image: dataURL
      },
      success: function (data) {
        window.location.href = '/';
      },
      error: function (xhr, status, err) {
        console.log(err);
      }
    });
  });
});

$(document).ready(function () {
  //var active_zoom_tool = null
  var image = null;
  var is_dragging = false;
  var initial_image_offset = {};
  var initial_total_offset = {};

  var unbind_function = function (e) {
    $('#main-viewport').unbind('mousemove');
    $(window).unbind('mouseup', unbind_function);
    $('#main-canvas').unbind('mouseup', unbind_function);
    is_dragging = false;
  };

  $('img').on('dragstart', function(e) {
    e.preventDefault();
  });

  $('#main-viewport').mousedown(function (e) {
    /*if (active_zoom_tool) {

    }*/
    e.preventDefault();

    image = $('#main-viewport-image');
    initial_image_offset = {'left': parseInt(image.css('left'), 10),
                            'top': parseInt(image.css('top'), 10)
                           };
    initial_total_offset = {'left': initial_image_offset.left - e.pageX,
                            'top': initial_image_offset.top - e.pageY};


    $('#main-viewport').mousemove(function (e) {
      if (!is_dragging) {
        $(window).mouseup(unbind_function);
        $('#main-canvas').mouseup(unbind_function);
        is_dragging = true;
      }

      console.log(e.pageX, e.pageY);

      image.css({'left': initial_total_offset.left + e.pageX,
                 'top': initial_total_offset.top + e.pageY});
    });
  });
});