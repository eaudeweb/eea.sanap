$(function () {

  $('.add-item').on('click', function () {
    var trigger = prompt($(this).data('title'));
    if (!trigger) {
        return;
    }

    var li = $('<li />');
    var input = $('<input />');
    var label = $('<label >')

    input.attr({'name': 'triggers',
                'type': 'checkbox',
                'value': trigger});
    label.text(trigger);

    li.append(input)
    li.append(label);
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

});