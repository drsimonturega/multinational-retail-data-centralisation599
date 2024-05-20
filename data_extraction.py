# This class will contain methods that extract data from a particular 
# data source, these sources will include CSV files, an API 
# and an S3 bucket.

# Imported libaries
import boto3
import numpy as np
import pandas as pd
import requests
import tabula

class DataExtractor:

    # class constructor
    def __init__(self):
        """Inintailises the class"""
        return
        
    def read_rds_table(self, tb_name):  # can add external arguments
        """
        Extracts tables from a data base

        Keyword arguments:
        self -- variables that store information unique to each 
        object created from the class
        tb_name -- name of new data base table to be extracted
        """
        for tab in self.tab_lst:
            name = (f'df_{tb_name}')
            if tb_name in tab:
                self.df_tran = pd.read_sql_table(tab, self.engine)
                break       
        return  self.df_tran
    
    def retrieve_pdf_data(self, pdf_lnk):
        """
        Retrieves pdf data from a *.pdf file

        Keyword arguments:
        self -- variables that store information unique to each 
        object created from the class
        pdf_lnk -- address of *.pdf files we want to extract data from
        """
        self.df_tran = tabula.read_pdf(pdf_lnk, output_format = 'dataframe', pages='all')
        self.df_tran = pd.DataFrame(self.df_tran[0])
        return self.df_tran
    
    def list_number_of_stores(self):
        """
        List number of stores

        Keyword arguments:
        self -- variables that store information unique to each 
        object created from the class
        """
        url = 'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores'
        headers = {'x-api-key': 'yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX'}
        self.n_stores = requests.get(url, headers=headers)
        self.n_stores = self.n_stores.json()
        self.n_stores = self.n_stores['number_stores'] 
        return self.n_stores
    
    def retrieve_stores_data(self):
        """
        Retrieves store data

        Keyword arguments:
        self -- variables that store information unique to each 
        object created from the class
        """
        headers = {'x-api-key': 'yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX'}
        df_stores = pd.DataFrame()
        for n in range(1, self.n_stores):
            url = (f'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/{n}')
            stores_trans = requests.get(url, headers=headers)
            stores_trans = stores_trans.json()
            col_lst = stores_trans.keys()
            val_lst = stores_trans.values()
            self.df_tran = pd.DataFrame([val_lst])
            self.df_tran.columns = col_lst
            self.df_tran = pd.concat([df_stores, self.df_tran])
        self.df_tran.set_index('index', inplace = True)
        return self.df_tran
    
    def extract_from_s3(self):
        """
        Extracts df from S3 bucket

        Keyword arguments:
        self -- variables that store information unique to each 
        object created from the class
        """
        s3 = boto3.client('s3')
        response = s3.get_object(Bucket='data-handling-public', Key='products.csv')
        self.df_tran = pd.read_csv(response.get("Body"))
        col_lst = self.df_tran.columns.values.tolist()
        col_lst[0] = 'index'
        self.df_tran.columns = col_lst
        self.df_tran.set_index('index', inplace = True)
        return self.df_tran
    
    def extract_dates_s3(self):
        """
        Extracts df from S3 bucket

        Keyword arguments:
        self -- variables that store information unique to each 
        object created from the class
        """
        s3 = boto3.client('s3')
        response = s3.get_object(Bucket='data-handling-public', Key='date_details.json')
        self.df_tran = response["Body"].read().decode()
        self.df_tran = pd.read_json(self.df_tran)
        return self.df_tran


