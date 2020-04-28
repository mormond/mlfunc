import logging
import azure.functions as func
import os
import json
import pickle
import sklearn
from timeit import default_timer as timer

def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    localdir = context.function_directory
    lookup = {}
    model = {}
    features = []

    try:
        with open(os.path.join(localdir, '../data/lookup.pkl'), 'rb') as lookup_file:
            lookup = pickle.load(lookup_file)
            if not str(type(lookup).__name__).startswith("OrderedDict"):
                return func.HttpResponse("### !ERROR: {} is not a OrderedDict object".format('lookup.pkl'), status_code=500)

        with open(os.path.join(localdir, '../data/model.pkl'), 'rb') as model_file:
            model = pickle.load(model_file)
            if not str(type(model).__module__).startswith("sklearn"):
                return func.HttpResponse("### !ERROR: {} is not a sklearn object".format('model.pkl'), status_code=500)

        with open(os.path.join(localdir, '../data/flags.pkl'), 'rb') as flags_file:
            flags = pickle.load(flags_file)
            if not str(type(flags).__name__).startswith("list"):
                return func.HttpResponse("### !ERROR: {} is not a list object".format('flags.pkl'), status_code=500)

        request_dict = req.get_json()

        for key in lookup:
            val = request_dict[key]
            if type(val) == type(str()):
                val = lookup[key][val]

            features.append(val)

        start = timer()
        prediction = model.predict_proba([features]) 
        end = timer()

        prediction_list = dict(zip(flags, prediction[0]))

        logging.info("### Prediction result: {}".format(prediction_list))
        logging.info("### Prediction took: {} ms".format(round((end - start) * 1000, 2)))

        return func.HttpResponse(json.dumps(prediction_list), status_code=200, mimetype='application/json')

    except KeyError as key_error:
        print('### KEY_ERROR:', str(key_error))
        return func.HttpResponse(json.dumps({'error': 'Value: '+str(key_error)+' not found in model lookup'}), status_code=400, mimetype='application/json')
    except Exception as err:
        print('### EXCEPTION:', str(err))
        return func.HttpResponse(json.dumps({'error': str(err)}), status_code=500, mimetype='application/json')

