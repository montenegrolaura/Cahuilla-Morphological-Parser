class MorphologicalParser:
    def __init__(self, roots, nominalizers):
        self.roots = roots
        self.nominalizers = nominalizers

    def parse(self, word):
        components = {
            'root': [],
            'nominalizers': []
        }

        # Extract the root
        for root, definition in self.roots.items():
            if word.startswith(root):
                components['root'].append((root, definition))
                word = word[len(root):]
                break

        # Extract nominalizers
        for suffix, meaning in self.nominalizers.items():
            if word.endswith(suffix):
                components['nominalizers'].append((suffix, meaning))
                word = word[:-len(suffix)]

        return components
