from django import template

register = template.Library()

@register.filter(name='multifloatformat')
def multifloatformat(value, factor):
    try:
        value = float(value) * float(factor)
        return format(value, '.2f')  # Format with 2 decimal places
    except (TypeError, ValueError):
        return value
