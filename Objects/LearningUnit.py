class LearningUnit:

    #To a video belongs a name, description, videoLink, pdf and lecturers

    def __init__(self, name, description, resources, lecturers):
        self.resources = resources
        self.name = name
        self.description = description
        self.lecturers = lecturers
