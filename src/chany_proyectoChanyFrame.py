"""Esta interfaz fue creada con la intención de facilitar el trabajo en nuestro taller
de personalizción. Sirve para separar un grande en multiples páginas tamaño carta, oficio
o A4.

Nosotros lo utilizamos para crear mosaicos de hojas A4 y así poder sublimar diseños más
grandes que lo que nos permite imprimir nuestro equipo actual.

Solo requiere de wxpython y pillow adicionales a la librería estandar de python. Esperamos
que pueda ser de utilidad este código para personas que como nosotros nos dedicamos a la
personalización de productos sublimados.

También tenemos una versión para instalar en windows, si no quieres complicarte con la
instalación de dependencias esa es una buena opción, la contraseña de instalación es 
"sandink".

Hemos notado que en ocasiones al exportar a pdf aparece un recuadro negro de fondo en las
imagenes, aún no sabemos que es lo que causa este efecto adverso pero al exportar a png
el mismo archivo este inconveniente desaparece.

autor:Juan Tapia Tinoco 
email:tapiatinocojuan@gmail.com
sitio:https://sandink.shop

Copyright 2025 Sandink
"""

import wx
import chany_proyecto
import math
from PIL import Image, ImageDraw
from os import path

CM2PG = 2.54
anchuras = (
    (8.3, 11.7), #A4
    (8.5, 11), #Carta
    (8.5, 14), #Oficio
)
PDF = 0
PNG = 1

