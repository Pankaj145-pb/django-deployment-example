from django import template

register = template.Library()

@register.filter(name = 'cut')
def cut(value,arg):
    """
    This Cuts Out all Values Of R From string !
    """
    return value.replace(arg,'')

# register.filter('cut',cut)
