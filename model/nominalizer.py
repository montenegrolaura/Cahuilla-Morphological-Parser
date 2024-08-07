from model.morpheme import Morpheme
from model.enums import PartsOfSpeech, Class1Relationship

class Nominalizer(Morpheme):
    def __init__(self, canonical_form: str, gloss: str, pos: PartsOfSpeech, class1relationship: Class1Relationship):
        super().__init__(canonical_form, gloss, pos)
        self.class1relationship = class1relationship

    def __repr__(self):
        return f"Nominalizer(canonical_form={self.canonical_form}, gloss={self.gloss}, pos={self.pos}, class1_relationship={self.class1_relationship})"