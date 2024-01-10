# Sentiment Analysis

The objective of this school work was to code a sentiment analysis program.

This sentiment analysis questionaire contains 4 different question types:
- Choose 4 words that best describe your emotions at the moment
- Score your sentiment on scale 1-5 regarding scenario presented
- Would you agree with the following statement, yes/no
- Describe your feelings on topic presented

Analysis scoring is conducted as follows:
- Main goal of sentiment scoring is to determine whether the questionaire participant has a mainly positive, mainly neutral or mainly negative mood
- According to the base level analysis, new questions are presented if the participant wants to continue using the sentiment analyzer
- "Describe your feelings on topic presented" is the main scoring method and it is scored according to the number of positive and negative words found on the answer
- If "Describe your feelings on topic presented" sentiment score is positive, but combined sentiment score of other question types is negative, will the sentiment score be neutral and vice versa
  
