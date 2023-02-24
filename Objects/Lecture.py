class Lecture:

    def __init__(self, name, description, learningUnits, lecturers, areas, semesterValue):
        self.name = name
        self.description = description
        self.learningUnits = learningUnits
        self.lecturers = lecturers
        self.areas = areas
        self.semesterValue = semesterValue

    def __str__(self):
        return self.name + " : " + self.description + " : " + self.areas + " : " + self.semesterValue
