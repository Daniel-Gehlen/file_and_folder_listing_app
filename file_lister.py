import os
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, 
                            QPushButton, QFileDialog, QTextEdit, QLabel)

class WebProjectLister(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
        # Diretórios que devem ser completamente ignorados
        self.ignored_dirs = {
            '__pycache__', '.git', '.vscode', '.idea', 'node_modules',
            'vendor', 'dist', 'build', 'cache', 'logs', 'tmp',
            'coverage', '.github', '.circleci', '.docker', 'venv',
            'env', '.venv', 'virtualenv', 'bin', 'include', 'lib',
            'lib64', 'site-packages', 'dist-packages'
        }
        
        # Arquivos que devem ser ignorados
        self.ignored_files = {
            '.DS_Store', 'Thumbs.db', '.env', '.env.local',
            'package-lock.json', 'yarn.lock', '.gitignore',
            '*.log', '*.swp', '*.swo', '.htaccess', '*.pyc',
            '*.pyo', '*.pyd', 'requirements.txt', 'Pipfile',
            'Pipfile.lock', '*.egg-info', '*.dist-info'
        }
        
        # Extensões relevantes para projetos web
        self.relevant_extensions = {
            '.html', '.htm', '.js', '.css', '.scss', '.less',
            '.php', '.py', '.rb', '.java', '.ts', '.jsx', '.tsx',
            '.json', '.xml', '.svg', '.sql', '.md', '.txt'
        }

    def initUI(self):
        self.setWindowTitle('Web Project Structure Viewer')
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        self.label = QLabel('Selecione a pasta raiz do projeto web:')
        layout.addWidget(self.label)

        self.button = QPushButton('Selecionar Pasta')
        self.button.clicked.connect(self.select_folder)
        layout.addWidget(self.button)

        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)
        layout.addWidget(self.text_edit)

        self.setLayout(layout)

    def select_folder(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ShowDirsOnly
        folder = QFileDialog.getExistingDirectory(self, "Selecionar Pasta", options=options)
        
        if folder:
            structure = self.analyze_web_project(folder)
            self.text_edit.setPlainText(structure)

    def should_ignore(self, name, path):
        """Determina se um arquivo/diretório deve ser ignorado"""
        # Ignora diretórios específicos
        if name in self.ignored_dirs:
            return True
            
        # Ignora arquivos específicos
        if name in self.ignored_files:
            return True
            
        # Ignora arquivos ocultos (iniciados com .)
        if name.startswith('.'):
            return True
            
        # Ignora arquivos temporários
        if name.endswith('~') or name.startswith('~'):
            return True
            
        # Ignora pastas de ambiente Python
        if 'venv' in path.split(os.sep) or 'virtualenv' in path.split(os.sep):
            return True
            
        # Ignora pastas de pacotes Python
        if 'site-packages' in path.split(os.sep) or 'dist-packages' in path.split(os.sep):
            return True
            
        return False

    def is_relevant_file(self, name):
        """Determina se um arquivo é relevante para mostrar"""
        _, ext = os.path.splitext(name)
        return ext.lower() in self.relevant_extensions

    def analyze_web_project(self, root_dir, level=0):
        """Analisa a estrutura do projeto web"""
        indent = '    ' * level
        output = []
        
        try:
            items = sorted(os.listdir(root_dir))
            for item in items:
                full_path = os.path.join(root_dir, item)
                
                if self.should_ignore(item, full_path):
                    continue
                    
                if os.path.isdir(full_path):
                    # Processa diretório
                    output.append(f"{indent}📁 {item}/")
                    output.append(self.analyze_web_project(full_path, level + 1))
                else:
                    # Processa arquivo
                    if self.is_relevant_file(item):
                        output.append(f"{indent}📄 {item}")
        except PermissionError:
            output.append(f"{indent}[Permissão negada]")
        except Exception as e:
            output.append(f"{indent}[Erro: {str(e)}]")
            
        return '\n'.join(output)

def main():
    app = QApplication(sys.argv)
    ex = WebProjectLister()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
