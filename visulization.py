import matplotlib.pyplot as plt
import numpy as np


def plot_model_history(model_history):
    fig, axs = plt.subplots(1, 2, figsize=(15, 5))
    
    # Handle both 'acc' and 'accuracy' metric names for compatibility
    acc_key = 'accuracy' if 'accuracy' in model_history.history else 'acc'
    val_acc_key = 'val_accuracy' if 'val_accuracy' in model_history.history else 'val_acc'
    
    # summarize history for accuracy
    epochs = range(1, len(model_history.history[acc_key]) + 1)
    axs[0].plot(epochs, model_history.history[acc_key])
    axs[0].plot(epochs, model_history.history[val_acc_key])
    axs[0].set_title('Model Accuracy')
    axs[0].set_ylabel('Accuracy')
    axs[0].set_xlabel('Epoch')
    # Fix set_xticks syntax - set tick locations with proper step
    num_epochs = len(model_history.history[acc_key])
    step = max(1, num_epochs // 10)
    axs[0].set_xticks(np.arange(1, num_epochs + 1, step))
    axs[0].legend(['train', 'val'], loc='best')
    axs[0].grid(True)
    
    # summarize history for loss
    epochs = range(1, len(model_history.history['loss']) + 1)
    axs[1].plot(epochs, model_history.history['loss'])
    axs[1].plot(epochs, model_history.history['val_loss'])
    axs[1].set_title('Model Loss')
    axs[1].set_ylabel('Loss')
    axs[1].set_xlabel('Epoch')
    # Fix set_xticks syntax - set tick locations with proper step
    num_epochs = len(model_history.history['loss'])
    step = max(1, num_epochs // 10)
    axs[1].set_xticks(np.arange(1, num_epochs + 1, step))
    axs[1].legend(['train', 'val'], loc='best')
    axs[1].grid(True)
    
    plt.tight_layout()
    plt.show()