# %%
import en_core_web_sm
from nltk import text
from string import punctuation
import nltk
nltk.download("wordnet")
nltk.download('omw-1.4')
from nltk.corpus import wordnet
nlp = en_core_web_sm.load()


# %%
def get_synonyms(word):
    synonyms = wordnet.synsets(word)
    syns = []
    for item in synonyms:
        for name in item.lemma_names():
            syns.append(name)
    return syns

# %%
def get_keywords(text):
    result = []
    pos_tag = ['PROPN', 'ADJ', 'NOUN', 'VERB']
    doc = nlp(text.lower())
    for token in doc:
        
        if(token.text in nlp.Defaults.stop_words or token.text in punctuation):
            continue
        
        if(token.pos_ in pos_tag):
            result.append(token.text)
                
    return result 


# %%
def tone_analyzer(text):
    import json
    from ibm_watson import ToneAnalyzerV3
    from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

    authenticator = IAMAuthenticator("gBM315juVfKWlIiEzn4uNyvhIO3JVy3CKKR8hnWZfMlD")
    tone_analyzer = ToneAnalyzerV3(
        version='2017-09-21',
        authenticator=authenticator
    )

    tone_analyzer.set_service_url("https://api.us-south.tone-analyzer.watson.cloud.ibm.com/instances/afd81026-a1c6-4e99-a7fb-cf368ae87909")


    tone_analysis = tone_analyzer.tone(
        {'text': text},
        content_type='application/json'
    ).get_result()
    # print(tone_analysis)
    result = []
    for i in range(len(tone_analysis["document_tone"]["tones"])):
        result.append((tone_analysis["document_tone"]["tones"][i]["score"], tone_analysis["document_tone"]["tones"][i]["tone_name"]))
    return result


# %%



