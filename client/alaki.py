from PyQt5.QtCore import pyqtSignal, QThread


class ExecuteThread(QThread):
    my_signal = pyqtSignal(str, str)

    def run(self):
        # do something here
        self.my_signal.connect(self.my_event)
        self.my_signal.emit("hihi", "bye")
        print('here')

    def my_event(self):
        print('event')

