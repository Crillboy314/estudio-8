from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c
)

doc = """
This is a decision-making activity that includes messages with a common dictionary. 
Two participants are asked separately whether they want option A or option B. Their choices directly determine the
payoffs to each of the participants.
"""


class Constants(BaseConstants):
    name_in_url = 'control1'
    players_per_group = 2
    num_rounds = 1

    # Payoffs depending on the situation

    YouA_OpponentB_payoff = c(70)
    YouB_OpponentA_payoff = c(20)

    both_B_payoff = c(40)
    both_A_payoff = c(10)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    send_message = models.StringField(
        label="Que mensaje le quiere mandar a la Persona 2?",
        choices=[
            ['A', 'Yo elijo A'],
            ['B', 'Yo elijo B']
        ],
        widget=widgets.RadioSelect
    )
    send_answer = models.StringField(
        label="Que mensaje le quiere mandar a la Persona 1?",
        choices=[
            ['A', 'Yo elijo A'],
            ['B', 'Yo elijo B']
        ],
        widget=widgets.RadioSelect
    )


class Player(BasePlayer):
    decision = models.StringField(
        choices=['A', 'B'],
        doc="""This player's decision""",
        widget=widgets.RadioSelect
    )

    def other_player(self):
        return self.get_others_in_group()[0]

    def set_payoff(self):
        payoff_matrix = {
            'A':
                {
                    'A': Constants.both_A_payoff,
                    'B': Constants.YouA_OpponentB_payoff
                },
            'B':
                {
                    'A': Constants.YouB_OpponentA_payoff,
                    'B': Constants.both_B_payoff
                }
        }

        self.payoff = payoff_matrix[self.decision][self.other_player().decision]

    question_1 = models.IntegerField(
        label="Suponga que usted es la Primera Persona, y que selecciona B, ¿cuál sería su pago si la Segunda Persona "
              "también elige B?",
        min=10, max=70)

    question_2 = models.IntegerField(
        label="Suponga que usted es la Segunda Persona, y selecciona B, ¿cuál sería su pago si la Primera Persona "
              "elige A?",
        min=10, max=70)
