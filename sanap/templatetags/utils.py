from flask import Markup
from libs import markup

from sanap.models import User


def is_not_empty(value):
    if value:
        if isinstance(value, dict):
            return any(value.values())
        return True
    return False


def pretty(value):
    if isinstance(value, dict):
        page = markup.page()
        page.ul(_class='dict')
        for k, v in value.items():
            if isinstance(v, list) and v:
                pretty_value = Markup.escape(', '.join(v))
            elif isinstance(v, dict) and v:
                subul = markup.page()
                subul.ul(_class='subdict')
                subul.li()
                subul.span('%s: ' % v.keys()[0])
                subul.span(Markup.escape(v.values()[0]))
                subul.li.close()
                subul.ul.close()
                pretty_value = subul()
            elif v:
                pretty_value = Markup.escape(v)
            else:
                continue
            page.li()
            page.span('%s:' % k.capitalize().replace('_', ' '))
            page.span(pretty_value)
            page.li.close()
        page.ul.close()
        return page()
    elif isinstance(value, list):
        return Markup.escape(', '.join(value))
    else:
        page = markup.page()
        page.span(Markup.escape(value), _class='simple')
        return page()

def country_coordinators(value):
    return User.objects.filter(country=value, invitee=None)
