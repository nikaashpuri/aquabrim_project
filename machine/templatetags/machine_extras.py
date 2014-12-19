__author__ = 'nikaashpuri'

from django import template

register = template.Library()

@register.filter
def subtract(value, arg):
    return int(arg) - value/5


@register.filter
def add_special(value, arg):
    return int(arg) + (110 -value)