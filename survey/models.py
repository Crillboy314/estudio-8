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

    age = models.IntegerField(
       label='¿Qué edad tiene usted?',
      min=13, max=125)

    gender = models.StringField(
        choices=['Masculino', 'Femenino', 'Otro'],
        label='¿Qué es su género de usted?',
        widget=widgets.RadioSelect)

    education = models.StringField(
       choices=['Ningún','Educación Inicial (Jardín)','Educación General Básica (Primaria)','Bachillerato (Secundaria)',
        'Algunos estudios universitarios','Instituto','Licenciatura o equivalente',
        'Maestría o equivalente','Doctorado'],
        label='¿Cuál es su nivel educativo?',
        widget=widgets.RadioSelect)

    intent = models.StringField(
        choices=['Interesado','Generoso','Hostil','Cooperativo','Racional','Irracional'],
        label='¿Qué crees que fue su intención del otro jugador en sus decisiones?',
        widget=widgets.RadioSelect)

    identity = models.StringField(
        choices=['Sí','No','Quizás'],
        label='Si supieras la identidad del otro jugador, ¿habrías tomado una decisión diferente?',
        widget=widgets.RadioSelect)

    risker = models.StringField(
        choices=[' 0 Nada preparado para tomar riesgo','1','2','3','4','5','6','7','8','9','10 Preparado para tomar riesgo'],
        label='Como te calificarías personalmente ? En general, Te consideras alguien preparado para tomar riesgo?',
        widget=widgets.RadioSelect)