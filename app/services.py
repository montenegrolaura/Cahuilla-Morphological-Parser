from typing import Dict
from database.repository import Repository
from database.mysql_repository import MysqlRepository
from model.rootVerb import RootVerb
from model.nominalizer import Nominalizer


class Services:

    def __init__(self):
        self.repository = MysqlRepository()

    # Use case 1: parse the surface form word into its morphological morphemes
    def parse_word(self, word_surface:str) -> Dict[str, str]:
        definition = self.repository.load_definitions(word_surface)
        roots = self.repository.load_rootVerbs()
        nominalizers = self.repository.load_nominalizers()
        nominalizers.sort(key=lambda x: len(x.canonical_form), reverse=True)
        print(nominalizers)

        components = {
            'definition': definition,
            'root': '',
            'root_gloss': '',
            'transitivity': None,
            'nominalizer': '',
            'nominalizer_gloss': ''
        }

        # Extract the root
        for root in roots:
            if word_surface.startswith(root.canonical_form):
                components['root'] = root.canonical_form
                components['root_gloss'] = root.gloss
                components['transitivity'] = root.transitivity
                word_surface = word_surface[len(root.canonical_form):]
                print(f"Root found: {root.canonical_form}, remaining word_surface: {word_surface}")
                break
            #elif self.partial_match(word_surface, root.canonical_form):
            #    matched_len = self.matched_root_len(word_surface, root.canonical_form)
            #    components['root'] = root.canonical_form
            #    components['root_gloss'] = root.gloss
            #    word_surface = word_surface[matched_len:]
            #    break

        # Extract nominalizers
        for nominalizer in nominalizers:
            if word_surface.endswith(nominalizer.canonical_form):
                components['nominalizer'] = nominalizer.canonical_form
                components['nominalizer_gloss'] = nominalizer.gloss
                print(f"Nominalizer found: {nominalizer.canonical_form}")
                break
                # word_surface = word_surface[:-len(nominalizer.canonical_form)]

        print(f"Final components: {components}")
        return components

    def partial_match(self, word_surface: str, root_form: str) -> bool:
        max_len = min(len(word_surface), len(root_form))
        for i in range(max_len, 0, -1):
            if word_surface.startswith(root_form[:i]):
                return True
        return False

    def matched_root_len(self, word_surface: str, root_form: str) -> int:
        max_len = min(len(word_surface), len(root_form))
        for i in range(max_len, 0, -1):
            if word_surface.startswith(root_form[:i]):
                return i
        return 0


if __name__ == "__main__":
    services = Services()
    example_word = 'vúvanpis'
    print(services.parse_word(example_word))




