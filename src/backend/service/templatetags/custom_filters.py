from django import template

register = template.Library()

STARTING_FROM = 1
STEP = 1


@register.filter
def get_range(value):
    return range(STARTING_FROM, value + 1)


@register.filter
def subtract(value, arg):
    return int(value) - arg
