
def questions_on_scale_main(mood_level)->float:
    """
    This function asks the user to rate their mood regarding a statement in a scale 1 to 5.
    The answer is scaled to positive 0-0.05 or negative 0-0.05 or if neutral 0.

    Parameters:
    mood_level = mood level is set at sentiment_analysis_main() and at the end of base level questions it's updated according to the sentiment analysis result

    Returns:
    if user answer is positive returns pos=0-0.05, 0
    if user answer is negative returns 0, neg=0-0.05
    if user answer is neutral returns 0, 0
    """
    questions_on_scale = {
        'base_level':'happy are you in general',
        'neutral':'meaningful does your life feel',
        'positive':'confident are you about reaching your future goals',
        'negative':'safe do you feel about your future'
    }

    mood = mood_level
    question = questions_on_scale[mood]
    pos = 0
    neg = 0
    while True:
        try:
            answer = int(input(f"\nOn a scale of 1-5 (where 1 is the most negative / 3 is neutral / 5 is the most positive) \n\nHow {question}?\n"))
            # positive answer
            if 3 < answer <= 5:
                pos = ((answer - 1.5) / 1.5) / 46.7
                return pos,0
                break
            # negative answer
            elif 3 > answer >= 1:
                neg = (((answer - 1.5) / 1.5) * -1) / 46.7
                return 0,neg
                break
            # neutral answer
            elif answer == 3:
                return 0,0
                break
            else:
                print("Please enter a value between 1 and 5.")
        except ValueError:
            print("Please, use a number.")



