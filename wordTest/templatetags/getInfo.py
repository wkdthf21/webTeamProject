from django import template

register = template.Library()

@register.simple_tag
def getSpellById(things, id):
    return things.get(word_id=id).word_spell

@register.simple_tag
def getMeanById(things, id):
    return things.get(word_id=id).word_mean

@register.simple_tag
def getTestById(things, id):
    return things.get(pk=id).test_id

@register.simple_tag
def getDateById(things, id):
    return things.get(pk=id).test_date
