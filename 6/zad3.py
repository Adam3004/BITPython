import exceptions
from statistics import mean

listOfGrades = {'A': 5, 'B': 4, 'C': 3, 'D': 2, 'F': 1, 'A+': 5.5, 'B+': 4.5, 'C+': 3.5, 'D+': 2.5, 'F+': 1.5}


class Checker:
    @staticmethod
    def grade_format_chekcer(name: str):
        if name not in listOfGrades.keys():
            raise exceptions.WrongGrade


class Grade:
    def __init__(self, name: str):
        Checker.grade_format_chekcer(name)
        self.name = name
        self.value = listOfGrades[name]

    def get_gade(self):
        return (self.name, self.value)

    def __str__(self):
        return (f'{self.name} {self.value}')


class GradeLog:
    def __init__(self):
        self.myGrades = list()
        self.names = {value: key for key, value in listOfGrades.items()}

    def add_grade(self, grade: Grade):
        self.myGrades.append(grade.get_gade())

    def get_grades_average(self):
        values = [elem[1] for elem in self.myGrades]
        return (f'Average: {self.names[round(mean(values))]}')

    def __str__(self):
        _output = [elem[0] for elem in self.myGrades]
        return f"Grades: {', '.join(_output)}"

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    grade1 = Grade('A')
    grade2 = Grade('F+')
    gradeLog1 = GradeLog()
    gradeLog1.add_grade(grade2)
    gradeLog1.add_grade(grade1)
    print(gradeLog1)
    print(gradeLog1.get_grades_average())
