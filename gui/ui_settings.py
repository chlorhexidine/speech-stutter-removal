from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QIcon)
from PySide6.QtWidgets import (QComboBox, QGridLayout, QLabel,
                               QLayout, QLineEdit, QPushButton, QSizePolicy,
                               QVBoxLayout)
import resources_rc


class Ui_form_settings(object):
    def setupUi(self, form_settings):
        if not form_settings.objectName():
            form_settings.setObjectName(u"form_settings")
        form_settings.resize(981, 346)
        icon = QIcon()
        icon.addFile(u":/icons/icons/settings_black.svg", QSize(), QIcon.Normal, QIcon.Off)
        form_settings.setWindowIcon(icon)
        form_settings.setStyleSheet(u"QWidget {\n"
                                    "  font-family: Arial;\n"
                                    "  font-size: 16pt;\n"
                                    "  font-weight: 400;\n"
                                    "  padding: 10px;\n"
                                    "  background-color: white;\n"
                                    "  margin: 5px;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton {\n"
                                    "  background: transparent;\n"
                                    "  border: 3px solid lightgray;\n"
                                    "  border-radius: 5px;\n"
                                    "  font-size: 14pt;\n"
                                    "  cursor: pointer;\n"
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
                                    "QLineEdit {\n"
                                    "  border: 3px solid lightgray;\n"
                                    "  border-radius: 5px;\n"
                                    "}\n"
                                    "\n"
                                    "QComboBox {\n"
                                    "  border: 3px solid lightgray;\n"
                                    "  border-radius: 5px;\n"
                                    "  min-width: 2em;\n"
                                    "}\n"
                                    "\n"
                                    "QComboBox:editable {\n"
                                    "  background: white;\n"
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
                                    "  border: 0;\n"
                                    "}\n"
                                    "")
        self.verticalLayout = QVBoxLayout(form_settings)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.layout_settings = QGridLayout()
        self.layout_settings.setObjectName(u"layout_settings")
        self.layout_settings.setSizeConstraint(QLayout.SetMinimumSize)
        self.btn_record_folder = QPushButton(form_settings)
        self.btn_record_folder.setObjectName(u"btn_record_folder")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/folder_black.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_record_folder.setIcon(icon1)
        self.btn_record_folder.setIconSize(QSize(24, 24))

        self.layout_settings.addWidget(self.btn_record_folder, 4, 0, 1, 1)

        self.le_record_folder = QLineEdit(form_settings)
        self.le_record_folder.setObjectName(u"le_record_folder")
        self.le_record_folder.setStyleSheet(u"")

        self.layout_settings.addWidget(self.le_record_folder, 4, 1, 1, 1)

        self.lbl_audio_devices = QLabel(form_settings)
        self.lbl_audio_devices.setObjectName(u"lbl_audio_devices")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_audio_devices.sizePolicy().hasHeightForWidth())
        self.lbl_audio_devices.setSizePolicy(sizePolicy)
        self.lbl_audio_devices.setAlignment(Qt.AlignCenter)

        self.layout_settings.addWidget(self.lbl_audio_devices, 0, 0, 1, 2)

        self.lbl_output = QLabel(form_settings)
        self.lbl_output.setObjectName(u"lbl_output")

        self.layout_settings.addWidget(self.lbl_output, 2, 0, 1, 1)

        self.box_output = QComboBox(form_settings)
        self.box_output.setObjectName(u"box_output")

        self.layout_settings.addWidget(self.box_output, 1, 1, 1, 1)

        self.lbl_input = QLabel(form_settings)
        self.lbl_input.setObjectName(u"lbl_input")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lbl_input.sizePolicy().hasHeightForWidth())
        self.lbl_input.setSizePolicy(sizePolicy1)

        self.layout_settings.addWidget(self.lbl_input, 1, 0, 1, 1)

        self.box_input = QComboBox(form_settings)
        self.box_input.setObjectName(u"box_input")

        self.layout_settings.addWidget(self.box_input, 2, 1, 1, 1)

        self.lbl_save_recording = QLabel(form_settings)
        self.lbl_save_recording.setObjectName(u"lbl_save_recording")
        sizePolicy.setHeightForWidth(self.lbl_save_recording.sizePolicy().hasHeightForWidth())
        self.lbl_save_recording.setSizePolicy(sizePolicy)
        self.lbl_save_recording.setAlignment(Qt.AlignCenter)

        self.layout_settings.addWidget(self.lbl_save_recording, 3, 0, 1, 2)

        self.verticalLayout.addLayout(self.layout_settings)

        self.retranslateUi(form_settings)

        QMetaObject.connectSlotsByName(form_settings)

    def retranslateUi(self, form_settings):
        form_settings.setWindowTitle(
            QCoreApplication.translate("form_settings", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438",
                                       None))
        self.btn_record_folder.setText(QCoreApplication.translate("form_settings",
                                                                  u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u043f\u0430\u043f\u043a\u0443",
                                                                  None))
        self.btn_record_folder.setShortcut(QCoreApplication.translate("form_settings", u"Ctrl+O", None))
        self.le_record_folder.setText("")
        self.lbl_audio_devices.setText(QCoreApplication.translate("form_settings",
                                                                  u"\u0417\u0432\u0443\u043a\u043e\u0432\u044b\u0435 \u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u0430",
                                                                  None))
        self.lbl_output.setText(
            QCoreApplication.translate("form_settings", u"\u0417\u0430\u043f\u0438\u0441\u044c", None))
        self.lbl_input.setText(QCoreApplication.translate("form_settings",
                                                          u"\u0412\u043e\u0441\u043f\u0440\u043e\u0438\u0437\u0432\u0435\u0434\u0435\u043d\u0438\u0435",
                                                          None))
        self.lbl_save_recording.setText(QCoreApplication.translate("form_settings",
                                                                   u"\u0421\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u0435 \u0437\u0430\u043f\u0438\u0441\u0438 \u0433\u043e\u043b\u043e\u0441\u0430",
                                                                   None))