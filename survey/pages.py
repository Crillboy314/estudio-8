from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants


#class Demographics(Page):
#    form_model = 'player'
#    form_fields = ['age',
#                   'gender']

class CognitiveReflectionTest(Page):
    form_model = 'player'
    form_fields = [# 'education',
                   'intent',
                   'identity',
                   'risker']

page_sequence = [
#    Demographics,
    CognitiveReflectionTest
]
