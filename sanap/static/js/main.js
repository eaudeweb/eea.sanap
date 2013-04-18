$(function () {

  $('#trigger-add').on('click', function () {
    var trigger = prompt('Add a new trigger');
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
    $('#triggers').append(li);
  });

});