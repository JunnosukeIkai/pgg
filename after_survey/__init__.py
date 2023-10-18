from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'after_survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    gender = models.StringField(
        label = "性別",
        choices = ['女性', '男性', 'その他'], blank=True
        )
    age = models.IntegerField(label = "年齢",unit = "歳")
    birthplace = models.StringField(
        label = "出身地",
        choices = ['北海道','青森県','岩手県','宮城県','秋田県','山形県','福島県','茨城県','栃木県','群馬県','埼玉県',
        '千葉県','東京都','神奈川県','山梨県','長野県','新潟県','富山県','石川県','福井県' ,'岐阜県','静岡県','愛知県','三重県',
        '滋賀県','京都府','大阪府','兵庫県','奈良県','和歌山県','鳥取県','島根県','岡山県','広島県','山口県', 
        '徳島県','香川県','愛媛県','高知県','福岡県','佐賀県','長崎県','熊本県','大分県','宮崎県','鹿児島県','沖縄県'],
    )
    comment = models.LongStringField(initial=None, verbose_name='実験について感想やコメントがあれば、ご自由にお書きください。')

# PAGES
class Survey(Page):
    form_model = 'player'
    form_fields = ['gender','age','birthplace','comment']

class Results(Page):
    pass


page_sequence = [Survey, Results]
