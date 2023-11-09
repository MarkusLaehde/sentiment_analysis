#!/usr/bin/python3

import os
import sys
from question_type_describe import question_describe_main
from question_type_on_scale import questions_on_scale_main
from question_type_yes_no import questions_yes_no_main
from question_type_choose_4 import question_choose_4_main

def terminal_clear():
    """
    This function clears the terminal when it's called.
    It keeps terminal looking tidy.

    STATEMENT: This was written by ChatGPT, but the idea is mine.
    """
    if os.name == 'posix':
        return os.system('clear')
    else:
        return os.system('cls')


def desribe_score(count_describe_pos, count_describe_neg)->float:
    """
    This function calculates the ratio of positive and negative words returned from question_describe_main().
    The formula is such that it always returns a value between 0 and 1.

    Parameters:
    count_describe_pos = number of positive words found in users answers to describe -questions
    count_describe_neg = number of negative words found in users answers to describe -questions

    Returns:
    pos = ratio returned if number of positive words is bigger, if ratio is equal 0 is returned
    neg = ratio returned if number of positive words is bigger, if ratio is equal 0 is returned
    """
    positive_words_count, negative_words_count = count_describe_pos, count_describe_neg
    pos = neg = 0
    # more positive words
    if positive_words_count > negative_words_count:
        pos += positive_words_count / (positive_words_count + negative_words_count)
        #print("describe pos", pos)
        return pos, 0
    # more negative words
    elif positive_words_count < negative_words_count:
        neg += negative_words_count / (positive_words_count + negative_words_count)
        #print("describe neg", neg)
        return 0, neg
    # equal amount of positive and negative
    else:
        return 0, 0


def mood_score(count_choose_4_pos, count_choose_4_neg, score_on_scale_pos, score_on_scale_neg, score_yes_no_pos, score_yes_no_neg, score_describe_pos, score_describe_neg)->float:
    """
    This function calculates the mood score of all answers returned (in case of question_describe_main(): score_describe_pos/score_describe_neg from desribe_score()).
    The formula is such that it always returns a value between 0 and 1. The formula is not a scientific one, but a result of testing done in google sheets.

    The mood score comes predominantly from the desribe_score(). 
    However, if score_describe_pos is totally positive(1), but all the other question-types are negative, will the total score be in 'neutral' range.
    Also, if score_describe_pos is in 'neutral' range, but all the other question-types are positive, will the total score be in 'positive' range.
    
    This logic also applies in the negative side.
    Limits of 'neutral' can be independently changed for positive and negative sides in the sentiment_analysis_main() with set_neutral_limit_pos/set_neutral_limit_neg -variables.

    Parameters:
    count_choose_4_pos = ratio of positive words returned from question_choose_4_main(), this value is between 0 and 0.05 
    count_choose_4_neg = ratio of negative words returned from question_choose_4_main(), this value is between 0 and 0.05 
    score_on_scale_pos = positive score returned from questions_on_scale_main(), this value is between 0 and 0.05, if users answer to question is negative, this value is 0
    score_on_scale_neg = negative score returned from questions_on_scale_main(), this value is between 0 and 0.05, if users answer to question is positive, this value is 0
    score_yes_no_pos = positive score returned from questions_yes_no_main(), this value is 0.05 if users answers is positive and 0 if users answer is negative or 'pass'
    score_yes_no_neg = negative score returned from questions_yes_no_main(), this value is 0.05 if users answers is negative and 0 if users answer is positive or 'pass'
    score_describe_pos = ratio returned from describe_score() if number of positive words is bigger, if ratio is equal 0 is returned, this value is always between 0 and 1
    score_describe_neg = ratio returned from describe_score() if number of negative words is bigger, if ratio is equal 0 is returned, this value is always between 0 and 1

    Returns:
    mood_on_positive_side_score = returns the mood score if mood is positive, this value is always between 0 and 1, if mood is negative or completely equal returns 0
    mood_on_negative_side_score = returns the mood score if mood is negative, this value is always between 0 and 1, if mood is positive returns 0
    NOTE: equal score is returned to the positive side, because testing this program with ChatGPT_test_answers, neutral answers had more positive words than negative
    """
    mood_on_positive_side_score = 0
    mood_on_negative_side_score = 0
    if score_describe_pos == score_describe_neg:
        mood_on_positive_side_score = ((score_describe_pos + count_choose_4_pos + score_on_scale_pos + score_yes_no_pos)**(1/5)) * ((100/(count_choose_4_neg + score_on_scale_neg + score_yes_no_neg + 0.1))*0.001)

    if score_describe_pos > score_describe_neg:
        mood_on_positive_side_score = ((score_describe_pos + count_choose_4_pos + score_on_scale_pos + score_yes_no_pos)**(1/5)) * ((100/(count_choose_4_neg + score_on_scale_neg + score_yes_no_neg + 0.1))*0.001)

    if score_describe_pos < score_describe_neg:
        mood_on_negative_side_score = ((score_describe_neg + count_choose_4_neg + score_on_scale_neg + score_yes_no_neg)**(1/5)) * ((100/(count_choose_4_pos + score_on_scale_pos + score_yes_no_pos + 0.1))*0.001)

    return mood_on_positive_side_score, mood_on_negative_side_score