COLORES_SANDINK = {
    "negro" : wx.Colour(0,0,0),
    "gris" : wx.Colour(50,50,50),
    "blanco" : wx.Colour(255,255,255),
    "rosa" : wx.Colour(246,87,197),
    "morado" : wx.Colour(134,69,228),
    "azul" : wx.Colour(3,195,250),
}
# Implementing ChanyFrame
class ChanyFrame( chany_proyecto.ChanyFrame ):
    def __init__( self, parent ):
        chany_proyecto.ChanyFrame.__init__( self, parent )
        #Se personalizan algunos elementos
        self.m_panel31.SetBackgroundColour(COLORES_SANDINK["gris"])
        button1 = self.m_filePicker2.GetPickerCtrl()
        button1.SetLabel("Exportar")
        button1.SetForegroundColour(COLORES_SANDINK["blanco"])
        button1.SetBackgroundColour(COLORES_SANDINK["rosa"])
        button2 = self.m_filePicker1.GetPickerCtrl()
        button2.SetLabel("Elegir")
        button2.SetForegroundColour(COLORES_SANDINK["blanco"])
        button2.SetBackgroundColour(COLORES_SANDINK["rosa"])
        self.logo_icon = wx.Icon(path.join("img", "sandink.png"),  wx.BITMAP_TYPE_ANY)
        self.SetIcon(self.logo_icon)
        #se crean algunas variables internas para le programa
        self.img = None
        self.path = None
        self.tamanio = self.m_radioBox1.GetSelection()
        self.direccion = self.m_radioBox11.GetSelection()
        self.tipo_archivo = self.m_radioBox12.GetSelection()
        self.translape = self.m_slider1.GetValue()
        self.margen = self.m_slider11.GetValue()
        self.dpi = self.m_slider111.GetValue()
        self.size = self.m_slider6.GetValue()
        self.x_off = self.m_slider121.GetValue()
        self.y_off = self.m_slider12.GetValue()
        self.line_width = self.m_slider1211.GetValue()
        self.m_textCtrl2.SetValue(str(self.translape))
        self.m_textCtrl1.SetValue(str(self.margen))
        self.m_textCtrl11.SetValue(str(self.dpi))
        self.m_textCtrl211.SetValue(str(self.x_off))
        self.m_textCtrl2111.SetValue(str(self.y_off))
        self.m_textCtrl2112.SetValue(str(self.line_width))
        self.m_filePicker2.Enable(False)
        self.m_radioBox1.Bind(wx.EVT_RADIOBOX, self.on_radio_box, )        
        self.m_radioBox1.Bind( 
            wx.EVT_RADIOBOX, 
            (lambda evt: self.on_radio_box(evt, "tamanio"))
        )
        self.m_radioBox11.Bind( 
            wx.EVT_RADIOBOX, 
            (lambda evt: self.on_radio_box(evt, "direccion"))
        )
        self.m_radioBox12.Bind( 
            wx.EVT_RADIOBOX, 
            (lambda evt: self.on_radio_box(evt, "tipo_archivo"))
        )
        aux = (
            (self.m_slider1, "translape", self.m_textCtrl2),
            (self.m_slider111, "dpi", self.m_textCtrl11),
            (self.m_slider11, "margen", self.m_textCtrl1),
            (self.m_slider6, "size", None),
            (self.m_slider121, "x_off", self.m_textCtrl211),
            (self.m_slider12, "y_off", self.m_textCtrl2111),
            (self.m_slider1211, "line_width", self.m_textCtrl2112),
        )
        for slider, variable, tex_ctrl in aux:
            slider.Bind(
                wx.EVT_SLIDER,
                (lambda evt, ctrl=tex_ctrl, var=variable: self.on_slider_change(evt, var, ctrl))
            )
            if tex_ctrl is not None:
                tex_ctrl.Bind(
                    wx.EVT_TEXT_ENTER,
                    (lambda evt, ctrl=slider, var=variable: self.on_text_ctrl_change(evt, var, ctrl))
                )

    def on_file_change(self, event):
        obj = event.EventObject
        self.path = obj.GetPath()
        self.img = wx.Image(self.path, wx.BITMAP_TYPE_ANY)
        self.pil_img = Image.open(self.path) 
        self.m_panel2.Refresh()
        self.m_filePicker2.Enable(True)

    def on_radio_box(self, event, atributo):
        """Actualiza las variables de configuracion"""
        obj = event.EventObject
        setattr(self, atributo, obj.GetSelection())
        self.m_panel2.Refresh()

    def on_paint(self, event):
        """Metodo para dibujar sobre un panel"""
        if self.img is not None:
            self.pintar(event.EventObject, self.img)
        event.Skip()
        
    def on_slider_change(self, event, atributo, text_ctrl):
        """Metodo para actualizar la variable asociada a un slider"""
        obj = event.EventObject
        setattr(self, atributo, obj.GetValue())
        if text_ctrl is not None:
            text_ctrl.SetValue(str(obj.GetValue()))
        self.m_panel2.Refresh()
    
    def on_text_ctrl_change(self, event, atributo, slider):
        """Metodo para actualizar la variable asociada a un text_ctrl"""
        obj = event.EventObject
        valor =  obj.GetValue()
        if not valor.isnumeric():
            obj.SetValue(str(slider.GetValue()))
            return
        valor = int(valor)
        min_value, max_value = slider.GetRange()
        if valor < min_value:
            valor = min_value
            obj.SetValue(str(valor))
        if valor > max_value:
            valor = max_value
            obj.SetValue(str(valor))
        slider.SetValue(valor)
        setattr(self, atributo, valor)
        self.m_panel2.Refresh()

    def pintar(self, panel, img):
        """Redibuja una imagen sobre un panel"""
        self.pil_img = Image.open(self.path)  
        width, height = self.pil_img.size
        margen_px = int(self.dpi*self.margen/CM2PG)
        translape_px = int(self.dpi*self.translape/CM2PG)
        x_off = int(self.x_off*self.dpi/CM2PG)
        y_off = int(self.y_off*self.dpi/CM2PG)
        ancho_hoja = int(anchuras[self.tamanio][self.direccion] * self.dpi) 
        ancho_px = ancho_hoja - 2*margen_px
        alto_hoja = int(anchuras[self.tamanio][not self.direccion] * self.dpi)
        alto_px = alto_hoja - 2*margen_px
        num_hojas_x = math.ceil((width - x_off)/ancho_px)
        num_hojas_y = math.ceil((height - y_off)/alto_px)
        img = ImageDraw.Draw(self.pil_img)   
        for i in range(num_hojas_x):
            for j in range(num_hojas_y):
                x = i*(ancho_px-translape_px) + x_off
                y = j*(alto_px-translape_px) + y_off
                try:
                    shape = (x, y, x + ancho_px, y + alto_px)
                    img.rectangle(shape, fill = None, outline ="red", width=self.line_width) 
                except:
                    shape = (x, y, width, height)
                    img.rectangle(shape, fill = None, outline ="red") 
        wx_image = wx.Image(self.pil_img.size[0], self.pil_img.size[1])
        wx_image.SetData(self.pil_img.convert("RGB").tobytes())  

        hasAlpha = self.pil_img.mode[ -1 ] == 'A'
        if hasAlpha:
            myPilImageCopyRGBA = self.pil_img.copy()
            alpha = myPilImageCopyRGBA.split()[-1]
            wx_image.SetAlpha(alpha.tobytes() )
      
        dc = wx.PaintDC(panel)
        dc.Clear()
        dc.SetBackground(wx.Brush("WHITE"))
        ancho, alto = panel.GetSize()
        nuevo_ancho = int(ancho*self.size/100) 
        nuevo_alto = int(alto*self.size/100)
        x = int((ancho - nuevo_ancho)/2)
        y = int((alto - nuevo_alto)/2)
        if 0 in (ancho, alto):
            return 
        if self.img:
            imagenEscalada = wx_image.Scale(
                nuevo_ancho, nuevo_alto, wx.IMAGE_QUALITY_HIGH
            )
            bitmap = imagenEscalada.ConvertToBitmap()
            dc.DrawBitmap(bitmap, x, y, True)
        else:
            pass

    def on_separar(self, event):
        """Separa una imagen en varias"""
        self.pil_img = Image.open(self.path) 
        width, height = self.pil_img.size
        margen_px = int(self.dpi*self.margen/CM2PG)
        translape_px = int(self.dpi*self.translape/CM2PG)
        x_off = int(self.x_off*self.dpi/CM2PG)
        y_off = int(self.y_off*self.dpi/CM2PG)
        ancho_hoja = int(anchuras[self.tamanio][self.direccion] * self.dpi) 
        ancho_px = ancho_hoja - 2*margen_px
        alto_hoja = int(anchuras[self.tamanio][not self.direccion] * self.dpi)
        alto_px = alto_hoja - 2*margen_px
        num_hojas_x = math.ceil((width - x_off)/ancho_px)
        num_hojas_y = math.ceil((height - y_off)/alto_px)
        images = [] 
        for i in range(num_hojas_x):
            for j in range(num_hojas_y):
                x = i*(ancho_px-translape_px) + x_off
                y = j*(alto_px-translape_px) + y_off
                try:
                    im1 = self.pil_img.crop((x, y, x + ancho_px, y + alto_px))
                    w = ancho_px
                    h = alto_px
                except:
                    im1 = self.pil_img.crop((x, y, width, height))
                    w = width - x
                    h = height - y
                new = Image.new(mode="RGBA", size=(ancho_hoja, alto_hoja), color=(255,255,255,0))
                aux = int(margen_px)
                new.paste(
                    im1, 
                    (aux, aux, aux+w, aux+h)
                )
                images.append(new)
        ruta = self.m_filePicker2.GetPath()
        if self.tipo_archivo == PDF:
            img = images.pop(0)
            img.save(f"{ruta}.pdf", save_all=True, append_images=images, dpi=(self.dpi, self.dpi))
        elif self.tipo_archivo == PNG:
            for i, img in enumerate(images):
                img.save(f"{ruta}-{i}.png", save_all=True, append_images=images, dpi=(self.dpi, self.dpi))


        dlg = wx.MessageDialog(None, "Archivo creado exitosamente")
        result = dlg.ShowModal()

    def on_change_size(self, event):
        self.Layout()
        self.Update()
        self.m_panel2.Refresh()

    def on_sash_changed(self, event):
        self.on_change_size(None)


def main():
    app = wx.App()
    ex = ChanyFrame(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()