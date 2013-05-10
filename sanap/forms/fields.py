from flask.ext import wtf
from flask import url_for
from libs import markup
from libs.markup import oneliner as e
from sanap.model_data import SECTORS_DATA


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


class ListTextWidget(object):

    def __call__(self, field, **kwargs):
        page = markup.page()
        page.ul(id=field.id)

        for subfield in field:
            page.li()
            value = field.data.get(subfield.data, '') if field.data else ''
            page.input(name=subfield.name, id=subfield.id, value=value)
            page.li.close()
        page.ul.close()
        return page()


class ListTextAreaWidget(object):

    def __call__(self, field, **kwargs):
        page = markup.page()
        page.ul(id=field.id)

        for subfield in field:
            page.li()
            value = field.data.get(subfield.data, '') if field.data else ''
            page.textarea(value, name=subfield.name, id=subfield.id,
                          class_='cell')
            page.textarea.close()
            page.li.close()
        page.ul.close()
        return page()

class MultiTextField(wtf.SelectMultipleField):

    widget = ListTextWidget()

    def process_data(self, value):
        self.data = value if isinstance(value, dict) else ''

    def process_formdata(self, valuelist):
        data = dict(zip(SECTORS_DATA, valuelist))
        self.data = dict((k, v) for k, v in data.iteritems() if v)

    def pre_validate(self, form):
        pass

class MultiTextAreaField(MultiTextField):

    widget = ListTextAreaWidget()


class CustomFileInput(wtf.widgets.FileInput):

    def __call__(self, field, **kwargs):
       result = super(CustomFileInput, self).__call__(field, **kwargs)
       values = field.data
       if values and isinstance(values, list):
            page = markup.page()
            page.p('Currently uploaded files', class_="file-storage")
            page.ul(_class='file-list')
            for value in values:
                page.li()
                page.a(value,
                       href=url_for('static', filename='files/%s' % value),
                       target='_blank')
                page.li.close()
            page.ul.close()
            result += page()
       return wtf.widgets.core.HTMLString(result)


class CustomFileField(wtf.FileField):

    widget = CustomFileInput()

    def process_formdata(self, valuelist):
        if valuelist and valuelist[0]:
            filestorage = valuelist[0]
            filestorage.filename = filestorage.filename.lower()
            self.data = filestorage
        else:
            self.data = ''

    def process_data(self, value):
        self.data = list(value) if value else None


class CustomRadioField(wtf.RadioField):

    def process_formdata(self, valuelist):
        if not valuelist:
            self.data = None
        else:
            self.data = valuelist[0]


class CustomBoolean(wtf.BooleanField):

    def process_formdata(self, valuelist):
        if bool(valuelist[0]):
            self.data = '1'
        else:
            self.data = ''


class Tagit(wtf.TextField):

    def process_data(self, value):
        if isinstance(value, list):
            self.data = ','.join(value)
        else:
            self.data = ''


def expand_choices(field):
    choices = list(field.choices)
    if field.data:
        for i in field.data:
            if i not in [c[0] for c in choices]: choices.append((i, i))
        field.choices = tuple(choices)
    return field


class MatrixBaseWidget(object):

    def update_data(self, form_field, data):
        for value in form_field.data.values():
            if not value: continue
            for item in value:
                if item not in [i[0] for i in data]: data.append((item, item))
        return data

    def update_keys(self, form_field, data_keys):
        for value in form_field.data.values():
            if not value: continue
            for item in value:
                if item not in data_keys: data_keys.append(item)
        return data_keys


class MatrixCheckboxWidget(MatrixBaseWidget):

    def __init__(self, data, *args, **kwargs):
        self.data = data
        self.id = kwargs.pop('id', '')
        self.label = kwargs.pop('label', '')
        self.title = kwargs.pop('title', '')

    def __call__(self, form_field, **kwargs):
        fields = [f for f in form_field if 'csrf_token' not in f.id ]
        data_keys = [i[0] for i in self.data]
        data_keys = self.update_keys(form_field, data_keys)
        self.data = self.update_data(form_field, self.data)

        page = markup.page()
        page.label(self.label)
        page.table(id=self.id, class_='matrix')
        page.thead()
        page.tr()
        page.th(self.title, class_='category-left')
        for i, f in enumerate(fields):
            page.th(f.label.text.capitalize(), class_=i%2 and 'odd' or 'even',
                    id="%s-%d" % (self.id, i))
        page.tr.close()
        page.thead.close()

        page.tbody()
        page.tr()
        page.td(e.div(data_keys), class_='category-left')
        for i, field in enumerate(fields):
            field.choices = [(k, v) for k, v in self.data]
            odd_even = i % 2 and 'odd' or 'even'
            page.td(field(**kwargs), class_=('check-column %s' % odd_even))
        page.tr.close()

        page.tbody.close()
        page.table.close()

        return page

