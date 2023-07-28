class Audition:

    all = []

    def __init__(self, role, actor, location, phone):
        self.role = role
        self.actor = actor
        self.location = location
        self.phone = phone
        Audition.all.append(self)

    def hired(self):
        'true' if False else 'false'

    pass
