from flask.ext import wtf
from libs import markup
from libs.markup import oneliner as e


class MultiCheckboxField(wtf.SelectMultipleField):

    def __init__(self, *args, **kwargs):
        self.pre_validate_option = kwargs.pop('pre_validate', False)
        super(MultiCheckboxField, self).__init__(*args, **kwargs)

    def pre_validate(self, form):
        if self.pre_validate_option:
            return super(MultiCheckboxField, self).pre_validate(self, form)
        return True

    widget = wtf.widgets.ListWidget(prefix_label=False)

    option_widget = wtf.widgets.CheckboxInput()


def expand_choices(field):
    choices = list(field.choices)
    if field.data:
        for i in field.data:
            if i not in choices: choices.append((i, i))
        field.choices = tuple(choices)
    return field


class MatrixCheckboxWidget():

    def __init__(self, data, *args, **kwargs):
        self.data = data
        self.id = kwargs.pop('id', '')

    def __call__(self, form_field, **kwargs):
        fields = [f for f in form_field if 'csrf_token' not in f.id ]
        data_keys = [i[0] for i in self.data]

        page = markup.page()
        page.table(id=self.id, class_='matrix')

        page.thead()
        page.tr()
        page.th('', class_='category-left')
        for i, f in enumerate(fields):
            page.th(f.label.text, class_=i%2 and 'odd' or 'even')
        page.tr.close()
        page.thead.close()

        page.tbody()
        page.tr()
        page.td(e.div(data_keys), class_='category-left')
        for i, field in enumerate(fields):
            field.choices = [(k, v) for k, v in self.data]
            odd_even = i%2 and 'odd' or 'even'
            page.td(field(**kwargs), class_=('check-column %s' % odd_even))
        page.tr.close()

        page.tbody.close()
        page.table.close()

        return page
