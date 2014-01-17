from django.core.urlresolvers import reverse

def reverse2(name, *args, **kwargs):
    return reverse(name, args=args, kwargs=kwargs)