from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'ending'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class EndPage(Page):
    pass


page_sequence = [EndPage]
