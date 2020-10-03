from django import template

from staff.models import UserProfile


register = template.Library()


@register.simple_tag
def get_currency():
    # TODO Если профилей нет - падает
    return UserProfile.objects.first().currency
