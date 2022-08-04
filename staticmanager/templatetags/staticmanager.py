from django import template
from django.conf import settings
from staticmanager.models import staticManager

register = template.Library()

@register.filter()
def get_key(value, arg):
    if arg in value.__dict__:
        return value.__dict__[arg]
    else:
        return ''

@register.filter()
def get_image(value, arg):
    if arg in value:
        return value[arg]['value']
    else:
        return ''
    
@register.filter()
def staticmanager(value, arg):
    try:
        arg = arg.split(':')
        obj = staticManager.objects.filter(keyobj=arg[0])[0]
        returner=''
        if obj.type == 1:
            returner = obj.textobj
        if obj.type == 2:
            returner = obj.textareaobj
        if obj.type == 3:
            returner = settings.MEDIA_URL + obj.fileobj
        if obj.type == 4:
            
            if arg[1] == 'h':
                returner = obj.linkobjh

            else:
                returner = obj.linkobjb


        return returner
    except:
        try: 
            value2 = value.split(':')
            if value2[1] == 'static':
                value = settings.STATIC_URL + value2[0]
                print(value)
        except:
            pass
    return value
