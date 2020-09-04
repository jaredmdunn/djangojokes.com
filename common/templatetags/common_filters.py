from django import template
from django.template.defaultfilters import date

register = template.Library()

@register.filter
def webudate(value, format):
    if (format == 'QY'):
        try:
            if (value.month <= 3):
                return f'1, {value.year}'
            elif (value.month <= 6):
                return f'2, {value.year}'
            elif (value.month <= 9):
                return f'3, {value.year}'
            elif (value.month <= 12):
                return f'4, {value.year}'
        except AttributeError:
            return ''
    else:
        return date(value, format)