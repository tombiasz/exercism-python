class Allergies(object):

    ALLERGENTS = {
        'eggs': 1,
        'peanuts': 2,
        'shellfish': 4,
        'strawberries': 8,
        'tomatoes': 16,
        'chocolate': 32,
        'pollen': 64,
        'cats': 128,
    }

    def __init__(self, number):
        self.number = number

    def _is_allergic_to(self, value):
        return bool(self.number & value)

    def is_allergic_to(self, string):
        value = self.ALLERGENTS.get(string)
        return self._is_allergic_to(value)

    @property
    def lst(self):
        return [
            key
            for key, value in self.ALLERGENTS.items()
            if self._is_allergic_to(value)
        ]
