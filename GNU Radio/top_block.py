#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Sat Apr 15 00:00:57 2017
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import constsink_gl
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import epy_block_0
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000
        self.amplitude = amplitude = 0

        ##################################################
        # Blocks
        ##################################################
        _amplitude_sizer = wx.BoxSizer(wx.VERTICAL)
        self._amplitude_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_amplitude_sizer,
        	value=self.amplitude,
        	callback=self.set_amplitude,
        	label='amplitude',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._amplitude_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_amplitude_sizer,
        	value=self.amplitude,
        	callback=self.set_amplitude,
        	minimum=0,
        	maximum=0.6,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_amplitude_sizer)
        self.wxgui_constellationsink2_0 = constsink_gl.const_sink_c(
        	self.GetWin(),
        	title='Constellation Plot',
        	sample_rate=samp_rate,
        	frame_rate=5,
        	const_size=2048,
        	M=4,
        	theta=0,
        	loop_bw=6.28/100.0,
        	fmax=0.06,
        	mu=0.5,
        	gain_mu=0.005,
        	symbol_rate=samp_rate/4.,
        	omega_limit=0.005,
        )
        self.Add(self.wxgui_constellationsink2_0.win)
        self.epy_block_0 = epy_block_0.blk(power_param=1.0)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.analog_random_uniform_source_x_0 = analog.random_uniform_source_i(0, 4, 0)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, amplitude, 42)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.analog_random_uniform_source_x_0, 0), (self.epy_block_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.wxgui_constellationsink2_0, 0))
        self.connect((self.epy_block_0, 0), (self.blocks_add_xx_0, 0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_constellationsink2_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_amplitude(self):
        return self.amplitude

    def set_amplitude(self, amplitude):
        self.amplitude = amplitude
        self._amplitude_slider.set_value(self.amplitude)
        self._amplitude_text_box.set_value(self.amplitude)
        self.analog_noise_source_x_0.set_amplitude(self.amplitude)


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
