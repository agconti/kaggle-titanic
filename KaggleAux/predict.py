from patsy import dmatrices
import numpy as np
from pandas import DataFrame


def predict(test_data, results, model_name):
    """
    Return a NumPy array of independent variable predictions of a test file
    basedon your regression of a train file.

    Parameters
    ----------
    test_data: pandas dataframe
        should be test data you are trying to predict
    results: dict
        should be dict of your models results wrapper and the formula used
        to produce it.
            ie.
            results['Model_Name'] = {[<statsmodels.regression.linear_model.RegressionResultsWrapper> , "Price ~ I(Supply, Demand)] }
    model_name: str
        should be the name of your model. You can iterate through the results dict.

    Returns
    -------
    NumPy array
        Predictions in a flat NumPy array.

    Example
    -------
    results = {'Logit': [<statsmodels.discrete.discrete_model.BinaryResultsWrapper at 0x117896650>,
               'survived ~ C(pclass) + C(sex) + age + sibsp  + C(embarked)']}
    compared_resuts = predict(test_data, results, 'Logit')
    """
    model_params = DataFrame(results[model_name][0].params)
    formula = results[model_name][1]

    # Create reg friendly test dataframe
    yt, xt = dmatrices(formula, data=test_data, return_type='dataframe')

    # remove extraneous features for efficiency
    # for c in xt.columns:
    #     if c not in model_params.index:
    #         to_drop.append(c)

    to_drop = list((c if c not in model_params.index for c in xt.columns))
    xt = xt.drop(to_drop, axis=1)


    to_drop = list(c if c not in xt.columns for c in model_params.index))

    for c in model_params.index:
        if c not in xt.columns:
            to_drop.append(c)
    model_params = model_params.drop(to_drop)

    # Convert to NumPy arrays for performance
    model_params = np.asarray(model_params)
    yt = np.asarray(yt)
    yt = yt.ravel()
    xt = np.asarray(xt)

    # Use our models to create predictions
    row, col = xt.shape
    model_params = model_params.ravel()
    model_array = []

    for _ in xrange(row):
            model_array.append(model_params)
    model_array = np.asarray(model_array)

    # Multiply matrix together
    predictions = np.multiply(xt, model_array)
    predictions = np.sum(predictions, axis=1)

    return predictions
