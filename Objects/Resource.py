class Resource:

    def __init__(self, type, link, license, description):
        self.license = license
        self.link = link
        self.type = type
        self.description = description

    def __str__(self):
        return self.type + " : " + self.link + " : " + self.license + " : " + self.description
