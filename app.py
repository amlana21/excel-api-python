from flask import Flask, make_response, jsonify, request
from genschema import Schema
from queryfunctions import QueryClass
from createfunc import CreateClass
from updatefuncs import UpdateClass
from deletefunctions import DeleteClass
from logger import LoggerClass
import traceback
import pickle

app = Flask(__name__)

schemaobj = Schema("input_data.xlsx")


@app.route("/")
def index():
    return "testing"


@app.route("/initiate", methods=["GET"])
def getschema():
    loggerobj = LoggerClass('getschema')
    logobj = loggerobj.getLogger()
    try:

        logobj.info('Starting schema process..')
        schema_inst = schemaobj.get_schema(logobj)
        logobj.info('End schema process..')
        print(schema_inst)
        # Pickle the object
        # with open('schemaobj','wb') as schema_out:
        #     pickle.dump(schemaobj,schema_out)
        # dict_1={'test':schemaobj}
        # filename = 'schemaobj1'
        # outfile = open(filename,'wb')
        # pickle.dump(dict_1,outfile)
        # outfile.close()
        logobj.info('Start generating API response..')
        resp = make_response(
            jsonify(status="success", schemadetails=schema_inst[1]), 200
        )
        logobj.info('End generating API response..')
    except Exception as e:
        
        errmsg=traceback.format_exc()
        logobj.error(f'Error: {errmsg}')
        resp = make_response(
            jsonify(
                status="error",
                errormessage="error in initializing the schema.Check system logs for details.",
            ),
            500,
        )
    logobj.info('Sending response and completing schema process..')
    return resp


@app.route("/query/<tablename>")
def queryfuncs(tablename):
    loggerobj = LoggerClass('query')
    logobj = loggerobj.getLogger()
    try:
        args = request.args
        print(args)
        # dataobj=QueryClass(schemaobj.dataobject)
        dataobj = QueryClass(tablename,logobj)
        # star query
        if len(args) == 0:
            logobj.info('Starting a star query..')
            outdata = dataobj.starquery()
            logobj.info('Completing a star query..')
            print(outdata)
        else:
            logobj.info('Starting a conditional query..')
            outdata = dataobj.conditionquery(input=args)
            logobj.info('Completing a conditional query..')

        # #star query
        # if len(args)==0:
        #     outdata=dataobj.starquery(table=tablename)
        #     print(outdata)

        logobj.info('Preparing success API response..')

        resp = make_response(
            jsonify(status="success", data=outdata.to_dict("records")), 200
        )
        logobj.info('Completing success API response..')
    except Exception as e:
        errmsg = traceback.format_exc()
        logobj.error(f'Error: {errmsg}')
        resp = make_response(
            jsonify(
                status="error",
                errormessage="error in query operation.Check logs for details.",
            ),
            500,
        )
    logobj.info('Sending response and completing query process..')
    return resp


@app.route("/create/<tablename>", methods=["POST"])
def createrecords(tablename):
    try:
        loggerobj = LoggerClass('create')
        logobj = loggerobj.getLogger()
    except Exception as e:
        resp=make_response(jsonify(status='error',errormessage='Error in initializing logs..please check system..'),500)
    try:
        logobj.info('Reading create inputs..')
        input = request.get_json()
        createobj = CreateClass(tablename,logobj)
        if isinstance(input, list):
            logobj.info('Starting process to add multiple rows..')
            createout = createobj.addmultiple(input)
            logobj.info('Preparing success API response..')
            resp = make_response(jsonify(status="success", data=createout), 200)
            logobj.info('Completing success API response..')
            logobj.info('Completing process to add multiple rows..')
        else:
            logobj.info('Starting process to add one row..')
            createout = createobj.addrows(input)
            logobj.info('Preparing success API response..')
            resp = make_response(jsonify(status="success", data=createout), 200)
            logobj.info('Completing success API response..')
            logobj.info('Completing process to add one row..')
        # print(isinstance(input,list))
        # resp=make_response(jsonify(status='success'),200)
    except Exception as e:
        errmsg = traceback.format_exc()
        logobj.error(f'Error: {errmsg}')
        resp = make_response(
            jsonify(
                status="error",
                errormessage="error in create operation.Check logs for details.",
            ),
            500,
        )
    logobj.info('Sending response and completing create process..')
    return resp


