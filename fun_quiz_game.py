import sys
sys.path.append('./files')

from quiz import question_bank, answer_bank

def get_user_response(answer_choices):
    '''
    This function prompts a user to type in an answer from a set of choices.
    If none of the answer choices match, a message is shown to the user
    and they are asked to provide another response. This will continue until the user
    correctly types in a response.
    
    After the user has correctly typed a response, the function will return
    that response in uppercase.
    '''
    needs_response = True
    while needs_response == True:
        # get response from user and change to uppercase
        user_response = input()
        user_response = user_response.upper()
   
        if (user_response == answer_choices[0] ) or (user_response == answer_choices[1]):
            needs_response = False
        # if not, display a message to the user to try again
        else:
            print("Wrong choice! Try again!")

    # return the response from the user (should already be in uppercase)
    print(user_response)
    return user_response

def personality_quiz(question_bank, answer_bank):
    philosopher_score = 0
    adventurer_score = 0
    q_number = 0 
    n_questions = len(question_bank) # total number of questions

    for question, choices in question_bank.items():
        
        q_number +=1
        print(f"Question {q_number} of {n_questions}: {question}")
        print(choices)
        user_response = get_user_response(choices)
        
        if user_response == answer_bank['Philosopher'][q_number - 1]:
             philosopher_score += 1
       
        else:
            adventurer_score += 1

    if philosopher_score > adventurer_score:
        match = '*****You are a great philosopher*****'
    elif philosopher_score < adventurer_score:
        match = '**** You are an amazing adventurer********'
    else:
        match = "******You have an equal mix of both Philosopher and Adventurer qualities!*****"
personality_quiz(question_bank, answer_bank)