from enum import Enum

class PartsOfSpeech(Enum):
    NOUN = 1
    VERB = 2
    SUFF = 3

class Transitivity(Enum):
    TRANSITIVE = 1
    INTRANSITIVE = 2


class Class1Relationship(Enum):
    VERBAL_ABSTRACT_NOUN = 1
    EVENT_NOT_YET_OCCURRED = 2
    ALREADY_OCCURRING_OR_OCCURRED = 3
    LOCATION_OR_PLACE = 4