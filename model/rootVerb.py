from model.morpheme import Morpheme
from model.enums import Transitivity, PartsOfSpeech

class RootVerb(Morpheme):
    def __init__(self, canonical_form: str, gloss: str, pos: PartsOfSpeech, transitivity: Transitivity):
        super().__init__(canonical_form, gloss, pos)
        self.transitivity = transitivity

    def __repr__(self):
        return f"RootVerb(canonical_form={self.canonical_form}, gloss={self.gloss}, pos={self.pos}, and transitivity={self.transitivity})"