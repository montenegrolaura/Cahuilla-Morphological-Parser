from database.repository import Repository
from model.word import Word


class MorphologicalParser:
    def __init__(self, repository: Repository):
        self.repository = repository

    def parse(self, word: Word):
        roots = self.repository.load_rootVerbs()
        nominalizers = self.repository.load_nominalizers()
        components = {
            'root': '',
            'root_gloss': '',
            'nominalizer': '',
            'nominalizer_gloss': ''
        }

        word_surface = word.surface_form

        # Extract the root
        for root in roots:
            if word_surface.startswith(root.canonical_form):
                components['root'] = root.canonical_form
                components['root_gloss'] = root.gloss
                word_surface = word_surface[len(root.canonical_form):]
                print(f"Root found: {root.canonical_form}, remaining word_surface: {word_surface}")
                break

        # Extract nominalizers
        for nominalizer in nominalizers:
            if word_surface.endswith(nominalizer.canonical_form):
                components['nominalizer'] = nominalizer.canonical_form
                components['nominalizer_gloss'] = nominalizer.gloss
                print(f"Nominalizer found: {nominalizer.canonical_form}")
                #word_surface = word_surface[:-len(nominalizer.canonical_form)]

        print(f"Final components: {components}")
        return components
