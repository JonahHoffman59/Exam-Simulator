######################################################################
# author: Jonah Hoffman
# date: 2/08/2023
# desc: runs a simulation that determines chances of passing a test
#####################################################################

from random import sample

DEBUG = True   # Activate intermediate output 

class Simulation:

    def __init__(self):
        print("Simulation Set Up:")
        print("="*66)

        # initialize number of passed tests
        self.passed_tests = 0

        # initialize scores
        self.scores = []

        # create list of questions 1 through whatever number you choose
        self.question_bank = list(range(1, int(input("What is the size of the question bank? ")) + 1))

        # ask user number of questions studied
        self.amount_studied = int(input("How many of those questions have you studied? "))

        # ask user number of questions on the test
        self.question_amount = int(input("How many questions does the test have? "))

        # ask user number of correct answers to pass the test
        self.passing_score = int(input("How many questions must you answer correctly to pass the test? "))

        print("="*66)

        # ask user how many simulations to run
        self.num_simulations = int(input("How many simulations do you want to run? "))
        
        print("="*66)


    def __str__(self):
        return (f'Questions you were asked: {self.test_questions}\nQuestions you studied: {self.questions_studied}\nQuestions you passed: {self.correct_questions}\nWhich means you scored {len(self.correct_questions)}/{len(self.test_questions)}')


    # function that runs one simulation
    def run_one_sim(self):
        # clear list of questions you got correct for each simulation
        self.correct_questions = []

        # creates random list of questions to be on the test
        self.test_questions = sample(self.question_bank, k=self.question_amount)

        # creates random list of questions user "studied"
        self.questions_studied = sample(self.question_bank, k=self.amount_studied)

        # for every test question this loop checks if it is a question the user "studied"
        for i in range(len(self.test_questions)):
            for j in range(self.amount_studied):
                if (self.test_questions[i] == self.questions_studied[j]):

                    # add questions that the user got correct to the list of correct questions
                    self.correct_questions.append(self.test_questions[i])

        # add score to list of scores
        self.scores.append(len(self.correct_questions))

        # if the user passes the test, then it adds to the number of tests passed
        if len(self.correct_questions) >= self.passing_score:
            self.passed_tests += 1
        
    
    # funtion to run multiple simulations
    def run_multiple_sims(self, num):
        for i in range(num):
            self.run_one_sim()
            
            # if DEBUG is True, displays debug info
            if DEBUG:
                print(f"Simulation No. {i + 1}")
                print(self)
                print("-"*66)

        # prints more debug info
        if DEBUG:
            print(f"Simulation scores were:\n{a.scores}")

            
    # finds percent of times the user passed the test
    def find_pass_rate(self):
        return 100 * (self.passed_tests/self.num_simulations)


# Main code
a = Simulation()
a.run_multiple_sims(a.num_simulations)
print("="*66)
print(f"You passed the test {a.find_pass_rate()}% of the  time")