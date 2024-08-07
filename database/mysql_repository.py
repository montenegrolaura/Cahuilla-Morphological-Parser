from .repository import Repository
import mysql.connector
from mysql.connector import Error
from model.enums import PartsOfSpeech, Transitivity, Class1Relationship
from model.morpheme import Morpheme
from model.rootVerb import RootVerb
from model.nominalizer import Nominalizer


class MysqlRepository(Repository):

    def __init__(self):
        super().__init__()
        config = {
            'user': 'root',
            'password': 'rootpassword',
            'host': 'localhost', # to run LOCALLY, this should be localhost
            'port': '3306', # to run LOCALLY, this should be 32000
            'database': 'cahuilla'
        }
        try:
            self.connection = mysql.connector.connect(**config)
            self.cursor = self.connection.cursor()
        except Error as e:
            print(f"Error: {e}")
            self.connection = None
            self.cursor = None


    def __del__(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

    def map_pos(self, pos: str) -> PartsOfSpeech:
        pos_switcher = {'noun': PartsOfSpeech.NOUN,
                        'verb': PartsOfSpeech.VERB,
                        'SUFF': PartsOfSpeech.SUFF,}
        return pos_switcher.get(pos, None)

    def map_transitivity(self, transitivity: str) -> Transitivity:
        transitivity_switcher = {'transitive': Transitivity.TRANSITIVE,
                               'intransitive': Transitivity.INTRANSITIVE}
        return transitivity_switcher.get(transitivity, None)

    def map_nominalizer(self, relationship: str) -> Class1Relationship:
        nominalizer_switcher = {'verbal abstract noun': Class1Relationship.VERBAL_ABSTRACT_NOUN,
                                'event not yet occurred': Class1Relationship.EVENT_NOT_YET_OCCURRED,
                                'already occurring or occurred': Class1Relationship.ALREADY_OCCURRING_OR_OCCURRED,
                                'location or place': Class1Relationship.LOCATION_OR_PLACE}
        return nominalizer_switcher.get(relationship, None)


    def load_morphemes(self) -> list[Morpheme]:
        sql = 'SELECT canonicalForm, gloss, pos FROM morpheme'
        self.cursor.execute(sql)
        entries = [{'canonicalForm': canonicalForm,
                    'gloss': gloss,
                    'pos': pos,
                    } for (canonicalForm, gloss, pos) in self.cursor]
        morphemes = [Morpheme(entry['canonicalForm'], entry['gloss'], self.map_pos(entry['pos'])) for entry in entries]
        return morphemes


    def load_rootVerbs(self) -> list[RootVerb]:
        sql = 'SELECT m.canonicalForm, m.gloss, m.pos, rv.transitivity FROM morpheme m JOIN rootVerb rv ON m.id = rv.id'
        self.cursor.execute(sql)
        entries = [{'canonicalForm': canonicalForm,
                    'gloss': gloss,
                    'pos': pos,
                    'transitivity': Transitivity,
                    } for (canonicalForm, gloss, pos, Transitivity) in self.cursor]
        rootVerbs = [RootVerb(entry['canonicalForm'], entry['gloss'], self.map_pos(entry['pos']), self.map_transitivity(entry['transitivity'])) for entry in entries]
        return rootVerbs


    def load_nominalizers(self) -> list[Nominalizer]:
        sql = 'SELECT m.canonicalForm, m.gloss, m.pos, n.class1Relationship FROM morpheme m JOIN nominalizer n ON m.id = n.id'
        self.cursor.execute(sql)
        entries = [{'canonicalForm': canonicalForm,
                    'gloss': gloss,
                    'pos': pos,
                    'class1Relationship': Class1Relationship
                    } for (canonicalForm, gloss, pos, Class1Relationship) in self.cursor]
        nominalizers = [Nominalizer(entry['canonicalForm'], entry['gloss'], self.map_pos(entry['pos']), self.map_nominalizer(entry['class1Relationship'])) for entry in entries]
        return nominalizers

    def load_definitions(self, word_surface: str) -> str:
        sql = 'SELECT definition FROM definition WHERE word_surface = %s'
        self.cursor.execute(sql, (word_surface,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        return None



# Debugging MySQLRepository to ensure data is loaded correctly
if __name__ == "__main__":
    repo = MysqlRepository()
    roots = repo.load_rootVerbs()
    print("Loaded roots:")
    for root in roots:
        print(f"Root: {root.canonical_form}, Gloss: {root.gloss}, Transitivity: {root.transitivity}")

    nominalizers = repo.load_nominalizers()
    print("Loaded nominalizers:")
    for nominalizer in nominalizers:
        print(f"Nominalizer: {nominalizer.canonical_form}, Gloss: {nominalizer.gloss}")

    definition = repo.load_definitions("vúvanpiš")
    print(f"Definition for 'vúvanpiš': {definition}")