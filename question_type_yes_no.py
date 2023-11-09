
def questions_yes_no_main(mood_level)->float:
    """
    This function presents statements about mood to the user and yes/no/pass answers are approved.
    Functions has different statements according to the mood level.

    Parameters:
    mood_level = mood level is set at sentiment_analysis_main() and at the end of base level questions it's updated according to the sentiment analysis result

    Returns:
    if user answer is positive returns 0.05, 0
    if user answer is negative returns 0, 0.05
    if user answer is 'pass' returns 0, 0
    """
    questions_yes_no = {
        'base_level':"I don't have much worries.",
        'neutral':"I'm happy with my role in my job.",
        'positive':'I feel that my life is in balance.',
        'negative':'My basic needs are met.'
    }

    mood = mood_level
    question = questions_yes_no[mood]
    while True:
        try:
            answer = input(f"\nWould you agree with the following statement:\n{question}\n\nPlease answer here (yes/no/pass):\n")
            answer = answer.lower()
            # positive answer
            if answer == 'yes':
                return 0.05,0
                break
            # negative answer
            elif answer == 'no':
                return 0,0.05
                break
            # pass
            elif answer == 'pass':
                return 0,0
                break
            else:
                print("Please answer yes, no or pass.")
        except ValueError:
            print("Please answer yes, no or pass.")
