import os
import platform
import sys
from pathlib import Path

from PySide6.QtCore import QUrl
from PySide6.QtMultimedia import (
    QMediaPlayer,
    QAudioOutput,
    QMediaDevices,
    QAudioInput,
    QMediaCaptureSession,
    QMediaRecorder, QMediaFormat,
)
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog, QWidget

from ui_main import Ui_MainWindow
from ui_settings import Ui_form_settings
import files

if platform.system() == 'Windows':
    os.environ['QT_MULTIMEDIA_PREFERRED_PLUGINS'] = 'windowsmediafoundation'


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.filepath = None
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput(QMediaDevices.defaultAudioOutput())
        self.audio_input = QAudioInput(QMediaDevices.defaultAudioInput())
        self.player.setAudioOutput(self.audio_output)

        self.session = QMediaCaptureSession()
        self.session.setAudioInput(self.audio_input)
        self.recorder = QMediaRecorder()
        self.session.setRecorder(self.recorder)
        self.recorder.setMediaFormat(QMediaFormat.MP3)
        self.recorder.setQuality(QMediaRecorder.HighQuality)

        self.disable_before(True)
        self.disable_after(True)

        self.volume = self.ui.slider_volume.value()
        self.initialize_volume()

        self.playback_rate = 1
        self.ui.box_playback_rate.currentTextChanged.connect(self.change_playback_rate)

        self.ui.slider_duration_before.valueChanged.connect(self.player.setPosition)
        self.player.durationChanged.connect(self.update_duration)
        self.player.positionChanged.connect(self.update_position)

        self.form_settings = None
        self.ui.btn_settings.clicked.connect(self.open_settings)

        self.ui.btn_record_stop.clicked.connect(self.record_voice)

        self.ui.btn_choose_file.clicked.connect(self.choose_file)

        self.ui.btn_play_pause_before.clicked.connect(self.play_pause_audio)

    def disable_before(self, disable: bool) -> None:
        to_disable = (
            'lbl_before', 'btn_play_pause_before', 'slider_duration_before', 'lbl_current_time_before',
            'lbl_duration_before'
        )
        for element in to_disable:
            getattr(self.ui, element).setDisabled(disable)

    def disable_after(self, disable: bool) -> None:
        to_disable = (
            'lbl_after', 'btn_play_pause_after', 'slider_duration_after', 'lbl_current_time_after',
            'lbl_duration_after'
        )
        for element in to_disable:
            getattr(self.ui, element).setDisabled(disable)

    def choose_file(self) -> None:
        extensions = "*.mp3 *.wav"

        filepath = QFileDialog.getOpenFileName(
            parent=self,
            caption='Выберите аудиозапись с заиканием',
            filter=extensions,
            dir=files.desktop_path
        )[0]

        self.ui.le_filepath.setText(filepath)
        self.player.setSource(QUrl(filepath))
        self.disable_before(False)

    def play_pause_audio(self) -> None:
        if self.ui.le_filepath.text():
            if self.ui.btn_play_pause_before.isChecked():
                self.player.play()
            else:
                self.player.pause()

    def change_volume(self) -> None:
        self.ui.lbl_volume.setText(str(self.ui.slider_volume.value()))
        self.audio_output.setVolume(self.ui.slider_volume.value() / 100)

        if self.audio_output.volume() == 0:
            self.ui.btn_volume.setChecked(True)
        else:
            self.ui.btn_volume.setChecked(False)

    def turn_off_on_volume(self) -> None:
        if self.ui.btn_volume.isChecked():
            self.volume = self.ui.slider_volume.value()
            self.ui.lbl_volume.setText('0')
            self.ui.slider_volume.setValue(0)
        else:
            self.ui.lbl_volume.setText(str(self.volume))
            self.ui.slider_volume.setValue(self.volume)

        self.audio_output.setVolume(self.ui.slider_volume.value() / 100)

    def initialize_volume(self) -> None:
        self.audio_output.setVolume(self.volume)
        self.ui.slider_volume.valueChanged.connect(self.audio_output.setVolume)
        self.ui.slider_volume.valueChanged.connect(self.change_volume)
        self.ui.btn_volume.clicked.connect(self.turn_off_on_volume)

    def change_playback_rate(self) -> None:
        self.player.setPlaybackRate(float(self.ui.box_playback_rate.currentText()))

    def update_duration(self, duration: int) -> None:
        self.ui.slider_duration_before.setMaximum(duration)

        if duration >= 0:
            self.ui.lbl_duration_before.setText(self.get_duration(duration))

    def update_position(self, position: int) -> None:
        if position >= 0:
            self.ui.lbl_current_time_before.setText(self.get_duration(position))

        self.ui.slider_duration_before.blockSignals(True)
        self.ui.slider_duration_before.setValue(position)
        self.ui.slider_duration_before.blockSignals(False)

    @staticmethod
    def get_duration(ms: int) -> str:
        s = round(ms / 1000)
        m, s = divmod(s, 60)
        h, m = divmod(m, 60)
        return ("%d:%02d:%02d" % (h, m, s)) if h else ("%d:%02d" % (m, s))

    def record_voice(self) -> None:
        if self.ui.btn_record_stop.isChecked():
            self.ui.btn_record_stop.setText('Остановить запись')
            if self.ui.btn_play_pause_before.isChecked():
                self.player.stop()
                self.ui.btn_play_pause_before.setChecked(False)

            files.create_folder_if_not_exists(files.record_folder_path)
            self.filepath = files.get_record_filepath()
            url = QUrl.fromLocalFile(os.fspath(self.filepath))
            self.recorder.setOutputLocation(url)
            self.recorder.record()
        else:
            self.ui.btn_record_stop.setText('Записать голос')
            self.recorder.stop()
            self.ui.le_filepath.setText(os.fspath(self.filepath))
            self.player.setSource(self.recorder.outputLocation())
            self.disable_before(False)

    def open_settings(self) -> None:
        self.form_settings = FormSettings()
        self.form_settings.show()


class FormSettings(QWidget):
    def __init__(self):
        super(FormSettings, self).__init__()
        self.form_ui = Ui_form_settings()
        self.form_ui.setupUi(self)

        self.initialize_audio_outputs()
        self.initialize_audio_inputs()

        self.form_ui.le_record_folder.setText(os.fspath(files.record_folder_path))
        self.form_ui.btn_record_folder.clicked.connect(self.change_record_folder)

    def initialize_audio_inputs(self):
        for device in QMediaDevices.audioInputs():
            self.form_ui.box_input.addItem(device.description())
        self.form_ui.box_input.setCurrentText(QMediaDevices.defaultAudioInput().description())

    def initialize_audio_outputs(self):
        for device in QMediaDevices.audioOutputs():
            self.form_ui.box_output.addItem(device.description())
        self.form_ui.box_output.setCurrentText(QMediaDevices.defaultAudioOutput().description())

    def change_record_folder(self) -> None:
        files.record_folder_path = Path(QFileDialog.getExistingDirectory(
            caption='Выберите папку для сохранения записей голоса'))
        self.form_ui.le_record_folder.setText(os.fspath(files.record_folder_path))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
