from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

class Constants(BaseConstants):
    name_in_url = 'survey2'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):

    birthdate = models.StringField(
        label='¿Cuál es su fecha de nacimiento? Por favor, use el formato día-mes-año (por ejemplo, 30-01-1998).',
        widget=widgets.DateInput)

    gender = models.StringField(
        choices=['Masculino', 'Femenino', 'Otro'],
        label='¿Cuál es su género?',
        widget=widgets.RadioSelect)

    maternal_lang = models.StringField(
        label='¿Cuál es su idioma materno?',
        widget=widgets.TextInput)

    dialect = models.StringField(
        label='Se identifica usted como hablante de un dialecto particular o variedad de este idioma (o idiomas)? ¿En caso afirmativo, como se llama ese dialecto o en dónde se habla?',
        widget=widgets.TextInput)

    other_langs = models.StringField(
        label='¿Qué otros idiomas habla bien?',
        widget=widgets.TextInput)

    langs_used_weekly = models.StringField(
        label='¿Qué idiomas (incluyendo sus idiomas maternos y el Castellano) usa al menos una vez a la semana?',
        widget=widgets.TextInput)

    nationality = models.StringField(
        label='¿Cuál es su nacionalidad?',\
        widget=widgets.TextInput)

    birthplace = models.StringField(
        label='¿Donde nació usted? (Ciudad, Provincia/Estado, País)',
        widget=widgets.TextInput)

    residence = models.StringField(
        label='¿En qué país reside?',
        widget=widgets.TextInput)

    bool_country = models.StringField(
        choices=['Sí','No'],
        label='¿Ha vivido toda su vida en el país en el que nació?',
        widget=widgets.RadioSelect)

    other_countries = models.StringField(
        label='Si ha vivido en otros países además de aquel en que nació, por favor indique en cuáles señalando cuántos años vivió en cada uno. Use el siguiente formato: EEUU, 4, Francia, 2, Chile, 1, etc.',
        widget=widgets.TextInput)

    bool_student = models.StringField(
        choices=['Sí','No'],
        label='¿Es usted estudiante?',
        widget=widgets.RadioSelect)

    profession = models.StringField(
        label='Si usted no es estudiante, ¿cuál es su profesión? Si es estudiante, escriba \'NA\' en la caja',
        widget=widgets.TextInput)

    education_level = models.StringField(
        choices=['Ningún','Educación Inicial (Jardín)','Educación General Básica (Primaria)','Bachillerato (Secundaria)',
        'Algunos estudios universitarios','Instituto','Licenciatura o equivalente',
        'Maestría o equivalente','Doctorado'],
        label='¿Cuál es su nivel educativo?',
        widget=widgets.RadioSelect)

    edu_countries = models.StringField(
        label='¿En que países recibió su educación?',
        widget=widgets.TextInput)

    edu_langs = models.StringField(
        label='¿En que idiomas recibió su educación? Por favor especifique.',
        widget=widgets.TextInput)

    phil_course_count = models.StringField(
        choices=['Nunca he tomado un curso de Filosofía',
                 'He tomado 1 o 2 cursos de Filosofía',
                 'He tomado más de 2 cursos de Filosofía, pero la Filosofía no es la disciplina en la que fui formado.',
                 'Estudio Filosofía y estoy por obtener una licenciatura en Filosofía.',
                 'Estudio Filosofía y tengo una licenciatura en Filosofía.',
                 'Estoy estudiando un posgrado en Filosofía.',
                 'Tengo un doctorado en Filosofía'],
        label='¿Cuántos cursos de Filosofía recibió durante sus estudios?',
        widget=widgets.RadioSelect)

    parents_edu_level = models.StringField(
        choices=['Ningún','Educación Inicial (Jardín)','Educación General Básica (Primaria)','Bachillerato (Secundaria)',
        'Algunos estudios universitarios','Instituto','Licenciatura o equivalente',
        'Maestría o equivalente','Doctorado'],
        label='Hasta donde sabe, ¿cuál es el nivel educativo más alto que alcanzó alguno de sus padres (el que tenga más estudios)?',
        widget=widgets.RadioSelect)

    religion = models.StringField(
        choices=['Ninguna','Católica','Evangelista','Protestante (distinto de evangelista)',
                 'Mormona','Cristiana ortodoxa','Cristiana (otra)','Judía','Musulmana',
                 'Hinduísta','Budista','Sintoísta','Confucionista','Daoista','Jainista',
                 'Sikh','Atea o agnóstica','Otra'],
        label='¿Cuál es su afiliación religiosa actual? Por favor marque todas las opciones aplicables.	',
        widget=widgets.RadioSelect)

    rel_freq = models.StringField(
        choices=['Diariamente','Semanalmente','Mensualmente','Unas cuantas veces al año','Nunca'],
        label='¿Con qué frecuencia participa en actividades religiosas?',
        widget=widgets.RadioSelect)

    rel_import = models.StringField(
        choices=['No es importante en absoluto','Un poco importante','Algo importante','Importante','Muy importante'],
        label='¿Qué tan importante es la religión en su vida?',
        widget=widgets.RadioSelect)

    politics = models.StringField(
        choices=['Muy de izquierda','Izquierda','Centro-izquierda','Centro','Centro-derecha','Derecha','Muy de derecha'],
        label='En términos generales, ¿cuál es su inclinación política?',
        widget=widgets.RadioSelect)