def continuation_or_feedback():
    """
    This functions runs at the end of base level -sentiment analysis. It asks if user wants continue with the analysis. 
    If user decides to continue, it passes user to continuation-questions.
    If user decides to quit, it asks for feedback and then quits the program with sys.exit().
    """
    print("\nThat was the end of the basic mood analysis.")
    continuation_question = input("\nDo you wish to continue with mood analysis further (yes/no)?\n")
    if continuation_question == "no":
        try:
            feedback_rating = int(input("\nDid you feel our analysis was accurate?\n\nPlease, rate our analysis on a scale of 1-5 (where 1 is the lowest score / 5 is the highest score)\nYour rating here: "))
            if 0 < feedback_rating <= 5:
                print("\nThank you!")
        except ValueError:
            pass
        feedback_open_from = input("\nYou can give open feedback here (or pass with Enter): \n")
        if 0 < len(feedback_open_from):
            print("Thank you!")
        print("\nThank you and all the best for your future!")
        sys.exit()
    if continuation_question == "yes":
        print("\nGreat, let's continue!")

def feedback():
    """
    This function runs at the end of the whole sentiment analysis. It asks for user feedback and then quits the program with sys.exit().
    """
    print("\nThat was the end of our analysis.")
    try:
        feedback_rating_end = int(input("\nDid you feel our analysis was accurate?\n\nPlease, rate our analysis on a scale of 1-5 (where 1 is the lowest score / 5 is the highest score)\nYour rating here: "))
        if 0 < feedback_rating_end <= 5:
            print("\nThank you!")
    except ValueError:
        pass
    feedback_open_from_end = input("\nYou can give open feedback here (or pass with Enter): \n")
    if 0 < len(feedback_open_from_end):
        print("Thank you!")
    print("\nThank you and all the best for your future!")
    sys.exit()
      

