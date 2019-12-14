from crudfunctions import CrudFunctions
import pandas as pd
class UpdateClass(CrudFunctions):

    def __init__(self,tablename,logobj):
        super().__init__(tablename)
        self.logobj=logobj


    def updatebyid(self,id,inpt):
        datdf=self.gettable()

        # datdf.set_index()
        self.logobj.info('Inside updatebyid method. Started dropping the matched row..')
        drow=datdf.iloc[id]
        datdf.drop(id,inplace=True)
        # print(datdf)
        print(drow)
        self.logobj.info('Inside updatebyid method. Started updating the matched row..')
        for k,v in inpt.items():
            drow[k]=v
        print(drow)
        self.logobj.info('Inside updatebyid method. Completed updating the matched row..')
        datdf=datdf.append(drow)
        # print(datdf)
        # datdf = datdf.reset_index()
        datdf.drop(datdf.columns[0], axis=1, inplace=True)
        # datdf.drop(datdf.columns[1], axis=1, inplace=True)
        datdf.sort_index(inplace=True)
        self.logobj.info('Inside updatebyid method. Writing updates to file..')

        datdf.to_csv(f'tables/{self.tablename}.csv')
        indexlist=drow.index.tolist()
        self.logobj.info('Inside updatebyid method. Preparing data to be returned..')
        retdict={'id':int(drow.iloc[0]),indexlist[1]:str(drow.iloc[1]),indexlist[2]:drow.iloc[2]}
        print(retdict)
        return retdict

    def updatebycond(self,condition,inpt):
        datdf = self.gettable()
        tmpdf=datdf.copy()
        self.logobj.info('Inside updatebycond method. Started reading input conditions and matching to data..')
        for k,v in condition.items():
            tmpdf=tmpdf[tmpdf[k]==v]
        self.logobj.info('Inside updatebycond method. Completed reading input conditions and matching to data..')
        self.logobj.info('Inside updatebycond method. Started dropping matched rows..')

        datdf.drop(tmpdf.index.tolist(),inplace=True)
        self.logobj.info('Inside updatebycond method. Completed dropping matched rows..')

        self.logobj.info('Inside updatebycond method. Started updating the rows..')
        for k,v in inpt.items():
            tmpdf[k]=tmpdf[k].apply(lambda x:v)
        self.logobj.info('Inside updatebycond method. Completed updating the rows..')

        # for i,rw in tmpdf.iterrows():
        #     for k,v in inpt.items():
        #         rw[k]=v
        #     # print(rw)
        print(tmpdf)

        for i,rw in tmpdf.iterrows():
            datdf = datdf.append(rw)
        datdf.drop(datdf.columns[0], axis=1, inplace=True)
            # datdf.drop(datdf.columns[len(datdf.columns)-1], axis=1, inplace=True)
        datdf.sort_index(inplace=True)

        self.logobj.info('Inside updatebycond method. Started writing to file..')
        datdf.to_csv(f'tables/{self.tablename}.csv')
        # ------ will be activated
        print(datdf)

        self.logobj.info('Inside updatebycond method. Preparing data to be returned..')
        indexlist = tmpdf.index.tolist()
        collist=tmpdf.columns.tolist()
        retdict=[]
        for i,rw in tmpdf.iterrows():
            tmpdict={}
            tmpdict = {'id': int(rw.iloc[0]), collist[1]: str(rw.iloc[1]), collist[2]: rw.iloc[2]}
            retdict.append(tmpdict)


        print(retdict)
        # retdict = {'id': int(tmpdf.iloc[0]), indexlist[1]: str(tmpdf.iloc[1]), indexlist[2]: tmpdf.iloc[2]}
        # print(retdict)
        return retdict


        # print(datdf)

if __name__=='__main__':

    updateobj=UpdateClass('accounts')
    updateobj.updatebycond({'account name':'abc3','type':'account'},{'revenue':200,'owner':'newuser1'})
