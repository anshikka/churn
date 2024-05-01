import os,sys
import csv


def main():
    with open('/Users/anshsikka/Documents/Personal/Projects/churn/backend/data/cc_networks.csv') as creditcards_csv:
        csv_reader = csv.reader(creditcards_csv, delimiter=',',)
        networks = []
        next(csv_reader, None) # skip header
        for row in csv_reader:
            id = int(row[0])
            name = row[1]
            open_or_closed = row[2]
            logo = row[3]
            networks.append([id, name, open_or_closed, logo])
        sys.path.append(os.path.abspath('..'))
        from utils import db_utils
        churn_db_handler = db_utils.ChurnDBConnectionHandler()
        churn_db_handler.connect()
        churn_db_handler.bulk_insert_if_not_exists(networks, ['id', 'name', 'open_or_closed', 'logo'], 'public.creditcard_network', 'id')
        churn_db_handler.record_load_timestamp('public.creditcard_network', os.path.basename(__file__) )


