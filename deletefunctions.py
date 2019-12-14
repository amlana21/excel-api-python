from crudfunctions import CrudFunctions
from logger import LoggerClass
import pandas as pd

class DeleteClass(CrudFunctions):

    def __init__(self, tablename,logobj):
        super().__init__(tablename)
        logobj1=LoggerClass(__name__)
        self.logobj=logobj


    def delbyid(self,id):
        self.logobj.info('Inside Delete by id method.Starting deletion....')
        datdf = self.gettable()
        # datdf = datdf.reset_index()

        # datdf.set_index()
        drow = datdf.iloc[id]
        print(datdf)
        datdf.drop(id, inplace=True)

        # print(drow)
        # for k, v in inpt.items():
        #     drow[k] = v
        # print(drow)
        # datdf = datdf.append(drow)
        # print(datdf)
        # datdf = datdf.reset_index()
        datdf.drop(datdf.columns[0], axis=1, inplace=True)
        datdf = datdf.reset_index()
        datdf.drop(datdf.columns[0], axis=1, inplace=True)
        datdf.sort_index(inplace=True)
        print(datdf)

        self.logobj.info('Inside Delete by id method.Writing to file....')
        datdf.to_csv(f'tables/{self.tablename}.csv')
        indexlist = drow.index.tolist()
        self.logobj.info('Inside Delete by id method.Preparing data to be returned....')
        retdict = {'id': int(drow.iloc[0]), indexlist[1]: str(drow.iloc[1]), indexlist[2]: drow.iloc[2]}
        print(retdict)
        return retdict

    def delbyfields(self,condition):
        datdf = self.gettable()
        tmpdf = datdf.copy()
        print(datdf)
        self.logobj.info('Inside Delete by fields method.Reading inputs and matching records....')
        for k, v in condition.items():
            tmpdf = tmpdf[tmpdf[k] == v]

        self.logobj.info('Inside Delete by fields method.Deleting records....')
        datdf.drop(tmpdf.index.tolist(), inplace=True)

        # for k, v in inpt.items():
        #     tmpdf[k] = tmpdf[k].apply(lambda x: v)

        # for i,rw in tmpdf.iterrows():
        #     for k,v in inpt.items():
        #         rw[k]=v
        #     # print(rw)
        # print(tmpdf)
        #
        # for i, rw in tmpdf.iterrows():
        #     datdf = datdf.append(rw)
        datdf.drop(datdf.columns[0], axis=1, inplace=True)
        datdf=datdf.reset_index()
        # datdf.drop(datdf.columns[0], axis=1, inplace=True)

        # datdf.drop(datdf.columns[len(datdf.columns)-1], axis=1, inplace=True)
        datdf.drop(datdf.columns[0], axis=1, inplace=True)
        datdf.sort_index(inplace=True)

        self.logobj.info('Inside Delete by fields method.Writing to file....')
        datdf.to_csv(f'tables/{self.tablename}.csv')
        # ------ will be activated
        print(datdf)

        indexlist = tmpdf.index.tolist()
        collist = tmpdf.columns.tolist()
        retdict = []
        for i, rw in tmpdf.iterrows():
            tmpdict = {}
            tmpdict = {'id': int(rw.iloc[0]), collist[1]: str(rw.iloc[1]), collist[2]: rw.iloc[2]}
            retdict.append(tmpdict)

        self.logobj.info('Inside Delete by fields method.Finished preparing data to be returned....')
        # print(retdict)
        # retdict = {'id': int(tmpdf.iloc[0]), indexlist[1]: str(tmpdf.iloc[1]), indexlist[2]: tmpdf.iloc[2]}
        print(retdict)
        return retdict


if __name__=='__main__':
    delobj=DeleteClass('accounts')
    # delobj.delbyid(4)
    # delobj.delbyfields({'account name':'abc3','type':'account'})