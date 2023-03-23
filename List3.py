import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider, Button

n = 100

theta = np.linspace(0, 2.0 * np.pi, n)
phi = np.linspace(0, 2.0 * np.pi, n)

theta, phi = np.meshgrid(theta, phi)

c, a = 1, 2


def f(c, a):
    x = (c + a * np.cos(theta)) * np.cos(phi)
    y = (c + a * np.cos(theta)) * np.sin(phi)
    z = a * np.sin(theta)
    return x, y, z


# fig = plt.figure()
# ax = plt.axes(projection='3d')

plot_x, plot_y, plot_z = f(2, 1)

# fig.subplots_adjust(left=0.25, bottom=0.25)

# ax_c = fig.add_axes([0, 1, 2, 3])

fig, ax = plt.subplots(ncols=1, subplot_kw={"projection": "3d"})
# fig.subplots_adjust(left=0.35, bottom=0.35)

plt.subplots_adjust(bottom=0.25)

torus = ax.plot_surface(plot_x, plot_y, plot_z, rstride=5, cstride=5)
# https://compwa-org.readthedocs.io/report/006.html

c_slider = Slider(
    ax=plt.axes([0.25, 0.1, 0.65, 0.03]),
    label='c',
    valmin=0.0,
    valmax=20.0,
    valinit=1,
)

# ax_a = fig.add_axes([0, 1, 2, 3])

a_slider = Slider(
    ax=plt.axes([0.2, 0.05, 0.65, 0.03]),
    label='a',
    valmin=0.0,
    valmax=20.0,
    valinit=1,
    # orientation="vertical"
)


def update(value):
    new_x, new_y, new_z = f(c_slider.val, a_slider.val)
    ax.clear()
    ax.plot_surface(new_x, new_y, new_z, rstride=5, cstride=5)
    fig.canvas.draw_idle()


c_slider.on_changed(update)
a_slider.on_changed(update)
plt.show()

# %matplotlib notebook
#
# # The parametrized function to be plotted
# def f(t, amplitude, frequency):
#     return amplitude * np.sin(2 * np.pi * frequency * t)
#
#
# t = np.linspace(0, 1, 1000)
#
# # Define initial parameters
# init_amplitude = 5
# init_frequency = 3
#
# # Create the figure and the line that we will manipulate
# fig, ax = plt.subplots()
# line, = ax.plot(t, f(t, init_amplitude, init_frequency), lw=2)
# ax.set_xlabel('Time [s]')
#
# # adjust the main plot to make room for the sliders
# fig.subplots_adjust(left=0.25, bottom=0.25)
#
# # Make a horizontal slider to control the frequency.
# axfreq = fig.add_axes([0.25, 0.1, 0.65, 0.03])
# freq_slider = Slider(
# ax=axfreq,
#     label='Frequency [Hz]',
#     valmin=0.1,
#     valmax=30,
#     valinit=init_frequency,
# )
#
# # Make a vertically oriented slider to control the amplitude
# axamp = fig.add_axes([0.1, 0.25, 0.0225, 0.63])
# amp_slider = Slider(
#     ax=axamp,
#     label="Amplitude",
#     valmin=0,
#     valmax=10,
#     valinit=init_amplitude,
#     orientation="vertical"
# )
#
#
# # The function to be called anytime a slider's value changes
# def update(val):
#     line.set_ydata(f(t, amp_slider.val, freq_slider.val))
#     fig.canvas.draw_idle()
#
#
# # register the update function with each slider
# freq_slider.on_changed(update)
# amp_slider.on_changed(update)
#
# # Create a `matplotlib.widgets.Button` to reset the sliders to initial values.
# resetax = fig.add_axes([0.8, 0.025, 0.1, 0.04])
# button = Button(resetax, 'Reset', hovercolor='0.975')
#
#
# def reset(event):
#     freq_slider.reset()
#     amp_slider.reset()
#
# button.on_clicked(reset)
#
# plt.show()
