import pytest
from model.enums import *
from model.morpheme import Morpheme
from model.rootVerb import RootVerb
from model.nominalizer import Nominalizer
from model.word import Word
from database.mysql_repository import MysqlRepository
from app.services import Services


@pytest.fixture
def repo():
    return MysqlRepository()

@pytest.fixture
def services():
    return Services()

def test_parser_1(services):
    word_surface = 'vúvanpiš'
    components = services.parse_word(word_surface)
    print(str(components))

    expected_str = (
        "The definition is 'an insect that stings'. "
        "The root verb is 'vúvan' which means 'to hit'. This verb is transitive. "
        "The nominalizer is 'piš' which is a NMLZ.FUT and means 'event not yet occurred'."
    )

    assert str(components) == expected_str
    assert components.definition == 'an insect that stings'
    assert components.root == 'vúvan'
    assert components.root_gloss == 'to hit'
    assert components.transitivity == Transitivity.TRANSITIVE
    assert components.class1relationship == Class1Relationship.EVENT_NOT_YET_OCCURRED
    assert components.nominalizer == 'piš'
    assert components.nominalizer_gloss == 'NMLZ.FUT'


def test_parser_2(services):
    word_surface = 'ʔáminat'
    components = services.parse_word(word_surface)
    print(str(components))

    expected_str = (
        "The definition is 'the throwing or the orphan'. "
        "The root verb is 'ʔámin' which means 'to throw'. This verb is transitive. "
        "The nominalizer is 'at' which is a NMLZ.ABST and means 'verbal abstract noun'."
    )

    assert components.definition == 'the throwing or the orphan'
    assert components.root == 'ʔámin'
    assert components.root_gloss == 'to throw'
    assert components.transitivity == Transitivity.TRANSITIVE
    assert components.class1relationship == Class1Relationship.VERBAL_ABSTRACT_NOUN
    assert components.nominalizer == 'at'
    assert components.nominalizer_gloss == 'NMLZ.ABST'


def test_parser_3(services):
    word_surface = 'kʷáʔisniat'
    components = services.parse_word(word_surface)
    print(str(components))

    expected_str = (
        "The definition is 'the writing'. "
        "The root verb is 'kʷáʔisni' which means 'to write'. This verb is transitive. "
        "The nominalizer is 'at' which is a NMLZ.ABSTT and means 'verbal abstract noun'."
    )

    assert components.definition == 'the writing'
    assert components.root == 'kʷáʔisni'
    assert components.root_gloss == 'to write'
    assert components.transitivity == Transitivity.TRANSITIVE
    assert components.class1relationship == Class1Relationship.VERBAL_ABSTRACT_NOUN
    assert components.nominalizer == 'at'
    assert components.nominalizer_gloss == 'NMLZ.ABST'


def test_parser_4(services):
    word_surface = 'pívat'
    components = services.parse_word(word_surface)
    print(str(components))

    expected_str = (
        "The definition is 'tobacco'. "
        "The root verb is 'pívaʔ' which means 'to smoke'. This verb is intransitive. "
        "The nominalizer is 'at' which is a NMLZ.ABST and means 'verbal abstract noun'."
    )

    assert components.definition == 'tobacco'
    assert components.root == 'pívaʔ'
    assert components.root_gloss == 'to smoke'
    assert components.transitivity == Transitivity.INTRANSITIVE
    assert components.class1relationship == Class1Relationship.VERBAL_ABSTRACT_NOUN
    assert components.nominalizer == 'at'
    assert components.nominalizer_gloss == 'NMLZ.ABST'


def test_parser_5(services):
    word_surface = 'kʷáʔisniʔil̃'
    components = services.parse_word(word_surface)
    print(str(components))

    expected_str = (
        "The definition is 'the writing'. "
        "The root verb is 'kʷáʔisni' which means 'to write'. This verb is transitive. "
        "The nominalizer is 'ʔil̃' which is a NMLZ.ABST and means 'verbal abstract noun'."
    )

    assert components.definition == 'the writing'
    assert components.root == 'kʷáʔisni'
    assert components.root_gloss == 'to write'
    assert components.transitivity == Transitivity.TRANSITIVE
    assert components.class1relationship == Class1Relationship.VERBAL_ABSTRACT_NOUN
    assert components.nominalizer == 'ʔil̃'
    assert components.nominalizer_gloss == 'NMLZ.ABST'