def sentiment_analysis_main():
    """
    This is the main function which runs the sentiment analysis process.
    Inside are calls to functions used in different stages of sentiment analysis as well as feedback to the user according to their measured mood.
    """
    ###### START ######
    # Opening words
    print("""\n*** WELCOME TO A MOOD ANALYZER ***
    \nThis analyzer consists of:
    - Choosing words from a word cloud
    - Rating your mood on a scale of 1 - 5
    - Evaluating statements about your mood
    - Describing your feelings with open answers

    Once completing base level questions you get a basic mood analysis.
    At this point you can choose to continue on with the analysis or quit and give feedback (if you like).
    If you decide to continue with the analysis, you will get new questions tailored to your mood. 

    Hopefully this analysis helps you at reflecting your emotions and feelings about life!""")

    exit_start = input("\nPress Enter when you're ready to begin.")
    terminal_clear()

    # set the starting level of mood analysis
    mood_level = 'base_level'

    ###### BASE_LEVEL -QUESTIONS ######
    # ask choose_4 -questions and return answer count
    count_choose_4_pos, count_choose_4_neg = question_choose_4_main()
    #print("ask 4 pos neg", count_choose_4_pos, count_choose_4_neg)
    terminal_clear()

    # ask on_scale -questions and return answer score
    score_on_scale_pos, score_on_scale_neg = questions_on_scale_main(mood_level)
    #print("on scale pos neg", score_on_scale_pos, score_on_scale_neg)
    terminal_clear()

    # ask yes/no -questions and return score
    score_yes_no_pos, score_yes_no_neg = questions_yes_no_main(mood_level)
    #print("yes no pos neg", score_yes_no_pos, score_yes_no_neg)
    terminal_clear()

    # ask describe -questions and return pos/neg word counts
    count_describe_pos, count_describe_neg = question_describe_main(mood_level)
    terminal_clear()


    ###### BASE_LEVEL MOOD -SCORING ######
    # calculate score for describe word counts and return it
    score_describe_pos, score_describe_neg = desribe_score(count_describe_pos, count_describe_neg)

    # calculate base level mood score
    base_mood_score_positive, base_mood_score_negative = mood_score(count_choose_4_pos, count_choose_4_neg, score_on_scale_pos, score_on_scale_neg, score_yes_no_pos, score_yes_no_neg, score_describe_pos, score_describe_neg)

    # set limit for neutral score -zone
    set_neutral_limit_pos = 0.45
    set_neutral_limit_neg = 0.45

    ###### MOOD -SCORE REPORT AND FEEDBACK / CONTINUATION ######
    #print("pos_mood_score", base_mood_score_positive)
    #print("neg_mood_score", base_mood_score_negative)

    # neutral mood
    if base_mood_score_positive < set_neutral_limit_pos and base_mood_score_negative < set_neutral_limit_neg:
        print("\nAccording to our analysis, your outlook on life is quite neutral. That's great! Life is a balance of holding on and letting go.")
        continuation_or_feedback()
        mood_level = 'neutral'

    # positive mood
    if base_mood_score_positive >= set_neutral_limit_pos:
        print("\nAccording to our analysis, your outlook on life is positive. That's great!")
        continuation_or_feedback()
        mood_level = 'positive'

    # negative mood
    if base_mood_score_negative >= set_neutral_limit_neg:
        print("\nAccording to our analysis, your outlook on life is on the negative side. We get it. Life is not always easy!")
        continuation_or_feedback()
        mood_level = 'negative'

    ######################################################################################################################################
    terminal_clear()
    ###### CONTINUATION -QUESTIONS ACCORDING TO THE MOOD-LEVEL SET IN THE LAST STEP ######
    # ask yes/no -questions and return score
    score_yes_no_pos, score_yes_no_neg = questions_yes_no_main(mood_level)
    #print("yes no pos neg", score_yes_no_pos, score_yes_no_neg)
    terminal_clear()

    # ask describe -questions and return pos/neg word counts
    count_describe_pos, count_describe_neg = question_describe_main(mood_level)
    terminal_clear()

    # ask on_scale -questions and return answer score
    score_on_scale_pos, score_on_scale_neg = questions_on_scale_main(mood_level)
    #print("on scale pos neg", score_on_scale_pos, score_on_scale_neg)
    terminal_clear()


    ###### BASE_LEVEL MOOD -SCORING ######
    # calculate score for describe word counts and return it
    score_describe_pos, score_describe_neg = desribe_score(count_describe_pos, count_describe_neg)

    # calculate base level mood score
    base_mood_score_positive, base_mood_score_negative = mood_score(count_choose_4_pos, count_choose_4_neg, score_on_scale_pos, score_on_scale_neg, score_yes_no_pos, score_yes_no_neg, score_describe_pos, score_describe_neg)

    # set limit for neutral score -zone
    set_neutral_limit_pos = 0.45
    set_neutral_limit_neg = 0.45

    # neutral mood
    if base_mood_score_positive < set_neutral_limit_pos and base_mood_score_negative < set_neutral_limit_neg:
        print("\nYour life seems to be in good balance!\nEnjoy the good days and don't let a bad day make you feel like you have a bad life.")
        feedback()

    # positive mood
    if base_mood_score_positive >= set_neutral_limit_pos:
        print("\nYou seem to be doing great!\nWe wish you will find ways to share your happiness with others.\nShared joy is double joy!")
        feedback()

    # negative mood
    if base_mood_score_negative >= set_neutral_limit_neg:
        print("\nDon't loose your hope! Remember that things can change for the better.\nRemember, that there is always a way to get help if things get too heavy.")
        feedback()

if __name__ == "__main__":
    sentiment_analysis_main()