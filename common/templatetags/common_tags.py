from django import template

register = template.Library()


@register.simple_tag
def active_page(request, view_name):
    from django.core.urlresolvers import resolve, Resolver404
    if not request:
        return ""
    try:
        if resolve(request.path_info).url_name == view_name:
            return "active"
        else:
            return resolve(request.path_info).url_name
    except Resolver404:
        return ""


@register.simple_tag
def h_join(inlist):
    s_out = ''
    s_out += inlist.pop(0)
    if inlist:
        if len(inlist) == 1:
            s_out += ', and ' + inlist.pop(0)
        elif len(inlist) > 1:
            s_out += ', ' + inlist.pop(0)
        else:
            pass
    else:
        pass
    return s_out

