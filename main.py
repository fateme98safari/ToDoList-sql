from PySide6.QtWidgets import *
from PySide6.QtCore import *
from functools import partial
from main_window import Ui_MainWindow 
from database import Datebase
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.db=Datebase()
        self.read_from_database()
        self.ui.btn_new_tasks.clicked.connect(self.new_task)
        # self.clicked.connect(self.del_task)
        
    def read_from_database(self):
        tasks=self.db.get_tasks()

        for i in range(len(tasks)):
            new_checkbox=QCheckBox()
            new_label=QLabel()
            new_btn=QPushButton()
            new_date_time=QDateTimeEdit()
            
            
            new_label.setText(tasks[i][1])
            new_checkbox.toggled.connect(partial(self.done,tasks[i][0]))
            new_btn.setText("❌")
            new_btn.clicked.connect(partial(self.del_task, tasks[i][0]))
            

            self.ui.gl_tasks.addWidget(new_label , i ,0)
            self.ui.gl_tasks.addWidget(new_checkbox , i ,1)
            self.ui.gl_tasks.addWidget(new_btn , i ,3)
            self.ui.gl_tasks.addWidget(new_date_time, i ,2)

            # if tasks[i][4]==1:
            #     new_label.setStyleSheet("color: rgb(61, 0, 0);")

    def new_task(self):
        new_title=self.ui.tb_new_task_title.text()
        new_describtion=self.ui.tb_new_task_description.toPlainText()
        dt = self.ui.dateTimeEdit.dateTime()
        feedback=self.db.add_new_tasks(new_title , new_describtion , dt)

        if feedback==True:
          self.read_from_database()
          self.ui.tb_new_task_title.setText("")
          self.ui.tb_new_task_description.setText("")

        else:
            msg_box=QMessageBox()
            msg_box.setText("مشکل رخ داده است")
            msg_box.exec_()

    def del_task(self,id):
        self.db.remove_tasks(id)


    def done(self,id,k):
        self.db.is_done(id)
        

           
if __name__ == "__main__":
    app=QApplication(sys.argv)

    main_window=MainWindow()
    main_window.show()
    app.exec_()

    