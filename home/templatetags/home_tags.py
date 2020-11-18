from django import template
import datetime
register = template.Library()

@register.simple_tag(name='get_time')
def get_time():
    return datetime.time.max()