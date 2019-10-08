from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c
)

import random


doc = """
This is a decision-making activity. Two participants send messages and are asked separately
whether they want option A or option B with different symbols. Their choices directly determine the
payoffs to each of the participants.
"""


class Constants(BaseConstants):
    name_in_url = 'control2trial'
    players_per_group = 2
    num_rounds = 1

    endowment = c(5)
    message_cost = c(5)
    
    instructions_template = 'control2trial/Instructions.html'

    # Payoffs depending on the situation

    YouL_OpponentR_payoff = c(70)
    YouR_OpponentL_payoff = c(20)

    both_R_payoff = c(40)
    both_L_payoff = c(10)

    # Characters for codified messages
    P1_codified_R = '@'
    P1_codified_L = '#'
    P2_codified_R = '*'
    P2_codified_L = '&'

    Bot_codified_R = '%'
    Bot_codified_L = '^'

    payoff_matrix = {
        'L':
            {
                'L': both_L_payoff,
                'R': YouL_OpponentR_payoff
            },
        'R':
            {
                'L': YouR_OpponentL_payoff,
                'R': both_R_payoff
            }
    }


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            #p.pNum = random.choice([1, 2])
            p.pNum = p.id_in_group


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pNum = models.IntegerField()

    bot_decision = models.StringField(
        choices=[['L', Constants.Bot_codified_L], ['R', Constants.Bot_codified_R]],
        doc="""This player's bot decision""",
        widget=widgets.RadioSelect
    )

    def set_payoff(self):
        self.trial_payoff = Constants.payoff_matrix[self.decision][self.bot_decision] + Constants.endowment - self.paid_msg * Constants.message_cost

    def check_Ask(self):
        N = self.send_message == 'ask' or self.send_answer == 'ask'
        Y = self.ask_used and self.ask_answer
        return N and Y

    ask_used = models.BooleanField(initial=False)

    ask_answer = models.BooleanField(
        choices=[
            [True, 'Sí'],
            [False, 'No']
        ],
        widget=widgets.RadioSelect,
        label="Tu respuesta:"
    )
    send_answer = models.StringField(
        # label = "What option do you want the participant A to think you will chose?",
        choices=[
            ['L', 'el lado izquierdo'],
            ['R', 'el lado derecho'],
            ['LC', Constants.P2_codified_L],
            ['RC', Constants.P2_codified_R],
            ['ask', 'A']
        ],
        widget=widgets.RadioSelect
    )

    send_message = models.StringField(
        # label = "What option do you want the participant B to think you will chose?",
        choices=[
            ['L', 'el lado izquierdo'],
            ['R', 'el lado derecho'],
            ['LC', Constants.P1_codified_L],
            ['RC', Constants.P1_codified_R],
            ['ask', 'A']
        ],
        widget=widgets.RadioSelect
    )
    bot_answer = models.StringField(
        choices=[
            ['L', 'el lado izquierdo'],
            ['R', 'el lado derecho'],
            ['LC', Constants.Bot_codified_L],
            ['RC', Constants.Bot_codified_R],
            ['ask', 'A']
        ]
    )

    def rand_send_messageRLC(self):
        if not self.ask_used:
            self.send_message = random.choice(['LC', 'RC', 'ask'])
        else:
            self.send_message = random.choice(['LC', 'RC'])
        self.bot_answer = self.send_message

    def rand_send_messageRL(self):
        self.send_message = random.choice(['L', 'R'])

    def rand_send_answerRLC(self):
        if not self.ask_used:
            self.send_answer = random.choice(['LC', 'RC', 'ask'])
        else:
            self.send_answer = random.choice(['LC', 'RC'])
        self.bot_answer = self.send_answer

    def bot_result(self):
        self.bot_decision = random.choice(['L', 'R'])

    def rand_send_answerRL(self):
        self.send_answer = random.choice(['L', 'R'])

    def rand_ask_answer(self):
        self.ask_answer = random.choice([True, False])

    decision = models.StringField(
        choices=['L', 'R'],
        doc="""This player's decision""",
        widget=widgets.RadioSelect
    )
    paid_msg = models.IntegerField(initial=0)
    trial_payoff = models.CurrencyField(initial=0)

    def use_paid_message(self):
        self.paid_msg += 1
        self.ask_used = True
        return self.payoff

    question_1 = models.IntegerField(
        label="Suponga que usted es la Primera Persona, y que selecciona el símbolo de la derecha, ¿cuál sería su pago "
              "si la Segunda Persona también elige el símbolo de la derecha?",
        min=10, max=70)

    question_2 = models.IntegerField(
        label="Suponga que usted es la Segunda Persona, y selecciona el símbolo de la derecha, ¿cuál sería su pago si "
              "la Primera Persona elige el símbolo de la izquierda?",
        min=10, max=70)
