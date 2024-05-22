import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox, Button
import numpy as np

def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def plot_collatz_sequence(n):
    sequence = collatz_sequence(n)
    ax.clear()
    ax.plot(sequence, marker='o')
    ax.set_xlabel('Step')
    ax.set_ylabel('Value')
    ax.set_title('Collatz Sequence')
    ax.grid(True)
    plt.draw()

def submit(text):
    try:
        n = int(text)
        if n > 0:
            plot_collatz_sequence(n)
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Please enter a valid integer.")

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)

textbox_ax = plt.axes([0.1, 0.05, 0.8, 0.075])
textbox = TextBox(textbox_ax, 'Enter a positive integer:')
textbox.on_submit(submit)

plt.show()
