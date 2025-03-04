# File and Folder Listing Application

This application provides a graphical user interface (GUI) for listing files and folders within a specified directory, excluding unnecessary directories and files such as `build`, `temp`, `cache`, `logs`, etc.

## Technologies Used

- **Python**: The core programming language used to develop the application.
- **PyQt5**: A set of Python bindings for Qt libraries, used to create the GUI.
- **os**: A Python module providing a way of using operating system-dependent functionality like reading or writing to the file system.

## Features

- **Directory Selection**: Users can select a directory using a file dialog.
- **Recursive Listing**: Lists all files and subdirectories within the selected directory.
- **Exclusion Filter**: Excludes common unnecessary directories and files from the listing.
- **Error Handling**: Gracefully handles permission errors and other exceptions.

## Use Case

This application is ideal for users who need to quickly view the structure of a directory without being overwhelmed by irrelevant files and folders. It can be particularly useful for:

- **Developers**: Quickly inspecting project structures without seeing build artifacts or version control metadata.
- **Administrators**: Auditing directory contents without being cluttered by temporary or cache files.
- **General Users**: Organizing and reviewing file structures in a clean and intuitive manner.

## How to Use

1. **Create a Virtual Environment**:
   ```bash
   python -m venv myenv
   ```

2. **Activate the Virtual Environment**:
   - Windows:
     ```bash
     myenv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source myenv/bin/activate
     ```

3. **Install Dependencies**:
   ```bash
   pip install PyQt5
   ```

4. **Run the Application**:
   ```bash
   python file_lister.py
   ```

5. **Select a Directory**:
   - Use the "Select Folder" button to choose a directory.
   - The application will display the directory structure in the text area, excluding specified directories and files.

## Customization

You can customize the list of excluded directories and files by modifying the `excluir` set in the `listar_arquivos_e_pastas` function. Add or remove items as needed to fit your specific use case.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
