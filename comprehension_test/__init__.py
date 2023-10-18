from otree.api import *


doc = """ """


class C(BaseConstants):
    NAME_IN_URL = 'comprehension_test'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    quiz1 = models.BooleanField(label="公共財に貢献された総ポイントが0.2倍されたものが各プレイヤーに還元される")
    quiz2 = models.StringField(
        label='N期目開始時に500ポイント保有しており、自身のその期における貢献額を400ポイントとした。公共財に1000ポイント集まった場合、その期の利得は',
        choices=['400ポイント', '500ポイント', '600ポイント'],
    )
    quiz3 =models.StringField(
        label='カタストロフが発生した期の終わりに各プレイヤーの利得がーー倍される',
        choices=['0.2', '0.4', '0.5'],
    )
    quiz4 = models.BooleanField(label="このゲームは十期繰り返しで行われる")


class TEST_1(Page):
    form_model = 'player'
    form_fields = ['quiz1', 'quiz2', 'quiz3', 'quiz4']

    @staticmethod
    def error_message(player: Player, values):
        solutions = dict(quiz1=False, quiz2='600ポイント', quiz3='0.4', quiz4=True)
        errors = {f: 'Wrong' for f in solutions if values[f] != solutions[f]}
        if errors:
            return errors



class Results(Page):
    pass


class ResultsWaitPage(WaitPage):
    pass


page_sequence = [TEST_1, Results, ResultsWaitPage]


