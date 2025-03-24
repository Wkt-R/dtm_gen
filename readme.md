# DataMatrix Generator (dtm_gen)

This project generates **DataMatrix** codes (or **QR codes** as an alternative) from user input or a PostgreSQL database. It is designed to work on both **Windows** and **Linux** systems.

---

## Table of Contents
1. [Features](#features)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Project Structure](#project-structure)
6. [Troubleshooting](#troubleshooting)
7. [License](#license)
8. [Contributing](#contributing)
9. [Author](#author)

---

## Features
- Generate **DataMatrix** codes from user input.
- Save generated codes as images in a specified directory.
- **Optional**: Generate **QR codes** if DataMatrix is not required.
- **Future Support**: Generating codes from a PostgreSQL database.

---

## Prerequisites

### For Both Windows and Linux
- **Python 3.6 or higher**
- `pip` (Python package manager)

### For Linux
Install `libdmtx` (required for DataMatrix generation):
```bash
sudo apt-get update
sudo apt-get install libdmtx0b dmtx-utils
```

### For Windows
1. Install the **libdmtx DLL** manually (optional for DataMatrix generation).
2. Download the DLL from [libdmtx GitHub](https://github.com/dmtx/libdmtx).
3. Add the DLL to your system's **PATH**.

---

## Installation
### Clone the Repository:
```bash
git clone https://github.com/Wkt-R/dtm_gen.git
cd dtm_gen
```

### Create a Virtual Environment:
#### On Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```
#### On Windows:
```cmd
python -m venv venv
venv\Scripts\activate
```

### Install Dependencies:
```bash
pip install -r requirements.txt
```

---

## Usage
### Generate DataMatrix from User Input
Run the script with the following command:
```bash
python run.py --input 12345678912 --output-dir ./my_datamatrix --size 15
```

#### Arguments:
- `--input`: Input string of **11 numbers** to encode (e.g., `12345678912`).
- `--output-dir`: Directory to save the generated DataMatrix images (default: `./my_datamatrix`).
- `--size`: Size of the DataMatrix image (default: `8`).

#### Example Output:
```
Input data: 12345678912
Processed data: 12, 3, 45678, 912
Processing item 1: 12, 3, 45678, 912
DataMatrix code saved to ./my_datamatrix/datamatrix_1_12_3_45678_912.png
Process completed. DataMatrix image generated in ./my_datamatrix
```

---

## Project Structure
```
dtm_gen/
├── run.py               # script to run the program
├── setup.py             # setup
└── dtm_gen/
    ├── __init__.py
    ├── main.py          # Main script to run the program
    ├── cli.py           # Command-line argument parsing
    ├── db.py            # Database connection and query logic
    ├── generator.py     # DataMatrix/QR code generation logic
    └── processor.py     # Input validation and processing
```

---

## Troubleshooting
### 1. `ImportError: Unable to find dmtx shared library`
- **Linux**: Ensure `libdmtx` is installed:
  ```bash
  sudo apt-get install libdmtx0b dmtx-utils
  ```
- **Windows**: Manually install the libdmtx DLL and add it to your system's **PATH**.

### 2. `The barcode 'datamatrix' is not known`
- The `python-barcode` library does not support DataMatrix. Use **pylibdmtx** instead.

### 3. `ModuleNotFoundError: No module named 'dtm_gen'`
- Ensure the project root directory is in `sys.path`. The `run.py` script handles this automatically.

---

## License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Contributing
Contributions are welcome! Please **open an issue** or **submit a pull request**.

---

## Author
**Wiktor Kondraciuk**  
[wkondraciuk99@gmail.com]  
[GitHub Profile](https://github.com/Wkt-R)

---
