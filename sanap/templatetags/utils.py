from libs import markup



def pretty(value):
    if isinstance(value, dict):
        page = markup.page()
        page.ul()
        for k, v in value.items():
            if isinstance(v, list) and v:
                pretty_value = ', '.join(v)
            elif isinstance(v, dict) and v:
                subul = markup.page()
                subul.ul()
                subul.li()
                subul.strong(v.keys()[0])
                subul.span(v.values()[0])
                subul.li.close()
                subul.ul.close()
                pretty_value = subul()
            elif v:
                pretty_value = v
            else:
                continue
            page.li()
            page.strong(k.capitalize().replace('_', ' '))
            page.span(pretty_value)
            page.li.close()
        page.ul.close()
        return page()
    elif isinstance(value, list):
        return ', '.join(value)
    return value