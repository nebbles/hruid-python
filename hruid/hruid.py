import random
from .adjectives import adjectives
from .nouns import nouns
from .verbs import verbs
from .adverbs import adverbs


def random_number():
    return str(random.randint(2, 33))


def random_adjective():
    return random.choice(adjectives)


def random_noun():
    return random.choice(nouns)


def random_verb():
    return random.choice(verbs)


def random_adverb():
    return random.choice(adverbs)


class Generator:
    def __init__(
        self,
        delimeter="-",
        use_number=True,
        use_adjective=True,
        use_noun=True,
        use_verb=True,
        use_adverb=True,
    ):
        self.delimeter = delimeter
        self.use_number = use_number
        self.use_adjective = use_adjective
        self.use_noun = use_noun
        self.use_verb = use_verb
        self.use_adverb = use_adverb

    def random(self):
        phrase_items = []
        if self.use_number:
            phrase_items.append(random_number())
        if self.use_adjective:
            phrase_items.append(random_adjective())
        if self.use_noun:
            phrase_items.append(random_noun())
        if self.use_verb:
            phrase_items.append(random_verb())
        if self.use_adverb:
            phrase_items.append(random_adverb())

        return self.delimeter.join(phrase_items)
