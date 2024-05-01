import psycopg2
import configparser
from psycopg2.extras import execute_batch


class ChurnDBConnectionHandler:
    def __init__(self):
        self.conn = None

    def connect(self):
        try:
            config = configparser.ConfigParser()
            config.read('/Users/anshsikka/Documents/Personal/Projects/churn/backend/config/db.ini')
            with psycopg2.connect(host=config['postgresql']['host'], database=config['postgresql']['database'], user=config['postgresql']['user'], password=config['postgresql']['password']) as self.conn:
                print('Connected to the PostgreSQL server.')
                return self.conn
        except (psycopg2.DatabaseError, Exception) as error:
            print("Could not connect to postgres server.")
    
    def bulk_insert_if_not_exists(self, data, columns, table, key):
        cur = self.conn.cursor()
        columns_str = ",".join(columns)
        params_str = ",".join(['%s' for p in columns])
        query_str = """
        WITH source({}) as (values ({}) )
        insert into {} ({})
        SELECT {} FROM source s
        WHERE NOT EXISTS (
        SELECT 1 FROM {} target WHERE target.{} = s.{} 
        )
        
        """.format(columns_str, params_str, table, columns_str, columns_str, table, key, key)
        execute_batch(cur, query_str , data)
        rowcount = cur.rowcount
        self.conn.commit()
        print("Successfully inserted " + str(rowcount) + " rows into " + table + ".")


    def record_load_timestamp(self, table_name, script_name):
        cur = self.conn.cursor()
        data = (table_name, script_name)
        query_str = """
            INSERT INTO metadata.etl_log (table_name, script_name)
            VALUES (%s, %s)
        """
        cur.execute(query_str, data)
        self.conn.commit()