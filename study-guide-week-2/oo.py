# Create your classes here
class Student:
    "Creates a student with a first and last name and an address"

    def __init__(self, f_name, l_name, address):
        self.first_name = f_name
        self.last_name = l_name
        self.address = address


class Question:
    "Creates a question and answer pair"

    def __init__(self, q, a):
        self.question = q
        self.correct_answer = a

    def ask_and_evaluate(self):
        user_ans = input(f'{self.question} ')
        result = str(user_ans).lower() == self.correct_answer
        print(result)

        return result



class Exam:

    def __init__(self, name):
        """Creates and exam with a list of questions and answers"""

        self.name = name
        self.questions = []

    def add_question(self, q):
        """Adds a question -- answer pair to the exam questions list"""

        self.questions.extend(q)

    def administer(self):
        """Asks a user all questions in the question list and tallies the correct answers"""

        correct_answers = 0

        for q in self.questions:
           if q.ask_and_evaluate(): correct_answers += 1

        score = correct_answers / len(self.questions)

        print(f'You scored {int(score * 100)} %')

        return score


class StudentExam:
    """Stores all data for a student and an exam they have taken"""

    def __init__(self, student, exam):
        self.student = student
        self.exam = exam
        self.score = None

    def take_test(self):
        self.score = self.exam.administer()


def example():
    """Creates a mock testing environment by creating an exam, populating it with questions,
        creating a student, administering the test to the student and recoring their score
    """

    e1 = Exam('Methods')
    q1 = Question('What is the method for adding an element to a set?', '.add()')
    q2 = Question('What is the method for adding an element to a list?', '.append()')
    q3 = Question('Does Python allow you to combine strings and integers?', 'no')
    q4 = Question('What is the method for finding the length of a collection?', 'len()')
    q5 = Question('What type of collection is used to store unique values?', 'set')
    e1.add_question([q1, q2, q3, q4, q5])
    s1 = Student('Bob', 'Ross', '123 Happy Tree Lane')
    test = StudentExam(s1, e1)

    test.take_test()

example()




