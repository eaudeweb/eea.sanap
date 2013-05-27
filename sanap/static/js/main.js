$(function () {

  $('.add-item').on('click', function () {
    var value = prompt($(this).data('title'));
    if (!value) {
        return;
    }

    var li = $(this).parents('.row').find('ul').find('li:last').clone();
    var input = li.find('input');
    var label = li.find('label');

    var next_id = input.attr('id').replace(/\d+$/, function(n){ return (++n) });

    input.attr({'id': next_id,
                'checked': 'checked',
                'value': value});
    label.text(value);
    label.attr({'for': next_id})

    $(this).parents('.row').find('ul').append(li);
  });

  $('.matrix-other').on('click', function (e) {

    e.preventDefault();

    var row = $(this).parents('.row').find('tbody tr:last');
    var name = $(this).data('name');
    var category = prompt('Add another category');
    var fields = $(this).data('fields');

    if(!category) return;

    row.find('td').eq(0).append($('<div>').attr({
      'class': 'category-left',
    }).text(category));


    $.each(fields, function (i, value) {
      var parent_html = $('<li>')
      var input = $('<input>').attr({
        'type': 'checkbox',
        'value': category,
        'name': name + '-' + value
      });
      parent_html.append(input);
      row.find('td').eq(i+1).find('ul').append(parent_html);
    });

  });

  $('.tagit').select2({
    width: '600px',
    tags: [],
    tokenSeparators: [],
    formatNoMatches: function (term) { return "Use Tab/Enter key between different items." },
  });

  $('#sectors-adaptation_national,#sectors-adaptation_sub_national,#sectors-adaptation_local').find('input').spinner({
    min: 0, max: 6
  });


  // Ask user about leaving page when changes are unsaved
  $("form.ecoAsVir :input").change(function() {
    $('form.ecoAsVir').data('changed', true);
  });
  $("form.ecoAsVir button").mouseup(function() {
    $('form.ecoAsVir').data('changed', false);
  });
  window.onbeforeunload = function() {
    var assessment_form = $('form.ecoAsVir');
      if (assessment_form && assessment_form.data('changed')) {
        return 'You have unsaved changes in the assessment! Scroll to the bottom and use the "Save Draft" button to save your answers.';
      }
      return undefined;
  };


  // disabled inputs on submitted self-assessment
  $("form.ecoAsVir.final :input").attr("disabled", "disabled");

  $('.submitVersion').on('click', function (e) {

    var questions = [];
    var total_number = $('.question').length;
    $('.question').each(function () {
      var question = $(this);
      var answered = false;
      question.find(':input').each(function () {
        var input = $(this);
        if((input.is(':text') && input.val() != '') ||
           (input.is(':radio,:checkbox') && input.is(':checked')) ||
           (input.is('textarea') && input.val() != '')) {
          answered = true;
        };
      });
      if(answered) {
        questions.push(question);
        question.removeClass('unanswered');
      }
      else{
        question.hasClass('unanswered') || question.addClass('unanswered');
      }

    });

    if(questions.length < total_number) {
      if(confirm('You havn\'t answered ' + (total_number - questions.length) +
                 ' questions.\nWe have highlighted them for you.\n\nClick OK to continue '+
                 'submitting the final version without the possibility of changing the answers, '+
                 'or Cancel to go back to the questions.')) {
        return true;
      } else {
        e.preventDefault();
      }
    }

  });

  var scrollTo = function (top) {
     $('html, body').animate({scrollTop: top}, 'fast');
  };
  $('#scroll-top').on('click', function () {
    scrollTo(0);
  });
  $('#scroll-bottom').on('click', function () {
    scrollTo($(document).height());
  });


  $('.contact-answers').find('.question-row').each(function () {
    var ul_count = $(this).find('ul').length;
    var ul_empty_count = 0;
    $(this).find('ul').each(function () {
      if(!$.trim($(this).html())) {
        ul_empty_count = ul_empty_count + 1;
      }
    });

    if(ul_empty_count == ul_count) {
      var div = $('<div />');
      div.attr({'class': 'no-answer'});
      div.text('No answers for this question');
      $(this).find('.question-container').append(div);
    }
  });

  function multiple_upload_handler() {
    var changed = $(this);
    var last_input = $("input[type=file]", $(this).parent()).last();
    if (last_input.val()) {
      var new_input = changed.clone();
      new_input.change(function(){multiple_upload_handler.call(new_input[0])});
      new_input.css({float: "none", display: "block"});
      last_input.css({float: "none", display: "block"});
      last_input.after(new_input);
    }
  }

  // Multiple file input
  $('input[type=file]').change(function(){
    multiple_upload_handler.call(this);
  });

  $('.matrix').on('click', 'li', function (e) {
    var input = $(this).find('input[type=checkbox]');
    if(input.is(':checked')) {
      input.prop('checked', false);
    } else {
      input.prop('checked', true);
    }
  });

  $('.matrix').on('click', 'li input', function (e) {
    e.stopPropagation();
  });

});
