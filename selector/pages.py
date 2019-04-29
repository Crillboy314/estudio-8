from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(WaitPage):

    def app_after_this_page(self, upcoming_apps):
        t = self.group.treatment
        if t == 'default':
            return 'control'
        elif t == 't1':
            return 'control1'
        else:
            return 'control2'


page_sequence = [
    MyPage
]
