from flask.ext import wtf


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