@app.route("/updatebyid/<tablename>", methods=["PATCH"])
def updatebyid(tablename):
    try:
        loggerobj = LoggerClass('updatebyid')
        logobj = loggerobj.getLogger()
    except Exception as e:
        resp=make_response(jsonify(status='error',errormessage='Error in initializing logs..please check system..'),500)
    try:
        logobj.info('Reading update inputs..')
        inpt = request.get_json()
        print(inpt)
        inptid = inpt["id"]
        del inpt["id"]
        print(inpt)
        logobj.info('Starting process to update records..')
        updobj = UpdateClass(tablename,logobj)
        updresp = updobj.updatebyid(inptid, inpt)
        logobj.info('Completed update process and preparing API response..')
        resp = make_response(jsonify(status="success", data=updresp), 200)
    except Exception as e:
        errmsg = traceback.format_exc()
        logobj.error(f'Error: {errmsg}')
        resp = make_response(
            jsonify(
                status="error",
                errormessage="error in update operation.Check logs for details.",
            ),
            500,
        )
    logobj.info('Sending response and completing update process..')
    return resp


@app.route("/updatecondition/<tablename>", methods=["PATCH"])
def updatebycondition(tablename):
    try:
        loggerobj = LoggerClass('updatebycondition')
        logobj = loggerobj.getLogger()
    except Exception as e:
        resp=make_response(jsonify(status='error',errormessage='Error in initializing logs..please check system..'),500)
    try:
        logobj.info('Starting reading the inputs..')
        updinpt = request.get_json()
        args = request.args
        print(updinpt)
        inptdict = {}
        for k, v in args.items():
            inptdict[k] = v
        print(inptdict)

        logobj.info('Starting process to update records..')
        updobj = UpdateClass(tablename,logobj)
        updresp = updobj.updatebycond(args, updinpt)
        logobj.info('Completed update process and preparing API response..')
        resp = make_response(jsonify(status="success", data=updresp), 200)
    except Exception as e:
        errmsg = traceback.format_exc()
        logobj.error(f'Error: {errmsg}')
        resp = make_response(
            jsonify(
                status="error",
                errormessage="error in update operation.Check logs for details.",
            ),
            500,
        )
    logobj.info('Sending response and completing update process..')
    return resp


@app.route("/deletebyid/<tablename>", methods=["DELETE"])
def delbyid(tablename):
    try:
        loggerobj = LoggerClass('deletebyid')
        logobj = loggerobj.getLogger()
    except Exception as e:
        resp=make_response(jsonify(status='error',errormessage='Error in initializing logs..please check system..'),500)
    try:
        logobj.info('Starting reading the inputs..')
        args = request.args
        inptid = args["id"]
        logobj.info('Starting process to delete records..')
        delobj = DeleteClass(tablename,logobj)
        delout = delobj.delbyid(int(inptid))
        logobj.info('Completed delete process and preparing API response..')
        resp = make_response(jsonify(status="success", data=delout), 200)
    except Exception as e:
        errmsg = traceback.format_exc()
        logobj.error(f'Error: {errmsg}')
        resp = make_response(
            jsonify(
                status="error",
                errormessage="error in delete operation.Check logs for details.",
            ),
            500,
        )
    logobj.info('Sending response and completing delete process..')
    return resp


@app.route("/deletebyfields/<tablename>", methods=["DELETE"])
def delbyfields(tablename):
    try:
        loggerobj = LoggerClass('deletebyfields')
        logobj = loggerobj.getLogger()
    except Exception as e:
        resp=make_response(jsonify(status='error',errormessage='Error in initializing logs..please check system..'),500)
    try:
        logobj.info('Starting reading the inputs..')
        inpt = request.get_json()
        logobj.info('Starting process to delete records..')
        delobj = DeleteClass(tablename,logobj)
        delout = delobj.delbyfields(inpt)
        logobj.info('Completed delete process and preparing API response..')
        resp = make_response(jsonify(status="success", data=delout), 200)
    except Exception as e:
        errmsg = traceback.format_exc()
        logobj.error(f'Error: {errmsg}')
        resp = make_response(
            jsonify(
                status="error",
                errormessage="error in delete operation.Check logs for details.",
            ),
            500,
        )
    logobj.info('Sending response and completing delete process..')
    return resp


if __name__ == "__main__":
    app.run(debug=True)
