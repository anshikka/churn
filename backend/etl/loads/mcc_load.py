import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.api_utils import MasterCardAPI
from utils import db_utils

def main():
    mastercard_api = MasterCardAPI()
    churn_db_handler = db_utils.ChurnDBConnectionHandler()
    churn_db_handler.connect()
    mcc_categories = mastercard_api.get_all_mcc_codes()
    churn_db_handler.bulk_insert_if_not_exists(mcc_categories, ['mcc_code', 'name'], 'public.mcc', 'mcc_code')
    churn_db_handler.record_load_timestamp('public.mcc', os.path.basename(__file__) )
