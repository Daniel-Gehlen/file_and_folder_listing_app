import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QTextEdit, QLabel

def listar_arquivos_e_pastas(caminho_pasta):
    # List of directories and files to exclude
    excluir = {'build', 'temp', 'cache', 'logs', '__pycache__', '.git', '.vscode', '.idea', '.next', 'vendor-chunks', 'development', 'media', 'webpack', 'types', 'ui', 'node_modules', '.d.ts'}

    def formatar_entrada(caminho, nivel=0):
        indentacao = '  ' * nivel
        resultado = []
        if os.path.isdir(caminho):
            nome_pasta = os.path.basename(caminho)
            if nome_pasta not in excluir:
                resultado.append(f'{indentacao}Pasta: {nome_pasta}')
                try:
                    for item in sorted(os.listdir(caminho)):
                        if item not in excluir:
                            resultado.extend(formatar_entrada(os.path.join(caminho, item), nivel + 1))
                except PermissionError:
                    resultado.append(f'{indentacao}[Permissão negada]')
                except Exception as e:
                    resultado.append(f'{indentacao}[Erro: {e}]')
        else:
            nome_arquivo = os.path.basename(caminho)
            if nome_arquivo not in excluir:
                resultado.append(f'{indentacao}Arquivo: {nome_arquivo}')
        return resultado

    if not os.path.exists(caminho_pasta):
        return "O caminho fornecido não existe."

    linhas = formatar_entrada(caminho_pasta)
    if not linhas:
        return "Nenhuma entrada foi encontrada."
    else:
        return '\n'.join(linhas)

class FileListerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Listar Arquivos e Pastas')
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        self.label = QLabel('Selecione uma pasta para listar seus arquivos e subpastas:')
        layout.addWidget(self.label)

        self.button = QPushButton('Selecionar Pasta')
        self.button.clicked.connect(self.selecionar_pasta)
        layout.addWidget(self.button)

        self.text_edit = QTextEdit()
        layout.addWidget(self.text_edit)

        self.setLayout(layout)

    def selecionar_pasta(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ShowDirsOnly
        pasta_selecionada = QFileDialog.getExistingDirectory(self, "Selecionar Pasta", options=options)
        if pasta_selecionada:
            resultado = listar_arquivos_e_pastas(pasta_selecionada)
            self.text_edit.setPlainText(resultado)

def main():
    app = QApplication(sys.argv)
    ex = FileListerApp()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

