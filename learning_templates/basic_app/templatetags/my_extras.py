from django import template

register = template.Library()

@register.filter(name='cut')

def cut(value,arg):
    """
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg,'')

# register.filter('cut',cut)

 #first argument is going to be the string that you call the function when you use the template tag, and second one is the function itself
#check python documentation
