class School:
    def __init__(self):
        self.school_roster = {}
        self.added_list = []

    def add_student(self, name, grade):
        if name not in self.school_roster:
            self.school_roster.update({name:grade})
            self.added_list.append(True)
        else: self.added_list.append(False)

    def roster(self):
        return sorted(self.school_roster.keys(),key=lambda x: (self.school_roster[x], x))

    def grade(self, grade_number):
        return sorted(key for key,value in self.school_roster.items() if value == grade_number)

    def added(self):
        return self.added_list
