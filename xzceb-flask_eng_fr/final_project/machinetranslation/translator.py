"""System module."""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)



def english_to_french(englishtext):
    frenchtextdic = json.dumps(language_translator.translate(text=englishtext, \
     model_id='en-fr').get_result(), indent=2, ensure_ascii=False)
    frenchtext= json.loads(frenchtextdic)
    return frenchtext["translations"][0]["translation"]

def french_to_english(frenchtext):
    englishtextdic = json.dumps(language_translator.translate(text=frenchtext, \
     model_id='fr-en').get_result(), indent=2, ensure_ascii=False)
    englishtext= json.loads(englishtextdic)
    return englishtext["translations"][0]["translation"]
    