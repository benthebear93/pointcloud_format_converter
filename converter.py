
import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.uic import loadUi
from plyfile import PlyData, PlyElement
import open3d as o3d

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi("converter.ui",self)
        self.filedir = 0
        self.browse.clicked.connect(self.browsefiles)
        self.convert.clicked.connect(self.pcd_to_ply)

    def browsefiles(self):
        self.currt_root = os.getcwd()
        self.fname = QFileDialog.getOpenFileName(self, 'Open file', '', 'Pointcloud files (*.pcd *.ply)')
        self.filename.setText(self.fname[0])

    def pcd_to_ply(self):
        select_flag = False
        try:
            pc_filename = self.fname[0].split('/')[-1][:-4]
            pc_file_dir = self.fname[0][:-(len(pc_filename)+4)]
            select_flag = True
        except:
            print('Select the file first')

        if select_flag == True:
            # without open3d"
                #os.chdir(pc_file_dir)
                #commad = 'pcl_pcd2ply -format 0 input ' + pc_filename + ".pcd " + pc_filename +".ply"
                # os.system(commad)
            print("converting...")
            pcd = o3d.io.read_point_cloud(self.fname[0])
            print(pcd)
            o3d.io.write_point_cloud(pc_file_dir+pc_filename+".ply", pcd)
            print("convert done")


app=QApplication(sys.argv)
mainwindow=MainWindow()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(400)
widget.setFixedHeight(300)
widget.show()
sys.exit(app.exec_())