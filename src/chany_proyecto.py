# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class ChanyFrame
###########################################################################

class ChanyFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Exportar a mosaico", pos = wx.DefaultPosition, size = wx.Size( 1117,843 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 876,633 ), wx.DefaultSize )
		self.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Balbaleo" ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_splitter1 = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D|wx.SP_LIVE_UPDATE|wx.SP_NO_XP_THEME )
		self.m_splitter1.Bind( wx.EVT_IDLE, self.m_splitter1OnIdle )

		self.m_scrolledWindow1 = wx.ScrolledWindow( self.m_splitter1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow1.SetScrollRate( 5, 5 )
		bSizer51 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel31 = wx.Panel( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel31.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Clarendon BT" ) )
		self.m_panel31.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel31, wx.ID_ANY, u"Cargar archivo" ), wx.VERTICAL )

		self.m_filePicker1 = wx.FilePickerCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		sbSizer1.Add( self.m_filePicker1, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer2.Add( sbSizer1, 0, wx.EXPAND, 15 )

		m_radioBox1Choices = [ u"A4", u"Carta", u"Oficio" ]
		self.m_radioBox1 = wx.RadioBox( self.m_panel31, wx.ID_ANY, u"Tamaño", wx.DefaultPosition, wx.DefaultSize, m_radioBox1Choices, 1, wx.RA_SPECIFY_ROWS )
		self.m_radioBox1.SetSelection( 1 )
		bSizer2.Add( self.m_radioBox1, 0, wx.ALL|wx.EXPAND, 5 )

		m_radioBox11Choices = [ u"Retrato", u"Paisaje" ]
		self.m_radioBox11 = wx.RadioBox( self.m_panel31, wx.ID_ANY, u"Orientación", wx.DefaultPosition, wx.DefaultSize, m_radioBox11Choices, 1, wx.RA_SPECIFY_ROWS )
		self.m_radioBox11.SetSelection( 0 )
		bSizer2.Add( self.m_radioBox11, 0, wx.ALL|wx.EXPAND, 5 )

		sbSizer2211 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel31, wx.ID_ANY, u"Ancho linea roja" ), wx.HORIZONTAL )

		self.m_slider1211 = wx.Slider( sbSizer2211.GetStaticBox(), wx.ID_ANY, 3, 1, 10, wx.DefaultPosition, wx.DefaultSize, wx.SL_AUTOTICKS|wx.SL_HORIZONTAL|wx.SL_LABELS )
		sbSizer2211.Add( self.m_slider1211, 5, wx.ALL|wx.EXPAND, 1 )

		self.m_textCtrl2112 = wx.TextCtrl( sbSizer2211.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.TE_PROCESS_ENTER )
		sbSizer2211.Add( self.m_textCtrl2112, 0, wx.ALL, 5 )


		bSizer2.Add( sbSizer2211, 0, wx.EXPAND, 5 )

		sbSizer221 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel31, wx.ID_ANY, u"x_off" ), wx.HORIZONTAL )

		self.m_slider121 = wx.Slider( sbSizer221.GetStaticBox(), wx.ID_ANY, 0, 0, 10, wx.DefaultPosition, wx.DefaultSize, wx.SL_AUTOTICKS|wx.SL_HORIZONTAL|wx.SL_LABELS )
		sbSizer221.Add( self.m_slider121, 5, wx.ALL|wx.EXPAND, 1 )

		self.m_textCtrl211 = wx.TextCtrl( sbSizer221.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.TE_PROCESS_ENTER )
		sbSizer221.Add( self.m_textCtrl211, 0, wx.ALL, 5 )


		bSizer2.Add( sbSizer221, 0, wx.EXPAND, 5 )

		sbSizer22 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel31, wx.ID_ANY, u"y_off" ), wx.HORIZONTAL )

		self.m_slider12 = wx.Slider( sbSizer22.GetStaticBox(), wx.ID_ANY, 0, 0, 10, wx.DefaultPosition, wx.DefaultSize, wx.SL_AUTOTICKS|wx.SL_HORIZONTAL|wx.SL_LABELS )
		sbSizer22.Add( self.m_slider12, 5, wx.ALL|wx.EXPAND, 1 )

		self.m_textCtrl2111 = wx.TextCtrl( sbSizer22.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.TE_PROCESS_ENTER )
		sbSizer22.Add( self.m_textCtrl2111, 0, wx.ALL, 5 )


		bSizer2.Add( sbSizer22, 0, wx.EXPAND, 5 )

		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel31, wx.ID_ANY, u"Translape" ), wx.HORIZONTAL )

		self.m_slider1 = wx.Slider( sbSizer2.GetStaticBox(), wx.ID_ANY, 0, 0, 10, wx.DefaultPosition, wx.DefaultSize, wx.SL_AUTOTICKS|wx.SL_HORIZONTAL|wx.SL_LABELS )
		sbSizer2.Add( self.m_slider1, 5, wx.ALL|wx.EXPAND, 1 )

		self.m_textCtrl2 = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.TE_PROCESS_ENTER )
		sbSizer2.Add( self.m_textCtrl2, 0, wx.ALL, 5 )


		bSizer2.Add( sbSizer2, 0, wx.EXPAND, 5 )

		sbSizer21 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel31, wx.ID_ANY, u"Margen" ), wx.HORIZONTAL )

		self.m_slider11 = wx.Slider( sbSizer21.GetStaticBox(), wx.ID_ANY, 0, 0, 10, wx.DefaultPosition, wx.DefaultSize, wx.SL_AUTOTICKS|wx.SL_HORIZONTAL|wx.SL_LABELS )
		sbSizer21.Add( self.m_slider11, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_textCtrl1 = wx.TextCtrl( sbSizer21.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.TE_PROCESS_ENTER )
		sbSizer21.Add( self.m_textCtrl1, 0, wx.ALL, 5 )


		bSizer2.Add( sbSizer21, 0, wx.EXPAND, 5 )

		sbSizer211 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel31, wx.ID_ANY, u"DPI" ), wx.HORIZONTAL )

		self.m_slider111 = wx.Slider( sbSizer211.GetStaticBox(), wx.ID_ANY, 300, 72, 300, wx.DefaultPosition, wx.DefaultSize, wx.SL_AUTOTICKS|wx.SL_HORIZONTAL|wx.SL_LABELS )
		sbSizer211.Add( self.m_slider111, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_textCtrl11 = wx.TextCtrl( sbSizer211.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.TE_PROCESS_ENTER )
		sbSizer211.Add( self.m_textCtrl11, 0, wx.ALL, 5 )


		bSizer2.Add( sbSizer211, 0, wx.EXPAND, 5 )

		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel31, wx.ID_ANY, u"Exportar archivo" ), wx.VERTICAL )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_filePicker2 = wx.FilePickerCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_SAVE )
		bSizer5.Add( self.m_filePicker2, 0, wx.ALL|wx.EXPAND, 5 )

		m_radioBox12Choices = [ u"PDF", u"PNG" ]
		self.m_radioBox12 = wx.RadioBox( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Tipo archivo", wx.DefaultPosition, wx.DefaultSize, m_radioBox12Choices, 1, wx.RA_SPECIFY_ROWS )
		self.m_radioBox12.SetSelection( 0 )
		bSizer5.Add( self.m_radioBox12, 1, wx.ALL, 5 )


		sbSizer3.Add( bSizer5, 1, wx.EXPAND, 5 )


		bSizer2.Add( sbSizer3, 0, wx.EXPAND, 5 )


		self.m_panel31.SetSizer( bSizer2 )
		self.m_panel31.Layout()
		bSizer2.Fit( self.m_panel31 )
		bSizer51.Add( self.m_panel31, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_scrolledWindow1.SetSizer( bSizer51 )
		self.m_scrolledWindow1.Layout()
		bSizer51.Fit( self.m_scrolledWindow1 )
		self.m_panel3 = wx.Panel( self.m_splitter1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel2 = wx.Panel( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel2.SetFont( wx.Font( 9, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Clarendon Blk BT" ) )

		bSizer3.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_slider6 = wx.Slider( self.m_panel3, wx.ID_ANY, 100, 10, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		bSizer3.Add( self.m_slider6, 0, wx.ALL|wx.EXPAND, 5 )


		self.m_panel3.SetSizer( bSizer3 )
		self.m_panel3.Layout()
		bSizer3.Fit( self.m_panel3 )
		self.m_splitter1.SplitVertically( self.m_scrolledWindow1, self.m_panel3, 394 )
		bSizer1.Add( self.m_splitter1, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_SIZE, self.on_change_size )
		self.m_splitter1.Bind( wx.EVT_SPLITTER_SASH_POS_CHANGED, self.on_sash_changed )
		self.m_filePicker1.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_file_change )
		self.m_textCtrl2112.Bind( wx.EVT_TEXT_ENTER, self.bfbdf )
		self.m_filePicker2.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_separar )
		self.m_panel2.Bind( wx.EVT_PAINT, self.on_paint )
		self.m_slider6.Bind( wx.EVT_SLIDER, self.on_change_size )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def on_change_size( self, event ):
		event.Skip()

	def on_sash_changed( self, event ):
		event.Skip()

	def on_file_change( self, event ):
		event.Skip()

	def bfbdf( self, event ):
		event.Skip()

	def on_separar( self, event ):
		event.Skip()

	def on_paint( self, event ):
		event.Skip()


	def m_splitter1OnIdle( self, event ):
		self.m_splitter1.SetSashPosition( 394 )
		self.m_splitter1.Unbind( wx.EVT_IDLE )


