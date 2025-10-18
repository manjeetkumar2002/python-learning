quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A) London", "B) Berlin", "C) Paris", "D) Madrid"],
        "correct_answer": "C"
    },
    {
        "question": "Which programming language is known for its use in data science and machine learning?",
        "options": ["A) Java", "B) Python", "C) C++", "D) JavaScript"],
        "correct_answer": "B"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["A) Computer Processing Unit", "B) Central Processing Unit", "C) Central Program Utility", "D) Computer Program Unit"],
        "correct_answer": "B"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"],
        "correct_answer": "B"
    },
    {
        "question": "What year was Python first released?",
        "options": ["A) 1989", "B) 1991", "C) 1995", "D) 2000"],
        "correct_answer": "B"
    },
    {
        "question": "Who developed the theory of relativity?",
        "options": ["A) Isaac Newton", "B) Nikola Tesla", "C) Albert Einstein", "D) Stephen Hawking"],
        "correct_answer": "C"
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["A) African Elephant", "B) Blue Whale", "C) Giraffe", "D) Polar Bear"],
        "correct_answer": "B"
    },
    {
        "question": "In computing, what does 'HTML' stand for?",
        "options": ["A) Hyper Text Markup Language", "B) High Tech Modern Language", "C) Hyper Transfer Markup Language", "D) Home Tool Markup Language"],
        "correct_answer": "A"
    },
    {
        "question": "Which element has the chemical symbol 'O'?",
        "options": ["A) Gold", "B) Oxygen", "C) Osmium", "D) Oxide"],
        "correct_answer": "B"
    },
    {
        "question": "What is the smallest prime number?",
        "options": ["A) 0", "B) 1", "C) 2", "D) 3"],
        "correct_answer": "C"
    },
    {
        "question": "Which country is home to the kangaroo?",
        "options": ["A) Brazil", "B) Australia", "C) South Africa", "D) India"],
        "correct_answer": "B"
    },
    {
        "question": "What is the main ingredient in guacamole?",
        "options": ["A) Tomato", "B) Avocado", "C) Pepper", "D) Onion"],
        "correct_answer": "B"
    },
    {
        "question": "How many bits are in a byte?",
        "options": ["A) 4", "B) 8", "C) 16", "D) 32"],
        "correct_answer": "B"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["A) Vincent van Gogh", "B) Pablo Picasso", "C) Leonardo da Vinci", "D) Michelangelo"],
        "correct_answer": "C"
    },
    {
        "question": "What is the square root of 64?",
        "options": ["A) 6", "B) 7", "C) 8", "D) 9"],
        "correct_answer": "C"
    }
]

def quiz_run():
    score = 0
    total_questions = len(quiz_questions)

    for i in range(total_questions):
        question = quiz_questions[i]["question"]
        print(question)
        options = quiz_questions[i]["options"]
        for option in options:
            print(option)
        print("Enter your answer(A,B,C,D):")
        user_answer = input()
        if user_answer == quiz_questions[i]["correct_answer"]:
            score += 1
            print("Correct Answer !!")
        else:
            print("Incorrect Answer !!")
            print(f"Correct Answer is : {quiz_questions[i]['correct_answer']}")
        print(f"Your current score is : {score}/{total_questions}")

    print(f"You have give {score} correct answers.")

    print(f"Your score is {round((score/total_questions) * 100,2)}")
    print("Thank you for playing!")
quiz_run()