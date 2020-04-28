import logging
import azure.functions as func
import os
import json
import pickle

def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    localdir = context.function_directory
    resp = {}
    lookup = {}

    try:
        with open(os.path.join(localdir, '../data/lookup.pkl'), 'rb') as lookup_file:
            lookup = pickle.load(lookup_file)
            if not str(type(lookup).__name__).startswith("OrderedDict"):
                return func.HttpResponse("### !ERROR: {} is not a OrderedDict object".format(lookup_name), status_code=500)

        for key in lookup:
            if type(lookup[key]) == type(dict()):
                resp[key] = [subkey for subkey in lookup[key].keys()]
            else:
                resp[key] = 0

        return func.HttpResponse(json.dumps(resp), status_code=200, mimetype='application/json')

    except Exception as err:
        print('### EXCEPTION:', str(err))
        return func.HttpResponse(json.dumps({'error': str(err)}), status_code=500, mimetype='application/json')

