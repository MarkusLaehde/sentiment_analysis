import random

def question_choose_4_main()->float:
    """
    This function is currently used only in the base level -sentiment analysis.
    Function presents 10 words to the user in random order and asks for them to select 4 which best represent their mood.

    Returns:
    pos_return = ratio of positive words chosen by user in a scale from 0 to 0.05
    neg_return = ratio of negative words chosen by user in a scale from 0 to 0.05
    """
    choose_4_word_categories = {
        'satisfied':'positive',
        'happy':'positive',
        'relaxed':'positive',
        'wonderful':'positive',
        'positive':'positive',

        'lonely':'negative', 
        'tired': 'negative', 
        'hopeless':'negative',
        'sad':'negative',
        'cynical':'negative', 
        }

    word_sentiments = choose_4_word_categories
    word_list = list(word_sentiments.keys())
    random.shuffle(word_list)

    print("\nFrom this list, choose 4 words that best describe your emotions at the moment:\n")
    for word in word_list:
        print(word)
    while True:
        answer = input("\nWrite your 4 chosen words here (separate with commas):\n").replace(" ", "")
        answer.strip()
        try:
            check_count = 0
            for check in answer.split(','):
                if check in word_list:
                    check_count += 1
            if check_count > 4:
                print("\nDon't use more than 4 words!")
            elif check_count == 4:
                break
            else:
                print("\nPlease, use only words listed!")
        except ValueError:
            print("\nPlease, use only words listed!")
    
    positive_points = 0
    negative_points = 0
    
    for word in answer.split(','):
        for key, value in word_sentiments.items():
            if word == key:
                if value == 'negative':
                    negative_points += 1
                elif value == 'positive':
                    positive_points += 1

    pos_return = 0
    neg_return = 0

    pos_return = (positive_points / (positive_points + negative_points)) / 20
    neg_return = (negative_points / (positive_points + negative_points)) / 20

    return pos_return, neg_return


