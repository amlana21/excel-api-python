import pandas as pd
from crudfunctions import CrudFunctions

class CreateClass(CrudFunctions):

    def __init__(self,tablename,logobj):
        super().__init__(tablename)
        self.logobj=logobj

    def addrows(self,inputdict):
        dataf=self.gettable()
        # dataf=dataf.set_index('id')
        lastindex = len(dataf.index) - 1
        self.logobj.info('Inside add single row method.Adding new row..')
        dataf=dataf.append(inputdict,ignore_index=True)
        # cols=dataf.columns.tolist()
        # cols[0]='id'
        # dataf.columns=cols
        dataf.drop(dataf.columns[0],axis=1,inplace=True)
        self.logobj.info('Inside add single row method.Writing to file..')
        dataf.to_csv(f'tables/{self.tablename}.csv')
        lastindex += 1
        inputdict['id']=lastindex
        self.logobj.info('Inside add single row method.Completed writing to file..')
        return inputdict

    def addmultiple(self,inputlist):
        dataf=self.gettable()
        lastindex=len(dataf.index)-1
        print(lastindex)
        outputarray=[]
        self.logobj.info('Inside add multiple rows method.Cycling through input rows..')
        for inp in inputlist:
            dataf=dataf.append(inp,ignore_index=True)
            # cols=dataf.columns.tolist()
            # cols[0]='id'
            # dataf.columns=cols
            dataf.drop(dataf.columns[0],axis=1,inplace=True)
            dataf.to_csv(f'tables/{self.tablename}.csv')
            lastindex+=1
            inp['id']=lastindex
            outputarray.append(inp)
        self.logobj.info('Inside add multiple rows method.Completed adding rows..')
        return outputarray



if __name__=='__main__':
    testobj=CreateClass('accounts')
    testobj.addrows({'rowid':'2245'})
