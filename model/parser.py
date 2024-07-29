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
            'nominalizer': [],
            'nominalizer_gloss': []
        }

        word_surface = word.surface_form

        # Extract the root
        for root in roots:
            if word_surface.startswith(root.canonical_form):
                components['root'] = root.canonical_form
                components['root_gloss'] = root.gloss
                word_surface = word_surface[len(root.canonical_form)]
                break

        # Extract nominalizers
        for nominalizer in nominalizers:
            if word_surface.endswith(nominalizer.canonical_form):
                components['nominalizer'].append(nominalizer.canonical_form)
                components['nominalizer_gloss'].append(nominalizer.gloss)
                #word_surface = word_surface[:-len(nominalizer.canonical_form)]

        return components
