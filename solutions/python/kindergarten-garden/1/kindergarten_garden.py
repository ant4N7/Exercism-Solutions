class Garden:
    STUDENTS = ['Alice','Bob','Charlie','David','Eve','Fred','Ginny',
                'Harriet','Ileana','Joseph','Kincaid','Larry']
    PLANT_DICT = {'G':'Grass','C':'Clover','R':'Radishes','V':'Violets'}
    def __init__(self, diagram, students=STUDENTS):
        students.sort()
        diagrams = diagram.split('\n')
        self.plants = lambda s: [self.PLANT_DICT[key]for key in 
                                 diagrams[0][students.index(s)*2:students.index(s)*2+2]+
                                 diagrams[1][students.index(s)*2:students.index(s)*2+2]]
