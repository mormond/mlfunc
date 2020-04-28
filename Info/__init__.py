import logging
import azure.functions as func
import os
import json

def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    localdir = context.function_directory

    try:
        with open(os.path.join(localdir, '../data/metadata.json')) as f:
            metadata = json.load(f)
    except Exception as err:
        print('### EXCEPTION:', str(err))
        return func.HttpResponse(json.dumps({'error': str(err)}), status_code=500, mimetype='application/json')
    return func.HttpResponse(json.dumps({'status': 'alive', 'metadata': metadata}), status_code=200, mimetype='application/json')

