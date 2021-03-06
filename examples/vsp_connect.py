#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Vsp Connect
# Generated: Wed Oct 17 07:47:46 2012
##################################################

from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import grpyserial
import wx

class vsp_connect(grc_wxgui.top_block_gui):

	def __init__(self):
		grc_wxgui.top_block_gui.__init__(self, title="Vsp Connect")
		_icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
		self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

		##################################################
		# Variables
		##################################################
		self.samp_rate = samp_rate = 32000

		##################################################
		# Blocks
		##################################################
		self.serial_port_0_0 = grpyserial.serial_port("/dev/pts/7",0,115200,0,1,False)
		self.serial_port_0 = grpyserial.serial_port("/dev/pts/5",0,115200,0,1,False)

		##################################################
		# Connections
		##################################################
		self.connect((self.serial_port_0_0, 0), (self.serial_port_0, 0))
		self.connect((self.serial_port_0, 0), (self.serial_port_0_0, 0))

	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = vsp_connect()
	tb.Run(True)

