import pytest
from model.enums import *
from model.rootVerb import RootVerb
from model.nominalizer import Nominalizer
from model.morpheme import Morpheme
from database.mysql_repository import MysqlRepository

@pytest.fixture
def repo():
    return MysqlRepository()

def test_load_morphemes(repo):
    morphemes = repo.load_morphemes()
    assert len(morphemes) > 0
    assert isinstance(morphemes[0], Morpheme)

def test_load_rootVerbs(repo):
    root_verbs = repo.load_rootVerbs()
    assert len(root_verbs) > 0
    assert isinstance(root_verbs[0], RootVerb)
    assert root_verbs[0].transitivity in [Transitivity.TRANSITIVE, Transitivity.INTRANSITIVE]

def test_load_nominalizers(repo):
    nominalizers = repo.load_nominalizers()
    assert len(nominalizers) > 0
    assert isinstance(nominalizers[0], Nominalizer)
    assert nominalizers[0].class1_relationship in [
        Class1Relationship.VERBAL_ABSTRACT_NOUN,
        Class1Relationship.EVENT_NOT_YET_OCCURRED,
        Class1Relationship.ALREADY_OCCURRING_OR_OCCURRED,
        Class1Relationship.LOCATION_OR_PLACE
    ]