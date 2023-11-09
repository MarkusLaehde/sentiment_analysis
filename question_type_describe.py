
def question_describe_main(mood_level)->float:
    """
    This function asks the user to describe their mood according to the question/scenario presented.
    Function then checks the answers against negative_words- and positive_words -lists and counts how many times user uses negative or positive words.

    Parameters:
    mood_level = mood level is set at sentiment_analysis_main() and at the end of base level questions it's updated according to the sentiment analysis result
    negative_words = is a separate file where negative words are stored as a string
    positive_words = is a separate file where positive words are stored as a string

    Returns:
    positive_words_count = number of times positive words where used by user
    negative_words_count = number of times negative words where used by user

    STATEMENT: The method used for storing and fetching long word lists was suggested by ChatGPT
    """

    from negative_words import negative_words
    from positive_words import positive_words

    negative_words = negative_words.replace(" ", "")
    positive_words = positive_words.replace(" ", "")

    negative_words_list = [word.strip() for word in negative_words.split(',')]
    positive_words_list = [word.strip() for word in positive_words.split(',')]


    questions_describe = {
        'base_level':['life', 'relationships in your life'],
        'neutral':['your everyday routines', 'your accomplishments'],
        'positive':['your achievements', 'the way you contribute to the society'],
        'negative':['the neighborhood you live in', 'your work']
        }

    mood = mood_level
    answers = [] 

    for question in questions_describe[mood]:
        answer = input(f"\nDescribe how you feel about {question}.\nPlease answer here:\n")
        answers.append(answer)

    positive_words_count = negative_words_count = 0

    for word in positive_words_list:
        positive_words_count += str(answers).lower().count(word)
    for word in negative_words_list:
        negative_words_count += str(answers).lower().count(word) 

    return positive_words_count, negative_words_count



 
