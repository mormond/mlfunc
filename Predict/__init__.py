import logging
import azure.functions as func
import os
import json
import pickle

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        logging.info(req.get_body())
        request_dict = req.get_json()
        logging.info(request_dict)

        #results = predictor.predict(request_dict)
        #return jsonify(results)

    except KeyError as key_error:
        print('### KEY_ERROR:', str(key_error))
        return func.HttpResponse(json.dumps({'error': 'Value: '+str(key_error)+' not found in model lookup'}), status_code=400, mimetype='application/json')
    except Exception as err:
        print('### EXCEPTION:', str(err))
        return func.HttpResponse(json.dumps({'error': str(err)}), status_code=500, mimetype='application/json')




