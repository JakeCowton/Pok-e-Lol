
from slp import SLP

# Lowest MSE
LMSE = 0.001

def _normalise(data):
    """
    Normalises raw input data
    :type data: List
    :param data: The input data
    :rtype: List
    :returns: Normalised data
    """
    npc_health, user_health, avr_dam_taken, avr_dam_given = data

    npc_health = float(npc_health) / 500.0
    user_health = float(user_health) / 500.0
    avr_dam_taken = float(avr_dam_taken) / 500.0
    avr_dam_given = float(avr_dam_given) / 500.0

    return [npc_health, user_health, avr_dam_taken, avr_dam_given]

def _train(p, data):
    """
    Trains the perceptron
    :param p: The perceptron to train
    :param data: The data to train it with
    :rtype: SLP()
    :returns: trained perceptron
    """
    # Number of full iterations
    epochs = 0

    # Instantiate mse for the loop
    mse = 999

    while (abs(mse-LMSE) > 0.002):

        # Epoch cumulative error
        error = 0

        # For each set in the training_data
        for value in data:

            # Calculate the result
            output = p.result(value[0])

            # Calculate the error
            iter_error = value[1] - output

            # Add the error to the epoch error
            error += iter_error

            # Adjust the weights based on inputs and the error
            p.weight_adjustment(value[0], iter_error)

        # Calculate the MSE - epoch error / number of sets
        mse = float(error/len(data))

        # Increment the epoch number
        epochs += 1

    return p

def create_slp(data):
    """
    Create the SLP
    :param data: training data
    :rtype: SLP()
    :returns: Trained perceptron
    """
    # Create the perceptron
    p = SLP(6)
    # Train the perceptron
    _train(p, data)

    return p

def call_slp(p, inputs):
    """
    Use the SLP to get outputs from `inputs`
    :param p: perceptron
    :param inputs: npc health, user health, avr damage taken, avr damage given
    :rtype: string
    :returns: 'attack' or 'defend'
    """
    inputs = _normalise(inputs)
    return p.recall(inputs)
