
from database.mysql_repository import MysqlRepository
from model.deverbalNoun import DeverbalNoun

class Services:

    def __init__(self):
        self.repository = MysqlRepository()

    # Use case 1: parse the surface form word into its morphological morphemes
    def parse_word(self, word_surface:str) -> DeverbalNoun:
        definition = self.repository.load_definitions(word_surface)
        roots = self.repository.load_rootVerbs()
        nominalizers = self.repository.load_nominalizers()
        nominalizers.sort(key=lambda x: len(x.canonical_form), reverse=True)

        components = DeverbalNoun(definition=definition)

        # Extract the root
        for root in roots:
            if word_surface.startswith(root.canonical_form):
                components.root = root.canonical_form
                components.root_gloss = root.gloss
                components.transitivity = root.transitivity
                word_surface = word_surface[len(root.canonical_form):]
                print(f"Root found full match: {root.canonical_form}, remaining word_surface: {word_surface}")
                break
        else:
            for root in roots:
                if self.partial_match(word_surface, root.canonical_form):
                    components.root = root.canonical_form
                    components.root_gloss = root.gloss
                    components.transitivity = root.transitivity
                    word_surface = word_surface[3:]
                    print(f"Root found partial match: {root.canonical_form}, remaining word_surface: {word_surface}")
                    break

        # Extract nominalizers
        for nominalizer in nominalizers:
            if word_surface.endswith(nominalizer.canonical_form):
                components.nominalizer = nominalizer.canonical_form
                components.nominalizer_gloss = nominalizer.gloss
                components.class1relationship = nominalizer.class1relationship
                print(f"Nominalizer found: {nominalizer.canonical_form}")
                break
                # word_surface = word_surface[:-len(nominalizer.canonical_form)]

        print(f"Final components: {components}")
        return components

    def partial_match(self, word_surface: str, root_form) -> bool:
        return word_surface[:3] == root_form[:3]



if __name__ == "__main__":
    services = Services()
    example_word = 'vúvanpis'
    print(services.parse_word(example_word))




