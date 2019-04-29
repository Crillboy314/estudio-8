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
        label='What is your age?',
        min=13, max=125)

    gender = models.StringField(
        choices=['Male', 'Female', 'Other'],
        label='What is your gender?',
        widget=widgets.RadioSelect)

    education = models.StringField(
        choices=['No schooling','Primary School','Middle School','High School',
        'Some College','Trade/Technical/Vocational Training','Associate Degree',
        'Bachelor\'s Degree','Master\'s Degree','Doctorate'],
        label='What is your highest level of education attained?',
        widget=widgets.RadioSelect)

    intent = models.StringField(
        choices=['Selfish','Generous','Hostile','Cooperative','Rational','Irrational'],
        label='What do you think the intent of the other player was in their decisions?',
        widget=widgets.RadioSelect)

    identity = models.StringField(
        choices=['Yes','No','Maybe'],
        label='If you knew the identity of the other player, would you have made a different decision?',
        widget=widgets.RadioSelect)