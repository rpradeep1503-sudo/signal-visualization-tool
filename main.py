import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
import os

import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk

# ---------- Signal Functions ----------
def get_time(duration=1, samples=1000):
    return np.linspace(0, duration, samples)

def sine_wave(A, f, t):
    return A * np.sin(2 * np.pi * f * t)

def square_wave(A, f, t):
    return A * np.sign(np.sin(2 * np.pi * f * t))

def triangular_wave(A, f, t):
    return A * (2/np.pi) * np.arcsin(np.sin(2 * np.pi * f * t))

# ---------- Plot Function ----------
def plot_signal():
    import os

def plot_signal():
    A = amp_slider.get()
    F = freq_slider.get()
    signal_type = signal_var.get()

    t = get_time()

    if signal_type == "Sine":
        y = sine_wave(A, F, t)
        filename = "sine.png"
    elif signal_type == "Square":
        y = square_wave(A, F, t)
        filename = "square.png"
    else:
        y = triangular_wave(A, F, t)
        filename = "triangular.png"

    plt.figure()
    plt.plot(t, y)
    plt.title(f"{signal_type} Wave")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)

    os.makedirs("screenshots", exist_ok=True)
    plt.savefig(f"screenshots/{filename}")
    plt.show()

# ---------- GUI ----------
root = tk.Tk()
root.title("Signal Visualization Tool")
root.geometry("300x250")

tk.Label(root, text="Amplitude").pack()
amp_slider = tk.Scale(root, from_=0, to=10, resolution=0.1, orient="horizontal")
amp_slider.set(1)
amp_slider.pack()

tk.Label(root, text="Frequency (Hz)").pack()
freq_slider = tk.Scale(root, from_=1, to=50, orient="horizontal")
freq_slider.set(5)
freq_slider.pack()

tk.Label(root, text="Signal Type").pack()
signal_var = tk.StringVar(value="Sine")
signal_menu = ttk.Combobox(root, textvariable=signal_var,
                           values=["Sine", "Square", "Triangular"],
                           state="readonly")
signal_menu.pack()

tk.Button(root, text="Plot Signal", command=plot_signal).pack(pady=10)

root.mainloop()
