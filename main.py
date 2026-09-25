from src.models.models import UnansweredQuestion


def main():
    q1 = UnansweredQuestion(question="Question 1")
    q2 = UnansweredQuestion(question="Question 2")
    print(q1.question)
    print(q2.question)
    print(q1.question_id)
    print(q2.question_id)
    print(q1.question_id == q2.question_id)
    #print("Hello from rag-against-the-machine!")


if __name__ == "__main__":
    main()
