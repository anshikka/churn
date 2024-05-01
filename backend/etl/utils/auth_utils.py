import oauth1.authenticationutils as authenticationutils
from oauth1.oauth_ext import OAuth1RSA
import configparser

config = configparser.ConfigParser()
config.read('/Users/anshsikka/Documents/Personal/Projects/churn/backend/config/api.ini')

def get_signing_key():
    return authenticationutils.load_signing_key(config['mastercard_api']['pkcs12_filename'], config['mastercard_api']['password'])

def get_oauth():
    signing_key = get_signing_key()
    return OAuth1RSA(consumer_key=config['mastercard_api']['consumer_key'], signing_key=signing_key)
