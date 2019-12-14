import pandas as pd


class CrudFunctions:

    def __init__(self,tablename):
        self.tablename=tablename

    def gettable(self):
        df_data=pd.read_csv(f'tables/{self.tablename}.csv',index_col=False)
        return df_data