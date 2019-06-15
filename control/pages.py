from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants


class Introduction(Page):
    def vars_for_template(self):
        return {
            'sufee' : self.session.config['participation_fee'],
            'erpoint' : self.session.config['real_world_currency_per_point']*100
        }

    def is_displayed(self):
        return self.round_number == 1


class Tree(Page):

    def is_displayed(self):
        return self.round_number == 1


class Quiz(Page):
    form_model = 'player'
    form_fields = ['question_1', 'question_2']

    def is_displayed(self):
        return self.round_number == 1

    def error_message(self, values):
        if values['question_1'] != 40 and values['question_2'] != 20:
            return 'Both questions are incorrect'
        elif values['question_1'] == 40 and values['question_2'] !=20:
            return 'Question 2 is incorrect'
        elif values['question_1'] != 40 and values['question_2'] == 20:
            return 'Question 1 is incorrect'

class Decision(Page):
    form_model = 'player'
    form_fields = ['decision']


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        for p in self.group.get_players():
            p.set_payoff()


class Results(Page):
    def vars_for_template(self):
        me = self.player
        opponent = me.other_player()
        fee = self.session.config['participation_fee']
        return {
            'my_decision': me.decision,
            'opponent_decision': opponent.decision,
            'same_choice': me.decision == opponent.decision,
        }

    def app_after_this_page(self, upcoming_apps):
        if self.round_number == 2:
            return 'gamble'


page_sequence = [
    Introduction,
    Tree,
    Quiz,
    Decision,
    ResultsWaitPage,
    Results
]
