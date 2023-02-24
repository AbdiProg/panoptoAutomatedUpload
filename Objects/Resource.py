class Resource:

    def __init__(self, type, link, license):
        self.license = license
        self.link = link
        self.type = type

    def __str__(self):
        return self.type + " : " + self.link + " : " + self.license
