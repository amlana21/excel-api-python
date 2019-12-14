import pandas as pd
from logger import LoggerClass

class Schema:

    def __init__(self,filename):
        self.filename=filename
        self.dataobject=None


    def get_schema(self,logobj):
        tables=[]
        tabledetails={}
        tabledetails['tablemetrics']={}
        logobj.info('Start reading the input data file..')
        df_file=pd.ExcelFile('datafile/{}'.format(self.filename))
        tables=df_file.sheet_names
        tabledetails['tables']=tables
        logobj.info('End reading the input data file..')
        logobj.info('Start cycling through the sheets..')
        for tbl in tables:
            tabledetails['tablemetrics'][tbl]={}
            df_data=df_file.parse(tbl)
            # colname=df_data.columns.tolist()
            # colname[0]='id'
            # df_data.columns=colname
            # df_data.index.names=['id']
            # df_data.set_index('id')
            # print(df_data.columns.tolist())
            df_data.to_csv(f'tables/{tbl}.csv')
            # df_temp=pd.read_csv(f'tables/{tbl}.csv')
            # cols=df_temp.columns.tolist()
            # cols[0]='id'
            # df_temp.columns=cols
            # df_temp.to_csv(f'tables/{tbl}.csv',index=False)
            df_dict={}
            colnames=df_data.columns.tolist()
            rowcount=len(df_data.index)
            tabledetails['tablemetrics'][tbl]['columns']=colnames
            tabledetails['tablemetrics'][tbl]['rows']=rowcount
            for col in colnames:
                # print(df_data[col].nunique())
                df_dict[col]=df_data[col].nunique()
            # print(df_dict)
            highest_count=[col for col,row in df_dict.items() if df_dict[col]==max(df_dict.values())]
            tabledetails['tablemetrics'][tbl]['mostuniquerows']=highest_count[0]
        print(tabledetails)
        self.dataobject=df_file
        logobj.info('End cycling through the sheets and storing file info..')
        return [df_file,tabledetails]





if __name__=='__main__':
    schemaobj=Schema('input_data.xlsx')
    schemaobj.get_schema()