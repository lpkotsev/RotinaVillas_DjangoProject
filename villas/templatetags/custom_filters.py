from django import template

register = template.Library()

@register.filter
def euro(value):
    return f"€{value}"