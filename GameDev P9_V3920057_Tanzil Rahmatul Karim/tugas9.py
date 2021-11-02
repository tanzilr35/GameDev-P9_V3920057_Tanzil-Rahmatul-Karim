# Line 2-4 = Import data yg diperlukan
from direct.showbase.ShowBase import ShowBase #untuk memuat sebagian besar modul panda3d dan menyebabkan window 3D muncul
from panda3d.core import WindowProperties #untuk memuat semua prop yang ada di folder ini
from panda3d.core import load_prc_file #untuk memuat file prc

# Line 7 = Memanggil file myconfig.prc yg isinya konfigurasi dasar window, seperti title window dan ukurannya
load_prc_file('myconfig.prc') #agar mempersingkat script coding

class Model3D(ShowBase):
  def __init__(self):
    ShowBase.__init__(self)
    
    # Line 14 = Mengload model untuk gambar 3d dengan tipe file .egg
    self.building = loader.loadModel("models\panda.egg.pz")
    # Line 16 = Atur transformasi posisi dari gambar 3d
    self.building.setPos(0,50,0)
    # Line 18 = Atur ulang model yang akan dirender
    self.building.reparentTo(render)

game = Model3D()
game.run() #main loop untuk menjalankan frame window