# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-04-29 18:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import otree.db.models
import otree_save_the_change.mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('otree', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_subsession', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('send_message', otree.db.models.StringField(choices=[['L', 'the Left side'], ['R', 'the Right side'], ['LC', '#'], ['RC', '@'], ['ask', 'A']], max_length=10000, null=True)),
                ('send_answer', otree.db.models.StringField(choices=[['L', 'the Left side'], ['R', 'the Right side'], ['LC', '&'], ['RC', '*'], ['ask', 'A']], max_length=10000, null=True)),
                ('ask_used', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
                ('ask_answer', otree.db.models.BooleanField(choices=[[True, 'Yes'], [False, 'No']], verbose_name='Your answer:')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='control2_group', to='otree.Session')),
            ],
            options={
                'db_table': 'control2_group',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_group', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_payoff', otree.db.models.CurrencyField(default=0, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_gbat_arrived', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
                ('_gbat_grouped', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
                ('decision', otree.db.models.StringField(choices=[('L', 'L'), ('R', 'R')], max_length=10000, null=True)),
                ('paid_msg', otree.db.models.IntegerField(default=0, null=True)),
                ('question_1', otree.db.models.IntegerField(null=True, verbose_name='Suppose that you are First Person, and that you select your right symbol, what would be your payout if Second Person also chooses their right symbol?')),
                ('question_2', otree.db.models.IntegerField(null=True, verbose_name='Suppose that you are Second Person, you select your right symbol, what would be your payout if the First Person chooses their left symbol?')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='control2.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='control2_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='control2_player', to='otree.Session')),
            ],
            options={
                'db_table': 'control2_player',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='control2_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'control2_subsession',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.AddField(
            model_name='player',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control2.Subsession'),
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control2.Subsession'),
        ),
    ]
