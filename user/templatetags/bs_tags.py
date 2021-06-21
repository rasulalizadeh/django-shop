from django import template
from datetime import datetime

register = template.Library()


@register.filter
def bs_danger(value):
    if value == 'error':
        return 'danger'
    else:
        return value


@register.simple_tag
def bs_now():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
