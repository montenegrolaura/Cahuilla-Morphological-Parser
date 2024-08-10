from model.enums import Transitivity
from model.enums import Class1Relationship

class DeverbalNoun:
    def __init__(self, definition='', root='', root_gloss='', transitivity=None, nominalizer='', nominalizer_gloss='', class1relationship=None):
        self.definition = definition
        self.root = root
        self.root_gloss = root_gloss
        self.transitivity = transitivity
        self.nominalizer = nominalizer
        self.nominalizer_gloss = nominalizer_gloss
        self.class1relationship = class1relationship

    def __str__(self):
        transitivity_str = self.transitivity.name.lower().replace('_', ' ') if self.transitivity else ''
        class1relationship_str = self.class1relationship.name.lower().replace('_', ' ') if self.transitivity else ''

        return(f"The definition is '{self.definition}'. "
               f"The root verb is '{self.root}' which means '{self.root_gloss}'. This verb is {transitivity_str}. "
               f"The nominalizer is '{self.nominalizer}' which is a {self.nominalizer_gloss} and means '{class1relationship_str}'.")

    def to_dict(self):
        return{
            "definition": self.definition,
            "root": self.root,
            "root_gloss": self.root_gloss,
            "transitivity": self.transitivity.name if self.transitivity else None,
            "nominalizer": self.nominalizer,
            "nominalizer_gloss": self.nominalizer_gloss,
            "class1relationship": self.class1relationship.name if self.class1relationship else None
        }
