from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


doc = """
This is a decision-making activity. Two participants are asked separately
whether they want option A or option B. Their choices directly determine the
payoffs to each of the participants.
"""



class Constants(BaseConstants):
    name_in_url = 'control'
    players_per_group = 2
    num_rounds = 2

    instructions_template = 'control/Instructions.html'

    #Payoffs depending on the situation

    YouA_OpponentB_payoff = c(70)
    YouB_OpponentA_payoff = c(20)


    both_B_payoff = c(40)
    both_A_payoff = c(10)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    decision = models.StringField(
        choices=['A', 'B'],
        doc="""This player's decision""",
        widget=widgets.RadioSelect
    )

    trial_payoff = models.CurrencyField(initial=0)

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

        if self.round_number == 1:
            self.trial_payoff = payoff_matrix[self.decision][self.other_player().decision]
        else:
            self.payoff = payoff_matrix[self.decision][self.other_player().decision]

    question_1 = models.IntegerField(
        label = "Suponga que usted es la Primera Persona, y que selecciona B, ¿cuál sería su pago si la Segunda Persona también elige B?",
        min=10,max=70)

    question_2 = models.IntegerField(
        label = "Suponga que usted es la Segunda Persona, y selecciona B, ¿cuál sería su pago si la Primera Persona elige A?",
        min=10,max=70)
