
from slp import SLP

# Lowest MSE
LMSE = 0.001

def _normalise(data):
    """
    Turn data into values between 0 and 1
    :param data: list of lists of input data and output e.g.
        [
            [[in1, in2, ...], out],
            ...
        ]
    :returns: Normalised training data
    """
    temp_list = []
    for entry in data:
        entry_list = []
        for value in entry[0]:
            # Normalise the data. 1/255 ~ 0.003921568
            entry_list.append(float(value*0.003921568))
        temp_list.append([entry_list, entry[1]])
    return temp_list

def _train(p, data):
    """
    Trains the perceptron
    :param p: The perceptron to train
    :param data: The data to train it with
    """

    # Normalise the data
    training_data = _normalise(data)

    # Number of full iterations
    epochs = 0

    # Instantiate mse for the loop
    mse = 999

    while (abs(mse-LMSE) > 0.002):

        # Epoch cumulative error
        error = 0

        # For each set in the training_data
        for value in training_data:

            # Calculate the result
            output = p.result(value[0])

            # Calculate the error
            iter_error = value[1] - output

            # Add the error to the epoch error
            error += iter_error

            # Adjust the weights based on inputs and the error
            p.weight_adjustment(value[0], iter_error)

        # Calculate the MSE - epoch error / number of sets
        mse = float(error/len(training_data))

        # Increment the epoch number
        epochs += 1

    return p

def create_slp(ins, data):
    """
    Create the SLP
    :param ins: number of inputs
    :param data: training data
    """
    # Create the perceptron
    p = SLP(ins)

    _train(p, data)

    return p
