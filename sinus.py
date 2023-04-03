import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

x = np.linspace(0, 100)

def data(x, amp, puls):
    return amp*np.sin(puls*x)

# Create the figure and the line that we will manipulate
fig, ax = plt.subplots()
line, = plt.plot(x, data(x, 1, 1))
# Make a horizontal slider to control the frequency.
axmu = plt.axes([0.25, 0.1, 0.65, 0.03])
puls_slider = Slider(
    ax=axmu,
    label='Pulsation',
    valmin=0,
    valmax=9,
    valinit=1,
)

# Make a vertically oriented slider to control the amplitude
axlambda = plt.axes([0.1, 0.25, 0.0225, 0.63])
amp_slider = Slider(
    ax=axlambda,
    label="Amplitude",
    valmin=0,
    valmax=9,
    valinit=1,
    orientation="vertical"
)


# Make a vertically oriented slider to control the amplitude
ax_val = plt.axes([0.5, 0.2, 1.3, 0.06])
x_slider = Slider(
    ax=ax_val,
    label="X",
    valmin=0,
    valmax=30,
    valinit=9,
    #orientation="vertical"
)
# The function to be called anytime a slider's value changes
def update(val):
    x = np.linspace(0, x_slider.val)
    dat = data(x, amp_slider.val, puls_slider.val)
    line.set_ydata(dat)
    # fig.canvas.draw_idle()


# register the update function with each slider
amp_slider.on_changed(update)
puls_slider.on_changed(update)
x_slider.on_changed(update)

# Create a `matplotlib.widgets.Button` to reset the sliders to initial values.
resetax = plt.axes([0.1, 0.2, 0.3, 0.04])
button = Button(resetax, 'Reset', hovercolor='0.975')


def reset(event):
    amp_slider.reset()
    puls_slider.reset()
    x_slider.reset()

button.on_clicked(reset)

plt.show()

