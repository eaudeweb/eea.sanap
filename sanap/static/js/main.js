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

  $('.main-instruments-other').on('click', function (e) {

    e.preventDefault();

    var row = $('#main-instruments').find('tbody tr:last');
    var category = prompt('Add another category');
    var fields = ['agriculture', 'forestry', 'biodiversity', 'human_health',
                  'water', 'marine_fisheries', 'coastal_areas', 'mountain_areas',
                  'tourism', 'transport', 'energy', 'built_environment',
                  'spatial_planning', 'civil_protection', 'industry',
                  'business_services', 'financial_insurance', 'cultural_heritage'];

    if(!category) return;

    row.find('td').eq(0).append($('<div>').attr({
      'class': 'category-left',
    }).text(category));


    $.each(fields, function (i, value) {
      var parent_html = $('<li>')
      var input = $('<input>').attr({
        'type': 'checkbox',
        'value': category,
        'name': 'main_instruments-' + value
      });
      parent_html.append(input);
      row.find('td').eq(i+1).find('ul').append(parent_html);
    });

  });

});