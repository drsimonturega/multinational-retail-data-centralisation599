# This class will contain methods that extract data from a particular 
# data source, these sources will include CSV files, an API 
# and an S3 bucket.

#from database_utils import DatabaseConnector
import pandas as pd
import numpy as np
import tabula
import requests
import boto3
#import json

class DataExtractor:

    # class constructor
    def __init__(self):
        #self.tab_lst = tab_lst
        #self.engine = engine
        #self.read_rds_table()
        return
        


    # methods
    def read_rds_table(self, tb_name):  # can add external arguments
        for tab in self.tab_lst:
            name = (f'df_{tb_name}')
            if tb_name in tab:
                self.df_tran = pd.read_sql_table(tab, self.engine)
                break       
        return  self.df_tran
    
    def retrieve_pdf_data(self, pdf_lnk):
        self.df_tran = tabula.read_pdf(pdf_lnk, output_format = 'dataframe', pages='all')
        self.df_tran = pd.DataFrame(self.df_tran[0])
        print(self.df_tran.head())
        print(self.df_tran.info())
        return self.df_tran
    
    def list_number_of_stores(self):
        url = 'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores'
        headers = {'x-api-key': 'yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX'}
        self.n_stores = requests.get(url, headers=headers)
        self.n_stores = self.n_stores.json()
        self.n_stores = self.n_stores['number_stores'] 
        return self.n_stores
    
    def retrieve_stores_data(self):
        headers = {'x-api-key': 'yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX'}
        self.df_stores = pd.DataFrame()
        for n in range(1, self.n_stores):
            url = (f'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/{n}')
            self.stores_trans = requests.get(url, headers=headers)
            self.stores_trans = self.stores_trans.json()
            col_lst = self.stores_trans.keys()
            val_lst = self.stores_trans.values()
            self.df_tran = pd.DataFrame([val_lst])
            self.df_tran.columns = col_lst
            self.df_tran = pd.concat([self.df_stores, self.df_tran])
        self.df_tran.set_index('index', inplace = True)
        print(self.df_tran.head())
        return self.df_tran
    
    def extract_from_s3(self):
        s3 = boto3.client('s3')
        response = s3.get_object(Bucket='data-handling-public', Key='products.csv')
        self.df_tran = pd.read_csv(response.get("Body"))
        col_lst = self.df_tran.columns.values.tolist()
        col_lst[0] = 'index'
        self.df_tran.columns = col_lst
        self.df_tran.set_index('index', inplace = True)
        print(self.df_tran.head())
        return self.df_tran
    
    def extract_dates_s3(self):
        s3 = boto3.client('s3')
        response = s3.get_object(Bucket='data-handling-public', Key='date_details.json')
        self.df_tran = response["Body"].read().decode()
        self.df_tran = pd.read_json(self.df_tran)
        print(self.df_tran.head())
        return self.df_tran


