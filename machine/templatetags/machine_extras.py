__author__ = 'nikaashpuri'

from django import template

register = template.Library()

@register.filter
def subtract(value, arg):
    return 215 - value


@register.filter
def add_special(value, arg):
    return 65 + (110 -value)