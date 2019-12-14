import pandas as pd
from genschema import Schema
class QueryClass:

    # def __init__(self,dataobj):
    #     self.dataobj=dataobj
    def __init__(self,datatable,logobj):
        self.datatable=datatable
        self.logobj=logobj

    def starquery(self):
        # tablename=kwargs['table']
        # df_data=self.dataobj.parse(tablename)
        self.logobj.info('Inside query class. Start of file reading..')
        df_data=pd.read_csv(f'tables/{self.datatable}.csv')
        self.logobj.info('Inside query class. Completed file reading..')
        print(df_data.columns)
        return df_data

    def conditionquery(self,**kwargs):
        # tablename=kwargs['table']
        self.logobj.info('Inside query class. Reading query input conditions..')
        inp=kwargs['input']
        queydict={k:v for k,v in inp.items()}
        print(queydict)
        self.logobj.info('Inside query class. Start of file reading..')
        df_data=pd.read_csv(f'tables/{self.datatable}.csv')
        self.logobj.info('Inside query class. Completed file reading..')
        df_out=None
        self.logobj.info('Inside query class. Preparing data to be returned back..')
        for k,v in queydict.items():
            df_data=df_data[df_data[k]==v]
        self.logobj.info('Inside query class. Completed preparing data to be returned back..')
        print(df_data)
        return df_data

    # def starquery(self,**kwargs):
    #     tablename=kwargs['table']
    #     # df_data=self.dataobj.parse(tablename)
    #     df_data=pd.read_csv(f'tables/{tablename}.csv')
    #     print(df_data.columns)
    #     return df_data

    # def conditionquery(self,**kwargs):
    #     tablename=kwargs['table']
    #     queydict={k:v for k,v in kwargs.items() if k!='table'}
    #     print(queydict)
    #     df_data=self.dataobj.parse(tablename)
    #     df_out=None
    #     for k,v in queydict.items():
    #         df_data=df_data[df_data[k]==v]
    #     print(df_data)
    #     return df_data


    def conditionalquery(self,querystr):

        pass

# schemaobj=Schema('input_data.xlsx')
# dataobject=schemaobj.get_schema()
# queryobj=QueryClass(dataobject)
#
# # queryobj.starquery(table='accounts')
# queryobj.conditionquery(table='accounts',type='account',owner='abcuser1')
