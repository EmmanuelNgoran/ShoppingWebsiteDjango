from django import template

register = template.Library()
#the template file is used as an identifier in the Django Html
#template to refer to a particular field an d style it depending of the 
#value returned by the server
@register.filter
def field_type(bound_field):
    return bound_field.field.widget.__class__.__name__
#if there is an error while matching the input of the user
#there will be call of the following to syle the form with 'is-valid' css selector
#or the 'is-invalid' css selector or only form-control
@register.filter
def input_class(bound_field):
    css_class = ''
    if bound_field.form.is_bound:
        if bound_field.errors:
            css_class = 'is-invalid'
        elif field_type(bound_field) != 'PasswordInput':
            css_class = 'is-valid'
        elif field_type(bound_field) !='IntegerField':
            css_class = 'is-valid'
    return 'form-control {}'.format(css_class)