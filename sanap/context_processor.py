
from sanap.model_data import *

def model_data_context():
    return {
        'COUNTRIES': dict(COUNTRIES),
        'LANGUAGES': dict(LANGUAGES),
        'Q': Q,
    }
