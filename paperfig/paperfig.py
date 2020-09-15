# -*- coding: utf-8 -*-
"""
Set the common figure styles for papers.
"""

import numpy as np
import matplotlib as mpl

# ==================================================================== #
# for MNRAS
# ==================================================================== #
mpl.rcParams['ps.fonttype'] = 42

import matplotlib.pyplot as plt
from matplotlib import colors
import seaborn as sns
import coloripy as cp


# to change tex to Times New Roman in mpl
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'Times New Roman'
plt.rcParams['mathtext.rm'] = 'serif'
plt.rcParams['mathtext.it'] = 'serif:italic'
plt.rcParams['mathtext.bf'] = 'serif:bold'
plt.rcParams['mathtext.fontset'] = 'custom'


def set_fontscale(font_scale=1):
    sns.set(style='ticks', context=None,
            font='Times New Roman',
            rc={#"text.usetex": True,
                #"font.family": 'serif',
                #"font.serif": 'Times New Roman',
                #"mathtext.rm": 'serif',
                #"mathtext.it": 'serif:italic',
                #"mathtext.bf": 'serif:bold',
                #"mathtext.fontset": 'custom',
                "xtick.direction": "in",
                "ytick.direction": "in",
                "axes.linewidth": 0.5*font_scale,
                "axes.labelsize": 9*font_scale,
                "font.size": 9*font_scale,
                "axes.titlesize": 9*font_scale,
                "legend.fontsize": 8*font_scale,
                "xtick.labelsize": 8*font_scale,
                "ytick.labelsize": 8*font_scale,
               })

    #plt.style.use('ticks')
    #width = 345

    """nice_fonts = {
        # Use LaTeX to write all text
        "text.usetex": True,
        "font.family": "serif",
        # Use 9pt font in plots, to match 9pt font in document
        "axes.labelsize": 9*font_scale,
        "font.size": 9*font_scale,
        #"title.fontsize": 9 * font_scale,
        # Make the legend/label fonts a little smaller
        "legend.fontsize": 8*font_scale,
        "xtick.labelsize": 8*font_scale,
        "ytick.labelsize": 8*font_scale,
    }

    mpl.rcParams.update(nice_fonts)"""

#set_fontscale(1)


cmap = sns.cubehelix_palette(start=0.5, rot=-1.5, gamma=1, hue=1, light=0.,
                             dark=1., reverse=False, as_cmap=True)
msh_cmap = cp.get_msh_cmap(num_bins=501, rescale='power', power=2.5)
msh_cmap2 = cp.get_msh_cmap(rgb1=np.array([0.085, 0.532, 0.201])*256,
                            rgb2=np.array([0.436, 0.308, 0.631])*256,
                            ref_point=(160, 160, 160),
                            num_bins=501, rescale='power', power=1.5)


# ==================================================================== #
# color definitions
# ==================================================================== #

# from cb2
emerald = sns.xkcd_rgb['emerald']
orange = sns.xkcd_rgb['bright orange']
purple = sns.xkcd_rgb['light purple']

# from cb2
cb2_emerald = '#66c2a5'
cb2_orange = '#fc8d62'
cb2_blue = '#8da0cb'

# from cb2 bright
cb_red = '#e41a1c'
cb_blue = '#377eb8'
cb_green = '#4daf4a'
cb_purple = '#984ea3'
cb_orange = '#ff7f00'
cb_grey = '#404040'

# seaborn deep palette
deep = sns.color_palette(palette='deep')

deep_blue = colors.rgb2hex(deep[0])
deep_orange = colors.rgb2hex(deep[1])
deep_green = colors.rgb2hex(deep[2])
deep_red = colors.rgb2hex(deep[3])

# ==================================================================== #
# convenience functions
# ==================================================================== #

# journal sizes
mnras_colwidth = 240. # pt
mnras_textwidth = 504. # pt
mnras_text_fontsize = 9. #pt
mnras_figcaption_fontsize = 8. #pt
golden_ratio = (5**.5 - 1) / 2
# use this in latex to get text and column width
# \showthe\textwidth
# \showthe\columnwidth

# use this in latex to get size
# \usepackage[T1]{fontenc}
# \newcommand\thefont{\expandafter\string\the\font}
# \thefont


def get_fig_size(width, height_ratio=None, fraction=1):
    """
    Set aesthetic figure dimensions to avoid scaling in latex. Function from
    https://jwalton.info/Embed-Publication-Matplotlib-Latex/.

    :param width: width in pts
    :type width: float
    :param height_ratio: fraction of width to set for the height
    :type height_ratio: float
    :param fraction: fraction of the width for the figure to occupy
    :type fraction: float
    :return: dimensions of figure in inches
    :rtype: tuple
    """
    # Width of figure
    fig_width_pt = width * fraction

    # Convert from pt to inches
    inches_per_pt = 1. / 72.2699  # 72.27 in original ??

    if height_ratio is None:
        # Golden ratio to set aesthetic figure height
        height_ratio = golden_ratio

    # Figure width in inches
    fig_width_in = fig_width_pt * inches_per_pt
    # Figure height in inches
    fig_height_in = fig_width_in * height_ratio

    fig_dim = (fig_width_in, fig_height_in)

    return fig_dim
