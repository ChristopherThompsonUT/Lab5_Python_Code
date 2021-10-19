from math import sin, pi
import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd
import time

def x(k, f_0=300):
    A =  1
    phi = 0

    f_s = 8e3
    T = f_s**-1

    return A * sin( 2* pi * k * (f_0/f_s) + phi)

def plot_stem():
    t_vals = np.array([j/8e3 for j in range(0, 81)])
    x_vals = np.array([x(k) for k in range(0, 81)])

    plt.stem(t_vals, x_vals)
    plt.title("Stem Plot for function x(kT)")
    plt.xlabel("Sample (kT)")
    plt.ylabel("Value x(kT)")
    plt.show()

def plot_partb():
    t_vals = np.array([j/8e3 for j in range(0, 81)])

    x_vals_300 = np.array([x(k, 300) for k in range(0, 81)])
    x_vals_500 = np.array([x(k, 500) for k in range(0, 81)])
    x_vals_700 = np.array([x(k, 700) for k in range(0, 81)])
    x_vals_900 = np.array([x(k, 900) for k in range(0, 81)])

    fig, axs = plt.subplots(2,2)
    axs[0,0].plot(t_vals, x_vals_300)
    axs[0,0].set_title("Signal (f(t)) vs Time (s), f_0 = 300 Hz")
    axs[0,1].plot(t_vals, x_vals_500)
    axs[0,1].set_title("Signal (f(t)) vs Time (s), f_0 = 500 Hz")
    axs[1,0].plot(t_vals, x_vals_700)
    axs[1,0].set_title("Signal (f(t)) vs Time (s), f_0 = 700 Hz")
    axs[1,1].plot(t_vals, x_vals_900)
    axs[1,1].set_title("Signal (f(t)) vs Time (s), f_0 = 900 Hz")

    plt.show()

def partc():
    k_vals = np.arange(2*8e3)

    wv_300 = np.array([x(k, 300)*.3 for k in k_vals])
    wv_500 = np.array([x(k, 500)*.3 for k in k_vals])
    wv_700 = np.array([x(k, 700)*.3 for k in k_vals])
    wv_900 = np.array([x(k, 900)*.3 for k in k_vals])
    sd.play(wv_300, 8e3)
    time.sleep(1)
    sd.play(wv_500, 8e3)
    time.sleep(1)
    sd.play(wv_700, 8e3)
    time.sleep(1)
    sd.play(wv_900, 8e3)
    time.sleep(1)
    sd.stop()
def partd():
    k_vals = np.arange(1*8e3)

    wv_300 = np.array([x(k, 300)*.3 for k in k_vals])
    wv_500 = np.array([x(k, 500)*.3 for k in k_vals])
    wv_700 = np.array([x(k, 700)*.3 for k in k_vals])
    wv_900 = np.array([x(k, 900)*.3 for k in k_vals])
    wv_total = np.hstack((wv_300, wv_500, wv_700, wv_900))

    sd.play(wv_total, 8e3)
    time.sleep(5)
    sd.stop()
    
def parte():
    k_vals = np.arange(1*8e3)

    wv_7900 = np.array([x(k, 7700)*.3 for k in k_vals])
    wv_7700 = np.array([x(k, 7500)*.3 for k in k_vals])
    wv_7500 = np.array([x(k, 7300)*.3 for k in k_vals])
    wv_7300 = np.array([x(k, 7100)*.3 for k in k_vals])
    wv_total = np.hstack((wv_7900, wv_7700, wv_7500, wv_7300))

    sd.play(wv_total, 8e3)
    time.sleep(5)
    sd.stop()
    
def part2a(f_s = 32e3):

    def c(t):
        A =50
        phi = 0
        mu = 2e3
        f_1 = 100

        return A * sin( pi * mu * (t**2) +2*pi*f_1 + phi)

    t_vals = np.arange(8*f_s)

    cwv = np.array([c(t) for t in t_vals])
    cwv_sub = cwv[:2000]
    
    sd.play(cwv, f_s)
    time.sleep(5)
    sd.stop()

    plt.plot([t/f_s for t in range(0,2000)], cwv_sub)
    title = ("Stem Plot for chirp signal c(t), f_s = "+ str(f_s) + "Hz")
    plt.title(title)
    plt.xlabel("Time (s)")
    plt.ylabel("c(t)")
    plt.show()

def part2b():

    print("Sampling at 32kHz")
    part2a()
    print("Sampling at 16kHz")
    part2a(16e3)
    time.sleep(1)
    print("Sampling at 8kHz")
    part2a(8e3)
    

