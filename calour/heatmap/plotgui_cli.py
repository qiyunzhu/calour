# ----------------------------------------------------------------------------
# Copyright (c) 2016--,  Calour development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
# ----------------------------------------------------------------------------

from .plotgui import PlotGUI
from matplotlib import pyplot as plt


class PlotGUI_CLI(PlotGUI):
    '''Show the plot and relevant info in terminal

    It uses ``matplotlib`` only to display the plot and prints info on the
    terminal screen.
    '''
    def __call__(self):
        '''Run the GUI.'''
        super().__call__()
        plt.show()
