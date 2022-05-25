#/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

def plot_history(history):
    """
    Plots loss and validation loss from a 
    keras training history. 

    Parameters
    ----------
    history : Keras history object
        output from a training history. 

    Returns
    -------
    Nothing
    
    """
    fig = plt.figure(figsize=(12,8))
    ax1 = fig.add_subplot(111)

    # summarize history for loss
    ax1.plot(history.history['loss'], label = 'loss')
    ax1.plot(history.history['val_loss'], label = 'val loss')
    ax1.set_title('Model Loss')
    ax1.set_ylabel('Loss')
    ax1.set_xlabel('Epoch')
    ax1.legend(loc='best')
    plt.show()
    
    return