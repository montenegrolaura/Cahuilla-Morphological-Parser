import abc
from model.enums import *
from model.morpheme import Morpheme
from model.rootVerb import RootVerb
from model.nominalizer import Nominalizer

class Repository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def load_morphemes(self) -> list[Morpheme]:
        raise NotImplementedError

    @abc.abstractmethod
    def load_rootVerbs(self) -> list[RootVerb]:
        raise NotImplementedError

    @abc.abstractmethod
    def load_nominalizers(self) -> list[Nominalizer]:
        raise NotImplementedError

    @abc.abstractmethod
    def load_definitions(self, word_surface: str) -> str:
        raise NotImplementedError