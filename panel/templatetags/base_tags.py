from django import template

register = template.Library()

@register.simple_tag
def title():
    return "وبلاگ جنگویی"


@register.inclusion_tag('panel/partials/link.html')
def link(request, link_name, content, classes):
    return {
        "request": request,
        "link_name": link_name,
        "link": "panel:{}".format(link_name),
        "content": content,
        "classes": classes
    }
