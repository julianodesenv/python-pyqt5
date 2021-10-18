import sys
from validate_cpf import validate_cpf
from generate_cpf import generate_cpf
from PyQt5.QtWidgets import QApplication, QMainWindow
import design


class GeraValidaCPF(QMainWindow, design.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.btnGeraCPF.clicked.connect(self.generate_cpf)
        self.btnValidaCPF.clicked.connect(self.validate_cpf)

    def generate_cpf(self):
        self.labelRetorno.setText(
            str(generate_cpf())
        )

    def validate_cpf(self):
        cpf = self.inputValidaCPF.text()
        self.labelRetorno.setText(
            str(validate_cpf(cpf))
        )


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    gera_validate_cpf = GeraValidaCPF()
    gera_validate_cpf.show()
    qt.exec_()
