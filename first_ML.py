import tensorflow as tf
import numpy as np
from tensorflow import keras

def house_model():
    ### START CODE HERE
    
    # Define input and output tensors with the values for houses with 1 up to 6 bedrooms
    # Hint: Remember to explictly set the dtype as float
    xs = np.array([1.0,  2.0, 3.0, 4.0, 5.0, 6.0], dtype=float)
    ys = np.array([100000.0,  150000.0, 200000.0, 250000.0, 300000.0, 350000.0], dtype=float)
    
    # Define your model (should be a model with 1 dense layer and 1 unit)
    model = tf.keras.Sequential([keras.layers.Dense(units =1, input_shape=[1])])
    
    # Compile your model
    # Set the optimizer to Stochastic Gradient Descent
    # and use Mean Squared Error as the loss function
    model.compile(optimizer='sgd', loss='mean_squared_error')
    
    # Train your model for 1000 epochs by feeding the i/o tensors
    model.fit(xs, ys, epochs=1000)
    
    ### END CODE HERE
    return model
model = house_model()
new_x = 7.0
prediction = model.predict([new_x])[0]
print(prediction)
