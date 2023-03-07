class LearningUnit:

    # To a video belongs a name, description, videoLink, pdf and lecturers

    def __init__(self, name, resources, lecturers):
        self.resources = resources
        self.name = name
        self.lecturers = lecturers

    def __str__(self):
        return self.name
