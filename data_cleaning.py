# Methods to clean data from data sources

from data_extraction import DataExtractor
import pandas as pd
import numpy as np

class DataCleaning:

    # class constructor
    def __init__(self):
        #self.df_users = df_user

        #self.clean_user_data()
        return

    def clean_user_data(self):
        # look out for NULL values
        print("Imported data percentage of missing values in each column:")
        print(self.df_users.isna().mean() * 100)
        # errors with dates
        inv_cols = ['join_date', 'date_of_birth']
        for c_cols in inv_cols:
            self.df_users[c_cols] = pd.to_datetime(self.df_users[c_cols], errors='coerce')
        # checking columns with regex expressions 
        inv_cols = {'email_address': '^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$', 'phone_number':'^(\(?\+?[0-9]*\)?)?[0-9_\- \(\)]*$'}
        cols_keys = inv_cols.keys()
        for c_cols in cols_keys:
            print(f'key is {c_cols} value is {inv_cols[c_cols]}')
            self.df_users.loc[~self.df_users[c_cols].str.match(inv_cols[c_cols]), c_cols] = np.nan
       # check amount of data with null, NaT, nan values
        print("percentage of missing values in each column:")
        print(self.df_users.isna().mean() * 100)
        # remove these values
        self.df_users = self.df_users.dropna(axis = 0)
        # recheck
        print("percentage of missing values in each column:")
        print(self.df_users.isna().mean() * 100)
        #change to clean
        self.df_clean = self.df_users
        return self.df_clean
    
    def clean_card_data(self):
        # errors with dates
        print("percentage of missing values in each column:")
        print(self.df_pdf.isna().mean() * 100)
        #self.df_users = self.df_users.dropna(axis = 0)
        inv_cols = ['date_payment_confirmed']
        for c_cols in inv_cols:
            self.df_pdf[c_cols] = pd.to_datetime(self.df_pdf[c_cols], errors='coerce')
        print("percentage of missing values in each column:")
        print(self.df_pdf.isna().mean() * 100)
        n_unique = self.df_pdf['card_number'].nunique()
        print(f'Total records {len(self.df_pdf)}, unique card numbers {n_unique}')
        self.df_pdf = self.df_pdf.drop_duplicates()
        # remove unwanted rows
        self.df_pdf = self.df_pdf.dropna(axis = 0)
        n_unique = self.df_pdf['card_number'].nunique()
        print(f'Total records {len(self.df_pdf)}, unique card numbers {n_unique}')
        self.df_clean = self.df_pdf
        return self.df_clean

    def clean_orders_data(self):
        # errors with dates
        #self.df_users = self.df_users.set_index('index', inplace = True)
        #print(self.df_users.head())
        print("percentage of missing values in each column:")
        print(self.df_users.isna().mean() * 100)
        self.df_clean = self.df_users.drop(columns=['first_name', 'last_name', '1', 'index', 'level_0'])
        print("percentage of missing values in each column:")
        print(self.df_clean.isna().mean() * 100) 
        print(self.df_users.head())                 
        return self.df_clean

    def clean_store_data(self):
        #print(self.df_stores.head())
        print("percentage of missing values in each column:")
        print(self.df_stores.isna().mean() * 100)
        self.df_stores = self.df_stores.dropna(axis = 1)
        inv_cols = ['opening_date']
        for c_cols in inv_cols:
            self.df_stores[c_cols] = pd.to_datetime(self.df_stores[c_cols], errors='coerce')
        self.df_stores = self.df_stores.dropna(axis = 0)
        print("percentage of missing values in each column:")
        print(self.df_stores.isna().mean() * 100)
        n_unique = self.df_stores['store_code'].nunique()
        print(f'Total records {len(self.df_stores)}, unique card numbers {n_unique}')
        self.df_clean = self.df_stores
        return self.df_clean
    
    def convert_product_weights(self):
        # this may need work
        temp = pd.DataFrame()
        temp['mul_no'] = []
        temp['mul_weight'] = []
        temp['units'] = self.df_prod['weight'].str.extract(r'("|g|kg|ml")')
        temp['weight'] = self.df_prod['weight'].str.replace(r'("|g|kg|ml")', '', regex=True)
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
        self.df_prod['weight'] = temp['weight']  
        return self.df_prod
    
    def clean_products_data(self):
        self.df_clean = self.df_prod.dropna(how = 'any', axis = 0)
        return self.df_clean
    
    def clean_dates_data(self):
        # errors with dates
        print("percentage of missing values in each column:")
        print(self.df_dates.isna().mean() * 100)
        self.df_clean = self.df_dates
        print("percentage of missing values in each column:")
        print(self.df_clean.isna().mean() * 100)                 
        return self.df_clean

#test = DataCleaning()