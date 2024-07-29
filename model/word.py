class Word:
    def __init__(self, surface_form: str, definition: str):
        self.surface_form = surface_form
        self.definition = definition

    def breakdown(self):
        pass

    def __repr__(self):
        return f"Word(surface_form={self.surface_form}, and definition={self.definition})"