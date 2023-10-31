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
    question1 = models.StringField(
        label = "性別",
        choices = ['女性', '男性', 'その他'], blank=True
        )
    question2 = models.StringField(
        label = "出身地",
        choices = ['北海道','青森県','岩手県','宮城県','秋田県','山形県','福島県','茨城県','栃木県','群馬県','埼玉県',
        '千葉県','東京都','神奈川県','山梨県','長野県','新潟県','富山県','石川県','福井県' ,'岐阜県','静岡県','愛知県','三重県',
        '滋賀県','京都府','大阪府','兵庫県','奈良県','和歌山県','鳥取県','島根県','岡山県','広島県','山口県', 
        '徳島県','香川県','愛媛県','高知県','福岡県','佐賀県','長崎県','熊本県','大分県','宮崎県','鹿児島県','沖縄県'],
    )
    question3 = models.StringField(
        label = "現在の住まい",
        choices = ['一人暮らし', '実家暮らし'], blank=True
        )
    question4 = models.StringField(
        label = "被災経験の有無",
        choices = ['あり', 'なし'], blank=True
        )
    question5 = models.StringField(
        label = "地域の避難訓練の参加経験(学校を除く)",
        choices = ['あり', 'なし'], blank=True
        )
    question6 = models.StringField(
        label = "防災情報の収集(アプリやポータルサイト等の活用)",
        choices = ['あり', 'なし'], blank=True
        )
    question7 = models.StringField(
        label = "自宅で行っている災害対策の有無(備蓄や家具の固定など)",
        choices = ['あり', 'なし'], blank=True
        )
    question10 = models.LongStringField(initial=None, verbose_name='実験について感想やコメントがあれば、ご自由にお書きください。',
    blank =True
    )

# PAGES
class Instruction(Page):
    pass


class Survey(Page):
    form_model = 'player'
    form_fields = ['question1','question2','question3','question4','question5','question6','question7']

class Survey2(Page):
    form_model = 'player'
    form_fields = ['question10']


class Results(Page):
    pass


page_sequence = [Instruction, Survey,Survey2,Results]
