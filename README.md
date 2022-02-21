
# Project Title

Customer Satisfaction Evaluation Project

## Project Description

We have created an algorithm, That, when given a data set containing respective datestamps and chats done with a chatbox, returns how well the chatbox performed and how much satisfied the end customers are based on Latency, Flow of conversation / Tone and accuracy. 
## Youtube Link
Link for our video submission:
https://youtu.be/PV1-O6z1_YA
## Authors

- [@Harsh Bishnoi](https://github.com/premJyotish007)
- [@Ayush Gupta](https://github.com/ayushg5)
- [@Pranshu Tekchandani](https://www.github.com/pat4)
- [@Sidharth Jain](https://github.com/jainsidharth420)



# Model

In our research for customer satisfaction, we found that clients mainly look for these three things in customer service - 


## Latency - Average response time:

Our algorithm looks at the timestamps at the beginning and end of the conversation as well as the net sum of events, inputs, and responses in one conversation to determine a turnaround/latency time in seconds/msg
Taking into account the unimodal, highly right skewed histogram, and close resemblance to a gaussian fit, we devised a percentile-based scoring system for time decrements.


Algorithm for devising percentile:

    times.sort() 

    percentiles = []

    percentile = 100

    for i in index(len(times)):

                if (times[i] - times[i - 1] >= 0.05):
                    percentile--;
                percentiles.append(percentile)
                if (percentile == 0):
                    break
Summary: decrease percentile by 1 if and only if a change in time of more than 50 milliseconds is observed

Key insights:
Because of the closely clustered nature of the data, we observed that the mean percentile score is relatively high at 84 with 0 percentile mapping to 32 seconds of response time and 100 percentile mapping to a 100% chatbot driven conversation of 0.11 seconds/msg.
Final conclusion: Any time with a score of 84 or greater, i.e. corresponding to a mean response time of 12.47 or less seconds is considered “customer satisfactory”.
		



## Flow of conversation:

Even before applying a filter of analyzing the content of conversation, we check to see the general flow of the conversation:
looking for common indicators such as-

1. Number of non responsive inputs or breaks in time sequence

2. Number of Unique elements

3. Statements indicating apology or incompetence

We believe Unique state is good. Repitions confuse and frustate the user, so are usually bad. Also, sorry's are usually followed by failure to deliver, so we also count the sorry's as negatives. 


Algorithm for scoring is as follows:

    for (convo in conversation):
        ignore lag as an exception to unique elements in convo
        score = 2 * (unique_statements_in_convo) - k * (total number of redundant response states) - sorry_count_in_convo


## Tone and Accuracy:

Tone can be calculated by running Natural language processing algorithms on our data set:
    
    1. Synonym lemmatization
    2. Keyword matching
    3. IBM Tone analyzer

Satisfaction can be measured by the occurrence of satisfactory words, and also the percentage match in the input provided and the output returned. 



## Final algorithm to calculate how good our algorithm is
    Final score = 0.33 * (time_score) + 0.33 * (conversational_flow_score) + 0.33 * (similarity_tone_score)

    
    Based The mean would serves as a benchmark for satisfactory experiences 
    Benchmark Final score = 0.33 * (mean_time_score) + 0.33 * (mean_conversational_flow_score) + 0.33 * (mean_similarity_tone_score)
    = 0.33 * 84.3057296329453 + 0.33 * 14.334067547723935 + 0.33 * (mean_similarity_tone_score)



## Installation



```bash
import nltk
import spacy

pip install pandas 
pip install numpy
import numpy as np
from scipy import stats
import math
import matplotlib
from matplotlib import pyplot as plt
import en_core_web_sm
from nltk import text
from string import punctuation
import nltk
nltk.download("wordnet")
nltk.download('omw-1.4')
from nltk.corpus import wordnet
nlp = en_core_web_sm.load()
import json
    from ibm_watson import ToneAnalyzerV3
    from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import ToneAnalyzerV3
    from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
