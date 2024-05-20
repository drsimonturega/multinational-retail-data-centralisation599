import yaml
from sqlalchemy import create_engine
from sqlalchemy import inspect
from data_extraction import DataExtractor
from data_cleaning import DataCleaning

#import pandas as pd

# Methods to connect with and upload data to the database
class DatabaseConnector(DataExtractor, DataCleaning):

    # class constructor
    def __init__(self):

        # attributes
        #self.cred_file = cred_file
        #self.tab_name = tab_name
        #self.cred_dict = dict()
        #self.df_users = df_users

        #self.read_db_creds()
        #self.cur_con = DatabaseConnector('db_creds.yaml') 
        return
        

    # load db credentials from a *.ymal file
    def read_db_creds(self, cred_file,):  # can add external arguments
        with open(f'{cred_file}') as f:
            self.cred_dict = yaml.load(f, Loader=yaml.FullLoader)
        self.init_db_engine()
        return self.cred_dict 
    
    # read credentials, initialise and return an sqlalchemy db engine
    def init_db_engine(self):  # can add external arguments
        self.engine = create_engine(f"postgresql+psycopg2://{self.cred_dict['RDS_USER']}:{self.cred_dict['RDS_PASSWORD']}@{self.cred_dict['RDS_HOST']}:{self.cred_dict['RDS_PORT']}/{self.cred_dict['RDS_DATABASE']}")
        self.engine.execution_options(isolation_level='AUTOCOMMIT').connect()
        self.engine.connect()
        return self.engine 
    
    
    def list_db_tables(self):  # can add external arguments
        inspector = inspect(self.engine)
        self.tab_lst = inspector.get_table_names()
        print(f'here is {self.tab_lst}')
        return self.tab_lst
    
    def upload_to_db(self, tab_name):
        print(self.df_clean.head())
        self.df_clean.to_sql(tab_name, self.engine, if_exists='replace')
        inspector = inspect(self.engine)
        print(inspector.get_table_names())
        return

        
    
up_ld = DatabaseConnector()
DatabaseConnector.read_db_creds(up_ld, 'db_creds.yaml')
DatabaseConnector.list_db_tables(up_ld)
DataExtractor.read_rds_table(up_ld, 'users')
DataCleaning.clean_user_data(up_ld)
DatabaseConnector.read_db_creds(up_ld, 'db_creds_II.yaml')

DatabaseConnector.upload_to_db(up_ld, 'dim_users')
DataExtractor.retrieve_pdf_data(up_ld, 'https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf')
DataCleaning.clean_card_data(up_ld)
DatabaseConnector.upload_to_db(up_ld, 'dim_card_details')
DataExtractor.list_number_of_stores(up_ld)
DataExtractor.retrieve_stores_data(up_ld)
DataCleaning.clean_store_data(up_ld)
DatabaseConnector.upload_to_db(up_ld, 'dim_store_details')
DataExtractor.extract_from_s3(up_ld)
DataCleaning.convert_product_weights(up_ld)
DataCleaning.clean_products_data(up_ld)
DatabaseConnector.upload_to_db(up_ld, 'dim_products')
DatabaseConnector.read_db_creds(up_ld, 'db_creds.yaml')
DatabaseConnector.list_db_tables(up_ld)
DataExtractor.read_rds_table(up_ld, 'orders')
DataCleaning.clean_orders_data(up_ld)
DatabaseConnector.read_db_creds(up_ld, 'db_creds_II.yaml')
DatabaseConnector.upload_to_db(up_ld, 'order_table')

DatabaseConnector.read_db_creds(up_ld, 'db_creds.yaml')
DatabaseConnector.list_db_tables(up_ld)
DataExtractor.extract_dates_s3(up_ld)
DataCleaning.clean_dates_data(up_ld)
DatabaseConnector.read_db_creds(up_ld, 'db_creds_II.yaml')
DatabaseConnector.upload_to_db(up_ld, 'dim_date_times')

