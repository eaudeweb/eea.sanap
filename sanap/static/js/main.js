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

});