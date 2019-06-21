from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    intent = models.StringField(
        choices=['Interesado','Generoso','Hóstil','Cooperativo','Racional','Irracional'],
        label='¿Cuál crees que fue la intención del otro jugador en sus decisiones?',
        widget=widgets.RadioSelect)

    identity = models.StringField(
        choices=['Sí','No','Quizás'],
        label='Si supieras la identidad del otro jugador, ¿habrías tomado una decisión diferente?',
        widget=widgets.RadioSelect)

    risker = models.StringField(
        choices=['0 Nada preparado para tomar riesgos','1','2','3','4','5','6','7','8','9','10 Preparado para tomar riesgos'],
        label='¿Cómo te calificarías personalmente? En general, ¿Te consideras alguien preparado para tomar riesgos o tratas de evitarlos?',
        widget=widgets.RadioSelect)

