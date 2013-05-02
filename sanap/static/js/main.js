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

});
