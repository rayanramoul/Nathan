import keras
import keras.backend as K
from keras.models import Sequential      # One layer after the other
from keras.layers import Dense, SimpleRNN, Flatten  # Dense layers are fully connected layers, Flatten layers flatten out multidimensional inputs
import tensorflow as tf
from sound_utils import * 

class RNN():
    def __init__(self):
        if not self.load():
            self.model = Sequential()
            self.model.add(Dense(64,
                    input_dim = 7,
                    activation = "tanh",
                    use_bias = False))
            self.model.add(Dense(64,
                    input_dim = 2,
                    activation = "tanh",
                    use_bias = False))
            self.model.add(SimpleRNN(2,
                        activation = "tanh",
                        use_bias = False))
            self.model.add(Dense(1,
                    activation = "relu",
                    use_bias = False))

            self.model.compile(loss='mse', optimizer='adam', metrics=['accuracy'])
    
    def save(self):
        model_json = self.model.to_json()
        with open("model.json", "w") as json_file:
            json_file.write(model_json)
        graph = tf.get_default_graph()
        with graph.as_default():
            self.model.save_weights("model.h5")

    def load(self):
        if os.path.isfile("model.json"):    
            json_file = open('model.json', 'r')
            loaded_model_json = json_file.read()
            json_file.close()
            self.model = model_from_json(loaded_model_json)
            # load weights into new model
            self.model.load_weights("model.h5")
            print("Loaded model from disk")
            self.model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
            return True
        else:
            return False

    def predict(self, input_path):
        return self.model.predict(input)

    def train(self, path):
        inputs, outputs = process(path)
        self.model.fit(inputs, outputs)
        self.save()

rnn_model = RNN()
rnn_model.train()