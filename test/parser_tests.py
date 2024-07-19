import pytest
from model.parser import MorphologicalParser

NOMINALIZERS = {
    'vel': 'nominalizer showing event already occurred',
    'ʔil̃': 'nominalizer that makes abstract verbs into nouns',
    'at': 'nominalizer that makes abstract verbs into nouns',
    'piš': 'nominalizer that indicates something has not yet occurred'
}

ROOTS = {
    'vúvan': 'hit',
    'kúp': 'sleep',
    'kʷáʔisni': 'write',
    'ʔámin': 'throw'
}

parser = MorphologicalParser(ROOTS, NOMINALIZERS)

def test_1():
    word = 'vúvan–piš'
    expected = {
        'root': [('vúvan', 'hit')],
        'nominalizers': [('piš', 'nominalizer that indicates something has not yet occurred')]
    }
    result = parser.parse(word)
    print(result)
    assert parser.parse(word) == expected

def test_2():
    word = 'kúp–vel'
    expected = {
        'root': [('kúp',  'sleep')],
        'nominalizers': [('vel', 'nominalizer showing event already occurred')]
    }
    results = parser.parse(word)
    print(results)
    assert results == expected

def test_3():
    word = 'kʷáʔisni–ʔil̃'
    expected = {
        'root': [('kʷáʔisni', 'write')],
        'nominalizers': [('ʔil̃', 'nominalizer that makes abstract verbs into nouns')]
    }
    results = parser.parse(word)
    print(results)
    assert results == expected

def test_4():
    word = 'ʔámin–at'
    expected = {
        'root': [('ʔámin', 'throw')],
        'nominalizers': [('at', 'nominalizer that makes abstract verbs into nouns')]
    }
    results = parser.parse(word)
    print(results)
    assert results == expected
