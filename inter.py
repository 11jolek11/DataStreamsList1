import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button



# Make a horizontal slider to control the frequency.
axmu = plt.axes([0.25, 0.1, 0.65, 0.03])
mu_slider = Slider(
    ax=axmu,
    label='Mu',
    valmin=0,
    valmax=1,
    valinit=init_mu,
)

# Make a vertically oriented slider to control the amplitude
axlambda = plt.axes([0.1, 0.25, 0.0225, 0.63])
lambda_slider = Slider(
    ax=axlambda,
    label="Lambda",
    valmin=0,
    valmax=1,
    valinit=init_lambda,
    orientation="vertical"
)


# The function to be called anytime a slider's value changes
def update(val):
    line.set_ydata(reliability_graph(t, mu_slider.val, lambda_slider.val))
    fig.canvas.draw_idle()


# register the update function with each slider
mu_slider.on_changed(update)
lambda_slider.on_changed(update)

# Create a `matplotlib.widgets.Button` to reset the sliders to initial values.
resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', hovercolor='0.975')


def reset(event):
    mu_slider.reset()
    lambda_slider.reset()

button.on_clicked(reset)

plt.show()

