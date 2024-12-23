from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'publicgoodsgame'
    PLAYERS_PER_GROUP = 4
    NUM_ROUNDS = 10
    ENDOWMENT = 500
    MULTIPLIER = 2


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
   contribution = models.IntegerField(min=0)
   prev_payoff = models.CurrencyField() 
   total_payoff = models.CurrencyField()
   payoff_pre = models.CurrencyField()


def contribution_max(player):
    if player.round_number == 1:
        return C.ENDOWMENT
    else:
        prev_payoff  =  player.in_round(player.round_number - 1).payoff
        return prev_payoff


def set_payoff(group):
    players = group.get_players()  
    contributions = [p.contribution for p in players]
    group.total_contribution = sum(contributions)
    group.individual_share = group.total_contribution * C.MULTIPLIER / C.PLAYERS_PER_GROUP
    for player in players:
        if group.round_number == 1:
            player.payoff = C.ENDOWMENT - player.contribution + group.individual_share
        else:
            player.prev_payoff  =  player.in_round(player.round_number - 1).payoff
            player.payoff = player.prev_payoff - player.contribution + group.individual_share
            player.total_payoff = player.prev_payoff + player.payoff

# PAGES

class Instraction(Page):
    def is_displayed(player: Player):
        return player.round_number == 1


class Contribute(Page):
    form_model = 'player'
    form_fields = ['contribution']

    @staticmethod 
    def vars_for_template(player: Player): 
        if player.round_number != 1:
            rval = {} 
            rval['prev_payoff'] =  player.in_round(player.round_number - 1).payoff
            return rval


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoff'

class Results(Page):

    @staticmethod 
    def vars_for_template(player: Player): 
        if player.round_number != 1:
            rval = {} 
            rval['prev_payoff'] =  player.in_round(player.round_number - 1).payoff
            return rval

class Rink(Page):
    def is_displayed(player: Player):
        return player.round_number == 10
    



page_sequence = [Instraction, 
                  Contribute,
                  ResultsWaitPage,
                  Results,
                  Rink]
