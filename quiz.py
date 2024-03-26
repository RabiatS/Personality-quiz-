question_bank = {
    'At a crossroads on a solo journey, you choose the path that is': ['VILLAGE', 'WILDERNESS'],
    'When making decisions, you rely more on your': ['LOGIC', 'HEART'],
    'At a social gathering, you are more likely to be': ['CONVERSING', 'EXPLORING'],
    'Your preferred activity is more likely to be': ['READING', 'TRAVELING'],
    'Faced with a problem, you first': ['THINK', 'ACT'],
    'Your ideal vacation involves': ['MEDITATION', 'ADVENTURE'],
    'In your free time, you enjoy': ['PHILOSOPHY', 'HOBBIES']
}

answer_bank = {
    'Philosopher': ['VILLAGE', 'LOGIC', 'CONVERSING', 'READING', 'THINK', 'MEDITATION', 'PHILOSOPHY'],
    'Adventurer': ['WILDERNESS', 'HEART', 'EXPLORING', 'TRAVELING', 'ACT', 'ADVENTURE', 'HOBBIES']
}
# functions
def get_input(options):
    response = input(f'Type your answer: {options[0]} OR {options[1]}?').upper()
    
    return response
