import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ['apikey']
url = os.environ['url']

def watson_connect(apikey, url):
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
    version = '2018-05-01',
    authenticator=authenticator
    )
    language_translator.set_service_url(url)
    return language_translator

translator = watson_connect(api_key, url)

def english_to_french(english_text):
    #write the code here
    try:
        french_text = translator.translate(
        text = english_text,
        model_id = 'en-fr').get_result()["translations"][0]["translation"]
        return french_text
    except ValueError:
        return "missing"

def french_to_english(french_text):
    #write the code here
    try:
        english_text = translator.translate(
        text = french_text,
        model_id='fr-en').get_result()["translations"][0]["translation"]
        return english_text
    except ValueError:
        return "missing"
