from os import pread
import pandas as pd
import numpy as np
import bentoml as bn
from bentoml.io import NumpyNdarray as nd
from pydantic import BaseModel as bm


model_ref = bn.sklearn.get('mlzoomcamp_homework:jsi67fslz6txydu5')
model_runner = model_ref.to_runner()

svc = bn.Service('mlzoomcamp_classifier', runners=[model_runner])

@svc.api(input = nd(), output = nd())
def classify(vector):
    prediction = model_runner.predict.run(vector)
    print(prediction)

    result = prediction[0]
    print(type(prediction))

    print(result)

    return prediction