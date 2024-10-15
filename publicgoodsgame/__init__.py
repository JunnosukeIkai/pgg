from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'publicgoodsgame'
    PLAYERS_PER_GROUP = 4
    NUM_ROUNDS = 5
    ENDOWMENT = 10
    MULTIPLIER = 1.6


class Subsession(BaseSubsession):
    def creating_session(subsession):
        if subsession.round_number == 1:
            subsession.group_randomly()
        else:
            subsession.group_like_round(1)


class Group(BaseGroup):
    total_contribution = models.FloatField()
    individual_share = models.FloatField()



class Player(BasePlayer):
   contribution = models.IntegerField(min=0, max=10)
   total_payoff = models.CurrencyField()


def set_payoff(group):
    players = group.get_players()  
    contributions = [p.contribution for p in players]
    group.total_contribution = sum(contributions)
    group.individual_share = group.total_contribution * C.MULTIPLIER / C.PLAYERS_PER_GROUP
    for p in players :
        if group.round_number == 5:
            p.payoff = C.ENDOWMENT - p.contribution + group.individual_share
            p.total_payoff = p.payoff + p.in_round(p.round_number-1).payoff + p.in_round(p.round_number-2).payoff + p.in_round(p.round_number-3).payoff + p.in_round(p.round_number-4).payoff           
        else:
            p.payoff = C.ENDOWMENT - p.contribution + group.individual_share


class Instraction(Page):
    def is_displayed(player: Player):
        return player.round_number == 1


class Contribute(Page):
    form_model = 'player'
    form_fields = ['contribution']


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoff'


class Results(Page):
    def is_displayed(player: Player):
        return player.round_number != 5

class Results5(Page):
    def is_displayed(player: Player):
        return player.round_number == 5


page_sequence = [Instraction, 
                  Contribute,
                  ResultsWaitPage,
                  Results,
                  Results5]
