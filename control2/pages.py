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


class Tree1(Page):

    def is_displayed(self):
        return self.round_number == 1


class Tree2(Page):

    def is_displayed(self):
        return self.round_number == 1


class RLC_P1(Page):
    template_name = 'control2/Message.html'
    form_model = 'group'
    form_fields = ['send_message']

    def is_displayed(self):
        return self.player.id_in_group == 1 and (self.group.send_message == 'ask' or self.group.send_message is None)

    def send_message_choices(self):
        choices = [
                ['LC', 'Yo elijo ' + Constants.P1_codified_L],
                ['RC', 'Yo elijo ' + Constants.P1_codified_R]
        ]
        if not self.group.ask_used:
            choices.append(
                ['ask', 'Pida al otro participante que revele el lado de la figura que planean elegir por un costo de 5 puntos']
            )
        return choices

    def before_next_page(self):
        if self.group.send_message == 'ask':
            self.player.use_paid_message()


class Wait(WaitPage):
    pass


class RLC_P2(Page):
    template_name = 'control2/Message.html'
    form_model = 'group'
    form_fields = ['send_answer']

    def is_displayed(self):
        return self.player.id_in_group == 2 and (self.group.send_answer is None or self.group.send_answer =='ask')

    def send_answer_choices(self):
        choices = [
            ['LC', 'Yo elijo ' + Constants.P2_codified_L],
            ['RC', 'Yo elijo ' + Constants.P2_codified_R]
        ]
        if not self.group.ask_used:
            choices.append(
                ['ask', 'Pida al otro participante que revele el lado de la figura que planean elegir por un costo de 5 puntos']
            )
        return choices

    def before_next_page(self):
        if self.group.send_answer == 'ask':
            self.player.use_paid_message()


class YesNo_P1(Page):
    template_name = 'control2/YesNo.html'
    form_model = 'group'
    form_fields = ['ask_answer']

    def is_displayed(self):
        return self.player.id_in_group == 1 and self.group.ask_used and self.group.send_answer == 'ask'

    def before_next_page(self):
        if not self.group.ask_answer and self.group.ask_answer is not None:
            self.player.use_paid_message()


class YesNo_P2(Page):
    template_name = 'control2/YesNo.html'
    form_model = 'group'
    form_fields = ['ask_answer']

    def is_displayed(self):
        return self.player.id_in_group == 2 and self.group.ask_used and self.group.send_message == 'ask'

    def before_next_page(self):
        if not self.group.ask_answer and self.group.ask_answer is not None:
            self.player.use_paid_message()


class RL_P1(Page):
    template_name = 'control2/RL.html'
    form_model = 'group'
    form_fields = ['send_message']

    def is_displayed(self):
        return self.player.id_in_group == 1 and self.group.check_Ask()

    def send_message_choices(self):
        choices = [['L', 'Yo elijo'], ['R', 'Yo elijo']]
        return choices


class RL_P2(Page):
    template_name = 'control2/RL.html'
    form_model = 'group'
    form_fields = ['send_answer']

    def is_displayed(self):
        return self.player.id_in_group == 2 and self.group.check_Ask()

    def send_answer_choices(self):
        choices = [['L', 'Yo elijo'], ['R', 'Yo elijo']]
        return choices


class Decision(Page):
    form_model = 'player'
    form_fields = ['decision']

    def decision_choices(self):
        if self.player.id_in_group == 1:
            choices = [
                ['L',Constants.P1_codified_L],
                ['R',Constants.P1_codified_R]
            ]
        else:
            choices = [
                ['L', Constants.P2_codified_L],
                ['R', Constants.P2_codified_R]
            ]
        return choices


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoff()


class Results(Page):
    def vars_for_template(self):
        me = self.player
        opponent = me.other_player()
        fee = self.session.config['participation_fee']
        return {
            'my_decision': me.decision,
            'opponent_decision': opponent.decision,
            'same_choice': me.decision == opponent.decision
        }

    def app_after_this_page(self, upcoming_apps):
        if self.round_number == 2:
            return 'gamble'


class Quiz(Page):
    form_model = 'player'
    form_fields = ['question_1', 'question_2']

    def is_displayed(self):
        return self.round_number == 1

    def error_message(self, values):
        if values['question_1'] != 40 and values['question_2'] != 20:
            return 'Ambas preguntas son incorrectas'
        elif values['question_1'] == 40 and values['question_2'] != 20:
            return 'Pregunta 2 es incorrecta'
        elif values['question_1'] != 40 and values['question_2'] == 20:
            return 'Pregunta 1 es incorrecta'

page_sequence = [
    Introduction,
    Tree1,
    Tree2,
    Quiz,
    RLC_P1,
    Wait,
    YesNo_P2,
    RL_P2,
    Wait,
    RL_P1,
    Wait,
    RLC_P2,
    Wait,
    YesNo_P1,
    RL_P1,
    Wait,
    RL_P2,
    Wait,
    RLC_P1,
    Wait,
    RLC_P2,
    Wait,
    Decision,
    ResultsWaitPage,
    Results
]
