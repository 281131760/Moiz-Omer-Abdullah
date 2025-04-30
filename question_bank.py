#---------------------------------------
#  Question Bank
#    Student B
#---------------------------------------

import random
import game_mechanics
# Simplified example with one category. Expand as needed.
questions = {
    "Science": [
        ("What is the chemical symbol for water?", "H2O"),
        ("What gas do humans breathe in?", "Oxygen"),
        ("What force pulls objects toward Earth?", "Gravity"),
        ("What organ pumps blood through the body?", "Heart"),
        ("What is the boiling point of water in Celsius?", "100"),
        ("What is the center of an atom called?", "Nucleus"),
        ("What gas do plants absorb?", "Carbon Dioxide")
        # Add more questions as tuples (question, answer)
    ],
}

hints = {
    "Science": [
        # Pair each question with a corresponding hint.
        "It's made of two hydrogen atoms and one oxygen atom.",
         "We need it to survive. It's 21% of the air.",
        "It starts with G and keeps the moon in orbit.",
        "It's a vital muscular organ.",
        "It's the same as 212°F.",
        "It's surrounded by electrons.",
        "It's abbreviated as CO2."
    ],
    # Repeat for other categories as needed.
}

#---------------------------------------

def select_random_question(category):
    """
    Selects a random question from the specified category.

    Parameters:
    - category (str): The category from which to select a question.

    Returns:
    - tuple: A tuple containing the selected question (str) and its corresponding answer (str).
    """
    #------------------------
    # Add your code here
    #------------------------
    n = random.randint(0, len(questions[category]) - 1)
    ques_ans = questions[category][n]
    return ques_ans 
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def check_answer(player_answer, correct_answer):
    """
    Checks if the player's answer matches the correct answer.

    Parameters:
    - player_answer (str): The answer provided by the player.
    - correct_answer (str): The correct answer to the question.

    Returns:
    - bool: True if the answers match, False otherwise.
    """
    #------------------------
    # Add your code here
    #------------------------
    return player_answer.lower() == correct_answer.lower()
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def remove_question(category, question):
    """
    Removes a question from the list once it has been asked.

    Parameters:
    - category (str): The category from which to remove the question.
    - question (str): The question to be removed.

    Returns:
    - None
    """
    #------------------------
    # Add your code here
    #------------------------
    index = questions[category][question]
    questions[category].pop(index)
    hints[category].pop(index)
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def display_question_and_accept_answer(question):
    """
    Displays a question to the player and accepts their answer via input.

    Parameters:
    - question (str): The question to be displayed.

    Returns:
    - str: The player's answer to the question.
    """
    #------------------------
    # Add your code here
    #------------------------
    re = game_mechanics.choose_category(questions.keys)
    question = select_random_question(re)
    print(question)
    ans = input("Answer Here: ").lower
    return ans



    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def provide_hint(category, question):
    """
    Provides a hint for the given question based on its category.

    Parameters:
    - category (str): The category of the question.
    - question (str): The question for which to provide a hint.

    Returns:
    - str: The hint for the given question.
    """
    #------------------------
    # Add your code here
    #------------------------
    ind = questions[category][question].index
    return hints[category][ind]
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def display_correct_answer(correct_answer):
    """
    Displays the correct answer if the player's answer is incorrect.

    Parameters:
    - correct_answer (str): The correct answer to the question.

    Returns:
    - None
    """
    #------------------------
    # Add your code here
    #------------------------
    print(correct_answer)
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------