def test_parser_6(services):
    word_surface = 'kúyil̃'
    components = services.parse_word(word_surface)
    print(str(components))

    expected_str = (
        "The definition is 'the burial'. "
        "The root verb is 'kúy' which means 'to bury'. This verb is transitive. "
        "The nominalizer is 'il̃' which is a NMLZ.ABST and means 'verbal abstract noun'."
    )

    assert components.definition == 'the burial'
    assert components.root == 'kúy'
    assert components.root_gloss == 'to bury'
    assert components.transitivity == Transitivity.TRANSITIVE
    assert components.class1relationship == Class1Relationship.VERBAL_ABSTRACT_NOUN
    assert components.nominalizer == 'il̃'
    assert components.nominalizer_gloss == 'NMLZ.ABST'


def test_parser_7(services):
    word_surface = 'ʔásniʔil̃'
    components = services.parse_word(word_surface)
    print(str(components))

    expected_str = (
        "The definition is 'the bathing, the bath'. "
        "The root verb is 'ʔásni' which means 'to bathe'. This verb is transitive. "
        "The nominalizer is 'ʔil̃' which is a NMLZ.ABST and means 'verbal abstract noun'."
    )

    assert components.definition == 'the bathing, the bath'
    assert components.root == 'ʔásni'
    assert components.root_gloss == 'to bathe'
    assert components.transitivity == Transitivity.TRANSITIVE
    assert components.class1relationship == Class1Relationship.VERBAL_ABSTRACT_NOUN
    assert components.nominalizer == 'ʔil̃'
    assert components.nominalizer_gloss == 'NMLZ.ABST'


def test_parser_8(services):
    word_surface = 'kúpvel'
    components = services.parse_word(word_surface)
    print(str(components))

    expected_str = (
        "The definition is 'the bed'. "
        "The root verb is 'kúp' which means 'to sleep'. This verb is intransitive. "
        "The nominalizer is 'vel' which is a NMLZ.PFV and means 'event not yet occurred'."
    )

    assert components.definition == 'the bed'
    assert components.root == 'kúp'
    assert components.root_gloss == 'to sleep'
    assert components.transitivity == Transitivity.INTRANSITIVE
    assert components.class1relationship == Class1Relationship.ALREADY_OCCURRING_OR_OCCURRED
    assert components.nominalizer == 'vel'
    assert components.nominalizer_gloss == 'NMLZ.PFV'


def test_parser_9(services):
    word_surface = 'yúmuvel'
    components = services.parse_word(word_surface)
    print(str(components))

    expected_str = (
        "The definition is 'the hat'. "
        "The root verb is 'yúmu' which means 'to put on the head'. This verb is transitive. "
        "The nominalizer is 'vel' which is a NMLZ.PFV and means 'already occurring or occurred'."
    )

    assert components.definition == 'the hat'
    assert components.root == 'yúmu'
    assert components.root_gloss == 'to put on the head'
    assert components.transitivity == Transitivity.TRANSITIVE
    assert components.class1relationship == Class1Relationship.ALREADY_OCCURRING_OR_OCCURRED
    assert components.nominalizer == 'vel'
    assert components.nominalizer_gloss == 'NMLZ.PFV'


def test_parser_10(services):
    word_surface = 'qáwivel'
    components = services.parse_word(word_surface)
    print(str(components))

    expected_str = (
        "The definition is 'handle'. "
        "The root verb is 'qáwi' which means 'to get tied'. This verb is transitive. "
        "The nominalizer is 'vel' which is a NMLZ.PFV and means 'event already occurring or occurred'."
    )

    assert components.definition == 'handle'
    assert components.root == 'qáwi'
    assert components.root_gloss == 'to get tied'
    assert components.transitivity == Transitivity.TRANSITIVE
    assert components.class1relationship == Class1Relationship.ALREADY_OCCURRING_OR_OCCURRED
    assert components.nominalizer == 'vel'
    assert components.nominalizer_gloss == 'NMLZ.PFV'


def test_parser_11(services):
    word_surface = 'čeŋenval'
    components = services.parse_word(word_surface)
    print(str(components))

    expected_str = (
        "The definition is 'dancing place'. "
        "The root verb is 'čeŋen' which means 'to dance'. This verb is transitive. "
        "The nominalizer is 'val' which is a NMLZ.LOC and means 'location or place'."
    )

    assert components.definition == 'dancing place'
    assert components.root == 'čeŋen'
    assert components.root_gloss == 'to dance'
    assert components.transitivity == Transitivity.TRANSITIVE
    assert components.class1relationship == Class1Relationship.LOCATION_OR_PLACE
    assert components.nominalizer == 'val'
    assert components.nominalizer_gloss == 'NMLZ.LOC'


