#!/usr/bin/env python

import wx
import ctypes

#
# === INSTRUCTIONS ===
#
# 1. COMPILE THE XCODE PROJECT FIRST.
#     Make sure to compile it in 32-bit, since wxPython relies on 32-bit mode
#
# 2. COPY THE .so FILE THAT WAS CREATED TO THE FOLDER
#    WHERE THIS PYTHON SCRIPT IS IN
#
# 3. RUN THIS PYTHON SCRIPT IN THE TERMINAL
#     Make sure to run Python in 32-bit mode
#
# 4. MOVE YOUR CURSOR TO THE WINDOW AND PRESS THE STYLUS HARD ON THE TABLET
#     You should see the pressure value change accordingly
#

tablet = ctypes.cdll.LoadLibrary('./libTabletLibC.so')

# you might want to wrap this in some class
tablet.get_point_x.restype = ctypes.c_longlong
tablet.get_point_y.restype = ctypes.c_longlong
tablet.get_point_z.restype = ctypes.c_longlong
tablet.get_buttons.restype = ctypes.c_longlong

tablet.get_tilt_x.restype = ctypes.c_double
tablet.get_tilt_y.restype = ctypes.c_double
tablet.get_rotation.restype = ctypes.c_double
tablet.get_pressure.restype = ctypes.c_double
tablet.get_tangent_pressure.restype = ctypes.c_double

tablet.get_vendor1.restype = ctypes.c_longlong
tablet.get_vendor2.restype = ctypes.c_longlong
tablet.get_vendor3.restype = ctypes.c_longlong
tablet.get_vendor_id.restype = ctypes.c_longlong
tablet.get_tablet_id.restype = ctypes.c_longlong
tablet.get_pointer_id.restype = ctypes.c_longlong
tablet.get_device_id.restype = ctypes.c_longlong
tablet.get_system_tablet_id.restype = ctypes.c_longlong
tablet.get_vendor_pointer_type.restype = ctypes.c_longlong
tablet.get_vendor_pointer_serial_number.restype = ctypes.c_longlong
tablet.get_vendor_unique_id.restype = ctypes.c_longlong
tablet.get_capability_mask.restype = ctypes.c_longlong
tablet.get_pointer_type.restype = ctypes.c_longlong
tablet.get_enter_proximity.restype = ctypes.c_longlong


class MyFrame(wx.Frame):
	def __init__(self, parent, title):
		wx.Frame.__init__(self, parent, title=title, size=(500,500))

		self.textBox = wx.TextCtrl(self, style=wx.TE_MULTILINE)

		self.Bind(wx.EVT_MOUSE_EVENTS, self.OnMouseEvent)
		self.textBox.Bind(wx.EVT_MOUSE_EVENTS, self.OnMouseEvent)

		self.Show(True)


	def OnMouseEvent(self, event):
		self.textBox.AppendText("x: " + str(tablet.get_point_x()) + " y: " + str(tablet.get_point_y()) + " p: " + str(tablet.get_pressure()) + "\n")

print "start: " + str(tablet.init()) # non-zero means error

app = wx.App(False)
frame = MyFrame(None, 'Test')
app.MainLoop()

print "end: " + str(tablet.stop()) # non-zero means error
