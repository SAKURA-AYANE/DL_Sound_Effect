from keras.models import load_model
from codes import read_audio as ra
import numpy as np
from numpy import newaxis
import matplotlib.pyplot as plt
import os
import errno
from scipy.io import wavfile
from scipy import signal
from codes.read_audio import npers

# input path
input_path = "data/test/input/"

for file in os.listdir(input_path):
    try:
        name_num = file.split("_")[-1]

        # get input numpy array
        test_in = ra.stft_ri(input_path + file)
        test_in = test_in[:, newaxis, :]

        # load the model
        model_path = "data/model/lstm_djent_model.h5"
        weight_path = "data/model/weights_djent.best.hdf5"
        model = load_model(model_path)

        # if exist load weights
        if os.path.exists(weight_path):
            model.load_weights(weight_path)

        # predict the output
        test_out = model.predict(test_in)
        out1, out2 = np.split(test_out.T, 2, axis=0)  # split output to real and imaginary
        out_stft = out1 + 1j * out2  # transfer to stft again
        _, d = signal.istft(out_stft, ra.rate, nperseg=npers)
        out_data = d.astype('int16')
        print(out_data)
        out_data = out_data.astype('int16')  # transfer data to int16

        # write audio
        wavfile.write(r"data/test/output/test_out_" + name_num, ra.rate, out_data)

        # plot the wave
        time = np.arange(0, len(out_data)) * (1.0 / ra.rate)  # time length of the audio
        plt.plot(time, out_data)
        plt.xlabel("Time(s)")
        plt.ylabel("Amplitude")
        plt.title("show wave")
        plt.grid('on')
        plt.show()

    # catch errors
    except IOError as exc:
        if exc.errno != errno.EISDIR:
            raise
