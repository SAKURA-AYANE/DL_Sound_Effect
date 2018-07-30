import wave
import numpy as np
import matplotlib.pyplot as plt

dim = 0
input_path = "data/train/input/"
output_path = "data/train/output/"
expected_path = "data/train/expected/"


# read input file
def read_file(path, i):
    input_filepath = path

    # choose file name
    if path == input_path:
        input_filename = "clean_" + str(i) + ".wav"
    else:
        input_filename = "tokyo_drive_" + str(i) + ".wav"
    input_file = wave.open(input_filepath + input_filename, 'rb')
    num_frame = input_file.getnframes()  # get the number of frames
    num_channel = input_file.getnchannels()  # get the number of channels
    global frame_rate
    frame_rate = input_file.getframerate()  # get the rate of frames
    global num_sample_width
    num_sample_width = input_file.getsampwidth()  # get the width of sample
    str_data = input_file.readframes(num_frame)  # read all frames
    input_file.close()  # close the file
    wave_data = np.fromstring(str_data, dtype=np.short)  # turn the data to numpy array

    # plot the wave
    time = np.arange(0, num_frame) * (1.0 / frame_rate)
    plt.plot(time, wave_data)
    plt.xlabel("Time(s)")
    plt.ylabel("Amplitude")
    plt.title("Single channel wavedata")
    plt.grid('on')  # 标尺，on：有，off:无。

    wave_data.shape = -1, num_channel  # shape the data depending on the number of channels
    wave_data = wave_data.T  # turn the wave data

    global dim
    dim = len(wave_data[0])

    # reshape the data
    wave_data = wave_data.reshape(dim, num_channel)

    return wave_data  # return numpy data


def get_dim():
    return dim


def get_frame_rate():
    return frame_rate

def get_sample_width():
    return num_sample_width
