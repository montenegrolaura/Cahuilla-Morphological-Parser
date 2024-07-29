import pytest
from model.enums import *
from model.morpheme import Morpheme
from model.rootVerb import RootVerb
from model.nominalizer import Nominalizer
from model.word import Word
from model.parser import MorphologicalParser
from database.mysql_repository import MysqlRepository


@pytest.fixture
def repo():
    return MysqlRepository()

@pytest.fixture
def parser(repo):
    return MorphologicalParser(repository=repo)

def test_morphological_parser(parser):
    word = Word(surface_form="vúvanpiš", definition='an insect that stings')

    components = parser.parse(word)

    assert components['root'] == 'vúvan'
    assert components['root_gloss'] == 'to hit'
    assert components['nominalizer'] == 'piš'
    assert components['nominalizer_gloss'] == 'NMLZ.FUT'




