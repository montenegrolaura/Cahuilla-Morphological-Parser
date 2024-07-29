from model.enums import PartsOfSpeech
class Morpheme:
    def __init__(self, canonical_form: str, gloss: str, pos: PartsOfSpeech):
        self.canonical_form = canonical_form
        self.gloss = gloss
        self.pos = pos

    def __repr__(self):
        return f"Morpheme(canonical_form={self.canonical_form}, gloss={self.gloss}, and pos={self.pos})"
