from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants


class DemographicsPageOne(Page):
    form_model = 'player'
    form_fields = ['birthdate',                 # What's your birthdate?
                   'gender',                    # What's your gender?
                   'dominant_hand',             # What's your dominant hand?
                   'maternal_lang',             # What is your maternal language?
                   'dialect',                   # Do you identify as a speaker of a specific dialect of this language?
                   'other_langs',               # What other languages do you speak well?
                   'langs_used_weekly']         # What languages do you use at least once a week?

class DemographicsPageTwo(Page):
    form_model = 'player'
    form_fields = ['nationality',               # What is your nationality
                   'birthplace',                # Where were you born (city, province, country)
                   'residence',                 # Where do you reside (city, province, country)
                   'bool_country',              # Have you lived your entire life in the country where you were born?
                   'other_countries',]          # What other countries have you lived in -- should be dictionary [country, years]

class DemographicsPageThree(Page):
    form_model = 'player'
    form_fields = ['bool_student',              # Are you a student?
                   'profession',                # What is your profession?
                   'education_level',           # What is your education level?
                   'edu_countries',             # In which countries did you receive your education?
                   'edu_langs',                 # In what languages did you receive your education? (Allow specification)
                   'bool_phil_course',          # Have you taken a philosophy course?
                   'phil_course_count']         # How many philosophy courses have you taken?

class DemographicsPageFour(Page):
    form_model = 'player'
    form_fields = ['parents_edu_level',         # What is your parent's education level?
                   'religion',                  # What is your religion?
                   'rel_freq',                  # How often do you participate in relgious activities?
                   'rel_import',                # How important is religion in your life?
                   'politics']                  # What is your political inclination?

page_sequence = [
    DemographicsPageOne,
    DemographicsPageTwo,
    DemographicsPageThree,
    DemographicsPageFour
]
