# Methods to clean data from data sources

# Imported libaries
from data_extraction import DataExtractor
import numpy as np
import pandas as pd


class DataCleaning:

    # class constructor
    def __init__(self):
        """Inintailises the class"""
        return
    
    def clean_na_in_data(self):
        """
        Remove na data with numerical analysis

        Keyword arguments:
        self -- variables that store information unique to each 
        object created from the class
        """
        # Remove na data with numerical analysis
        print("percentage of missing values in each column:")
        print(self.df_tran.isna().mean() * 100)
        self.df_clean = self.df_tran.dropna(how = 'any', axis = 0)
        print("percentage of missing values in each column:")
        print(self.df_clean.isna().mean() * 100)                
        return self.df_clean

    def clean_user_data(self):
        """
        Cleans user data

        Keyword arguments:
        self -- variables that store information unique to each 
        object created from the class
        """
        # errors with dates
        inv_cols = ['join_date', 'date_of_birth']
        for c_cols in inv_cols:
            self.df_tran[c_cols] = pd.to_datetime(self.df_tran[c_cols], errors='coerce')
        # checking columns with regex expressions 
        inv_cols = {'email_address': '^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$', 'phone_number':'^(\(?\+?[0-9]*\)?)?[0-9_\- \(\)]*$'}
        cols_keys = inv_cols.keys()
        for c_cols in cols_keys:
            print(f'key is {c_cols} value is {inv_cols[c_cols]}')
            self.df_tran.loc[~self.df_tran[c_cols].str.match(inv_cols[c_cols]), c_cols] = np.nan
       # check amount of data with null, NaT, nan values
        self.clean_na_in_data()
        return self.df_clean
    
    def clean_card_data(self):
        """
        Cleans card data

        Keyword arguments:
        self -- variables that store information unique to each 
        object created from the class
        """
        # errors with dates
        inv_cols = ['date_payment_confirmed']
        for c_cols in inv_cols:
            self.df_tran[c_cols] = pd.to_datetime(self.df_tran[c_cols], errors='coerce')
        n_unique = self.df_tran['card_number'].nunique()
        print(f'Total records {len(self.df_tran)}, unique card numbers {n_unique}')
        self.df_tran = self.df_tran.drop_duplicates()
        # remove unwanted rows
        self.clean_na_in_data()
        n_unique = self.df_clean['card_number'].nunique()
        print(f'Total records {len(self.df_clean)}, unique card numbers {n_unique}')
        return self.df_clean

    def clean_orders_data(self):
        """
        Cleans orders data

        Keyword arguments:
        self -- variables that store information unique to each 
        object created from the class
        """
        print("percentage of missing values in each column:")
        print(self.df_tran.isna().mean() * 100)
        self.df_clean = self.df_tran.drop(columns=['first_name', 'last_name', '1', 'index', 'level_0'])
        print("percentage of missing values in each column:")
        print(self.df_clean.isna().mean() * 100)                 
        return self.df_clean

    def clean_store_data(self):
        """
        Cleans store data

        Keyword arguments:
        self -- variables that store information unique to each 
        object created from the class
        """
        inv_cols = ['opening_date']
        for c_cols in inv_cols:
            self.df_tran[c_cols] = pd.to_datetime(self.df_tran[c_cols], errors='coerce')
        
        n_unique = self.df_tran['store_code'].nunique()
        print(f'Total records {len(self.df_tran)}, unique card numbers {n_unique}')
        self.df_clean = self.df_tran
        return self.df_clean
    
    def convert_product_weights(self):
        """
        Converst products weights from g and ml to kg

        Keyword arguments:
        self -- variables that store information unique to each 
        object created from the class
        """
        # this may need work
        temp = pd.DataFrame()
        temp['mul_no'] = []
        temp['mul_weight'] = []
        temp['units'] = self.df_tran['weight'].str.extract(r'("|g|kg|ml")')
        temp['weight'] = self.df_tran['weight'].str.replace(r'("|g|kg|ml")', '', regex=True)
        temp['weight'] = temp['weight'].astype(str)
        temp.insert(4,'multi',temp['units'])
        for n in range(0,len(temp)):
            if ' x ' in temp.iloc[n,3]:
               temp.iloc[n,0], temp.iloc[n,1] = temp.iloc[n,3].split(' x ')
            if ' .' in temp.iloc[n,3]:
                temp.iloc[n,3] = temp.iloc[n,3].replace(" .", "")
        temp['mul_no'] = temp['mul_no'].astype(float)
        temp['mul_weight'] = temp['mul_weight'].astype(float)
        for n in range(0,len(temp)):
            if 'x' in temp.iloc[n,3]:
                temp.iloc[n,3] = temp.iloc[n,0] * temp.iloc[n,1]
            if temp.iloc[n,2] == 'NaN':
                temp.iloc[n,3] = 'NaN'
            if  temp.iloc[n,2] == 'g':
               temp.iloc[n,3] = float(temp.iloc[n,3]) / 1000
               temp.iloc[n,2] = 'kg'
        self.df_tran['weight'] = temp['weight']  
        return self.df_tran
    

    
    
    
    
