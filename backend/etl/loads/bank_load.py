import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.api_utils import FDICAPI
from utils import db_utils

def main():
    fdic_api = FDICAPI()
    churn_db_handler = db_utils.ChurnDBConnectionHandler()
    churn_db_handler.connect()
    banking_institutions = fdic_api.get_all_institutions()
    churn_db_handler.bulk_insert_if_not_exists(banking_institutions, ['id', 'name'], 'public.bank', 'id')
    churn_db_handler.record_load_timestamp('public.bank', os.path.basename(__file__) )
