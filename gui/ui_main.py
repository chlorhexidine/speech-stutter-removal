from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QCursor,
                           QFont, QIcon)
from PySide6.QtWidgets import (QComboBox, QGridLayout, QHBoxLayout,
                               QLabel, QLineEdit, QPushButton,
                               QSizePolicy, QSlider, QVBoxLayout, QWidget)
import resources_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(770, 600)
        MainWindow.setMinimumSize(QSize(770, 600))
        icon = QIcon()
        icon.addFile(u":/icons/icons/record_voice_over_black.svg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget {\n"
                                 "  font-family: Arial;\n"
                                 "  font-size: 16pt;\n"
                                 "  font-weight: 400;\n"
                                 "  margin: 10px;\n"
                                 "  padding: 10px;\n"
                                 "  background-color: white;\n"
                                 "}\n"
                                 "\n"
                                 "QLabel#lbl_duration_after,\n"
                                 "#lbl_duration_before,\n"
                                 "#lbl_current_time_before,\n"
                                 "#lbl_current_time_after {\n"
                                 "  font-size: 12pt;\n"
                                 "  margin: 0;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton {\n"
                                 "  background: transparent;\n"
                                 "  border: 3px solid lightgray;\n"
                                 "  border-radius: 5px;\n"
                                 "  font-size: 14pt;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton#btn_play_pause_before,\n"
                                 "#btn_play_pause_after,\n"
                                 "#btn_volume {\n"
                                 "  padding: 5px;\n"
                                 "  margin-right: 0;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:hover {\n"
                                 "  background-color: lightgray;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:pressed {\n"
                                 "  background-color: gray;\n"
                                 "  border-color: gray;\n"
                                 "}\n"
                                 "\n"
                                 "QSlider::groove:horizontal {\n"
                                 "  border: 1px solid gray;\n"
                                 "  background: white;\n"
                                 "  height: 15px;\n"
                                 "  border-radius: 8px;\n"
                                 "}\n"
                                 "\n"
                                 "QSlider::sub-page:horizontal {\n"
                                 "  background: qlineargradient(\n"
                                 "    x1: 0,\n"
                                 "    y1: 0,\n"
                                 ""
                                 "    x2: 0,\n"
                                 "    y2: 1,\n"
                                 "    stop: 0 lightgray,\n"
                                 "    stop: 1 gray\n"
                                 "  );\n"
                                 "  height: 10px;\n"
                                 "  border-radius: 5px;\n"
                                 "}\n"
                                 "\n"
                                 "QSlider::add-page:horizontal {\n"
                                 "  background: white;\n"
                                 "  border: 3px solid lightgray;\n"
                                 "  height: 10px;\n"
                                 "  border-radius: 5px;\n"
                                 "}\n"
                                 "\n"
                                 "QSlider::handle:horizontal {\n"
                                 "  background: qlineargradient(\n"
                                 "    x1: 0,\n"
                                 "    y1: 0,\n"
                                 "    x2: 1,\n"
                                 "    y2: 1,\n"
                                 "    stop: 0 #eee,\n"
                                 "    stop: 1 #ccc\n"
                                 "  );\n"
                                 "  width: 20px;\n"
                                 "  margin-top: -3px;\n"
                                 "  margin-bottom: -3px;\n"
                                 "  border: 1px solid gray;\n"
                                 "  border-radius: 10px;\n"
                                 "}\n"
                                 "\n"
                                 "QSlider::handle:horizontal:hover {\n"
                                 "  background: qlineargradient(\n"
                                 "    x1: 0,\n"
                                 "    y1: 0,\n"
                                 "    x2: 1,\n"
                                 "    y2: 1,\n"
                                 "    stop: 0 #fff,\n"
                                 "    stop: 1 #ddd\n"
                                 "  );\n"
                                 "}\n"
                                 "")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_title = QLabel(self.centralwidget)
        self.lbl_title.setObjectName(u"lbl_title")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_title.sizePolicy().hasHeightForWidth())
        self.lbl_title.setSizePolicy(sizePolicy)
        self.lbl_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_title)

        self.layout_file = QHBoxLayout()
        self.layout_file.setObjectName(u"layout_file")
        self.btn_choose_file = QPushButton(self.centralwidget)
        self.btn_choose_file.setObjectName(u"btn_choose_file")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/folder_black.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_choose_file.setIcon(icon1)
        self.btn_choose_file.setIconSize(QSize(24, 24))

        self.layout_file.addWidget(self.btn_choose_file)

        self.le_filepath = QLineEdit(self.centralwidget)
        self.le_filepath.setObjectName(u"le_filepath")
        self.le_filepath.setStyleSheet(u"QLineEdit {\n"
                                       "  border: 3px solid lightgray;\n"
                                       "  border-radius: 5px;\n"
                                       "  font-size: 14pt;\n"
                                       "  margin-left: 0;\n"
                                       "}\n"
                                       "")

        self.layout_file.addWidget(self.le_filepath)

        self.verticalLayout.addLayout(self.layout_file)

        self.layout_record = QHBoxLayout()
        self.layout_record.setObjectName(u"layout_record")
        self.btn_record_stop = QPushButton(self.centralwidget)
        self.btn_record_stop.setObjectName(u"btn_record_stop")
        self.btn_record_stop.setStyleSheet(u"QPushButton:checked {\n"
                                           "	background-color: #ff735e;\n"
                                           "	border-color: #ff735e;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:checked:hover {\n"
                                           "	background-color: #e33e33;\n"
                                           "	border-color: #e33e33;\n"
                                           "}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/mic_black.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/icons/icons/stop_black.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_record_stop.setIcon(icon2)
        self.btn_record_stop.setIconSize(QSize(24, 24))
        self.btn_record_stop.setCheckable(True)

        self.layout_record.addWidget(self.btn_record_stop)

        self.btn_settings = QPushButton(self.centralwidget)
        self.btn_settings.setObjectName(u"btn_settings")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_settings.sizePolicy().hasHeightForWidth())
        self.btn_settings.setSizePolicy(sizePolicy1)
        self.btn_settings.setStyleSheet(u"margin-left: 0;")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/settings_black.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_settings.setIcon(icon3)
        self.btn_settings.setIconSize(QSize(24, 24))

        self.layout_record.addWidget(self.btn_settings)

        self.verticalLayout.addLayout(self.layout_record)

        self.layout_before = QGridLayout()
        self.layout_before.setObjectName(u"layout_before")
        self.slider_duration_before = QSlider(self.centralwidget)
        self.slider_duration_before.setObjectName(u"slider_duration_before")
        self.slider_duration_before.setMinimumSize(QSize(560, 0))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(16)
        font.setBold(False)
        self.slider_duration_before.setFont(font)
        self.slider_duration_before.setCursor(QCursor(Qt.PointingHandCursor))
        self.slider_duration_before.setStyleSheet(u"")
        self.slider_duration_before.setOrientation(Qt.Horizontal)
        self.slider_duration_before.setTickPosition(QSlider.TicksBelow)
        self.slider_duration_before.setTickInterval(5)

        self.layout_before.addWidget(self.slider_duration_before, 1, 2, 1, 1)

        self.btn_play_pause_before = QPushButton(self.centralwidget)
        self.btn_play_pause_before.setObjectName(u"btn_play_pause_before")
        self.btn_play_pause_before.setSizeIncrement(QSize(0, 1))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(14)
        font1.setBold(False)
        self.btn_play_pause_before.setFont(font1)
        self.btn_play_pause_before.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/play_arrow_black.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/icons/icons/pause_black.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_play_pause_before.setIcon(icon4)
        self.btn_play_pause_before.setIconSize(QSize(24, 24))
        self.btn_play_pause_before.setCheckable(True)

        self.layout_before.addWidget(self.btn_play_pause_before, 1, 0, 1, 1)

        self.lbl_current_time_before = QLabel(self.centralwidget)
        self.lbl_current_time_before.setObjectName(u"lbl_current_time_before")
        self.lbl_current_time_before.setStyleSheet(u"")

        self.layout_before.addWidget(self.lbl_current_time_before, 1, 1, 1, 1)

        self.lbl_duration_before = QLabel(self.centralwidget)
        self.lbl_duration_before.setObjectName(u"lbl_duration_before")
        self.lbl_duration_before.setStyleSheet(u"")

        self.layout_before.addWidget(self.lbl_duration_before, 1, 3, 1, 1)

        self.lbl_before = QLabel(self.centralwidget)
        self.lbl_before.setObjectName(u"lbl_before")
        sizePolicy.setHeightForWidth(self.lbl_before.sizePolicy().hasHeightForWidth())
        self.lbl_before.setSizePolicy(sizePolicy)
        self.lbl_before.setAlignment(Qt.AlignCenter)

        self.layout_before.addWidget(self.lbl_before, 0, 0, 1, 4)

        self.verticalLayout.addLayout(self.layout_before)

        self.layout_after = QGridLayout()
        self.layout_after.setObjectName(u"layout_after")
        self.btn_play_pause_after = QPushButton(self.centralwidget)
        self.btn_play_pause_after.setObjectName(u"btn_play_pause_after")
        self.btn_play_pause_after.setSizeIncrement(QSize(0, 1))
        self.btn_play_pause_after.setFont(font1)
        self.btn_play_pause_after.setStyleSheet(u"")
        self.btn_play_pause_after.setIcon(icon4)
        self.btn_play_pause_after.setIconSize(QSize(24, 24))
        self.btn_play_pause_after.setCheckable(True)

        self.layout_after.addWidget(self.btn_play_pause_after, 1, 0, 1, 1)

        self.lbl_current_time_after = QLabel(self.centralwidget)
        self.lbl_current_time_after.setObjectName(u"lbl_current_time_after")
        self.lbl_current_time_after.setStyleSheet(u"")

        self.layout_after.addWidget(self.lbl_current_time_after, 1, 1, 1, 1)

        self.slider_duration_after = QSlider(self.centralwidget)
        self.slider_duration_after.setObjectName(u"slider_duration_after")
        self.slider_duration_after.setCursor(QCursor(Qt.PointingHandCursor))
        self.slider_duration_after.setStyleSheet(u"")
        self.slider_duration_after.setOrientation(Qt.Horizontal)
        self.slider_duration_after.setTickPosition(QSlider.TicksBelow)
        self.slider_duration_after.setTickInterval(5)

        self.layout_after.addWidget(self.slider_duration_after, 1, 2, 1, 1)

        self.lbl_duration_after = QLabel(self.centralwidget)
        self.lbl_duration_after.setObjectName(u"lbl_duration_after")
        self.lbl_duration_after.setStyleSheet(u"")

        self.layout_after.addWidget(self.lbl_duration_after, 1, 3, 1, 1)

        self.lbl_after = QLabel(self.centralwidget)
        self.lbl_after.setObjectName(u"lbl_after")
        sizePolicy.setHeightForWidth(self.lbl_after.sizePolicy().hasHeightForWidth())
        self.lbl_after.setSizePolicy(sizePolicy)
        self.lbl_after.setAlignment(Qt.AlignCenter)

        self.layout_after.addWidget(self.lbl_after, 0, 0, 1, 4)

        self.verticalLayout.addLayout(self.layout_after)

        self.layout_playback_settings = QHBoxLayout()
        self.layout_playback_settings.setObjectName(u"layout_playback_settings")
        self.btn_volume = QPushButton(self.centralwidget)
        self.btn_volume.setObjectName(u"btn_volume")
        self.btn_volume.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/volume_up_black.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon5.addFile(u":/icons/icons/volume_off_black.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_volume.setIcon(icon5)
        self.btn_volume.setIconSize(QSize(24, 24))
        self.btn_volume.setCheckable(True)

        self.layout_playback_settings.addWidget(self.btn_volume)

        self.lbl_volume = QLabel(self.centralwidget)
        self.lbl_volume.setObjectName(u"lbl_volume")
        self.lbl_volume.setStyleSheet(u"margin: 0;")

        self.layout_playback_settings.addWidget(self.lbl_volume)

        self.slider_volume = QSlider(self.centralwidget)
        self.slider_volume.setObjectName(u"slider_volume")
        self.slider_volume.setStyleSheet(u"QSlider::sub-page:horizontal {\n"
                                         "  background: qlineargradient(\n"
                                         "    x1: 0,\n"
                                         "    y1: 0,\n"
                                         "    x2: 0,\n"
                                         "    y2: 1,\n"
                                         "    stop: 0 lightgray,\n"
                                         "    stop: 1 #668925\n"
                                         "  );\n"
                                         "}")
        self.slider_volume.setMaximum(100)
        self.slider_volume.setPageStep(10)
        self.slider_volume.setSliderPosition(50)
        self.slider_volume.setOrientation(Qt.Horizontal)

        self.layout_playback_settings.addWidget(self.slider_volume)

        self.lbl_playback_rate = QLabel(self.centralwidget)
        self.lbl_playback_rate.setObjectName(u"lbl_playback_rate")
        self.lbl_playback_rate.setStyleSheet(u"margin: 0;")

        self.layout_playback_settings.addWidget(self.lbl_playback_rate)

        self.box_playback_rate = QComboBox(self.centralwidget)
        self.box_playback_rate.addItem("")
        self.box_playback_rate.addItem("")
        self.box_playback_rate.addItem("")
        self.box_playback_rate.addItem("")
        self.box_playback_rate.addItem("")
        self.box_playback_rate.addItem("")
        self.box_playback_rate.addItem("")
        self.box_playback_rate.addItem("")
        self.box_playback_rate.setObjectName(u"box_playback_rate")
        self.box_playback_rate.setStyleSheet(u"QComboBox {\n"
                                             "  border: 3px solid lightgray;\n"
                                             "  border-radius: 3px;\n"
                                             "  width: 40px;\n"
                                             "  padding: 1px 15px 1px 3px;\n"
                                             "  margin-left: 0;\n"
                                             "}\n"
                                             "\n"
                                             "QComboBox:!editable:on,\n"
                                             "QComboBox::drop-down:editable:on {\n"
                                             "  background-color: gray;\n"
                                             "  border-color: gray;\n"
                                             "}\n"
                                             "\n"
                                             "QComboBox:on {\n"
                                             "  padding-top: 3px;\n"
                                             "  padding-left: 4px;\n"
                                             "}\n"
                                             "\n"
                                             "QComboBox::drop-down {\n"
                                             "  border: 0px;\n"
                                             "}\n"
                                             "")
        self.box_playback_rate.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.layout_playback_settings.addWidget(self.box_playback_rate)

        self.verticalLayout.addLayout(self.layout_playback_settings)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.box_playback_rate.setCurrentIndex(3)

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow",
                                                             u"\u041a\u043e\u0440\u0440\u0435\u043a\u0446\u0438\u044f \u0437\u0430\u0438\u043a\u0430\u043d\u0438\u044f",
                                                             None))
        self.lbl_title.setText(QCoreApplication.translate("MainWindow",
                                                          u"\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 \u0434\u043b\u044f \u043a\u043e\u0440\u0440\u0435\u043a\u0446\u0438\u0438 \u0437\u0430\u0438\u043a\u0430\u043d\u0438\u044f",
                                                          None))
        self.btn_choose_file.setText(QCoreApplication.translate("MainWindow",
                                                                u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0444\u0430\u0439\u043b",
                                                                None))
        self.btn_choose_file.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
        self.le_filepath.setText("")
        self.le_filepath.setPlaceholderText(QCoreApplication.translate("MainWindow",
                                                                       u"D:\\downloads\\\u0437\u0430\u043f\u0438\u0441\u044c \u043c\u043e\u0435\u0433\u043e \u0433\u043e\u043b\u043e\u0441\u0430.wav",
                                                                       None))
        self.btn_record_stop.setText(QCoreApplication.translate("MainWindow",
                                                                u"\u0417\u0430\u043f\u0438\u0441\u0430\u0442\u044c \u0433\u043e\u043b\u043e\u0441",
                                                                None))
        self.btn_settings.setText("")
        self.btn_play_pause_before.setText("")
        self.lbl_current_time_before.setText(QCoreApplication.translate("MainWindow", u"0:00", None))
        self.lbl_duration_before.setText(QCoreApplication.translate("MainWindow", u"0:00", None))
        self.lbl_before.setText(QCoreApplication.translate("MainWindow",
                                                           u"\u0417\u0430\u043f\u0438\u0441\u044c \u0434\u043e \u043a\u043e\u0440\u0440\u0435\u043a\u0446\u0438\u0438",
                                                           None))
        self.btn_play_pause_after.setText("")
        self.lbl_current_time_after.setText(QCoreApplication.translate("MainWindow", u"0:00", None))
        self.lbl_duration_after.setText(QCoreApplication.translate("MainWindow", u"0:00", None))
        self.lbl_after.setText(QCoreApplication.translate("MainWindow",
                                                          u"\u0417\u0430\u043f\u0438\u0441\u044c \u043f\u043e\u0441\u043b\u0435 \u043a\u043e\u0440\u0440\u0435\u043a\u0446\u0438\u0438",
                                                          None))
        self.btn_volume.setText("")
        self.lbl_volume.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.lbl_playback_rate.setText(QCoreApplication.translate("MainWindow",
                                                                  u"\u0421\u043a\u043e\u0440\u043e\u0441\u0442\u044c \u0432\u043e\u0441\u043f\u0440\u043e\u0438\u0437\u0432\u0435\u0434\u0435\u043d\u0438\u044f",
                                                                  None))
        self.box_playback_rate.setItemText(0, QCoreApplication.translate("MainWindow", u"0.25", None))
        self.box_playback_rate.setItemText(1, QCoreApplication.translate("MainWindow", u"0.5", None))
        self.box_playback_rate.setItemText(2, QCoreApplication.translate("MainWindow", u"0.75", None))
        self.box_playback_rate.setItemText(3, QCoreApplication.translate("MainWindow", u"1.0", None))
        self.box_playback_rate.setItemText(4, QCoreApplication.translate("MainWindow", u"1.25", None))
        self.box_playback_rate.setItemText(5, QCoreApplication.translate("MainWindow", u"1.5", None))
        self.box_playback_rate.setItemText(6, QCoreApplication.translate("MainWindow", u"1.75", None))
        self.box_playback_rate.setItemText(7, QCoreApplication.translate("MainWindow", u"2.0", None))

        self.box_playback_rate.setCurrentText(QCoreApplication.translate("MainWindow", u"1.0", None))