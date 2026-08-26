# VecCal

VecCal is a simple web-based vector calculus calculator developed as a course project for **Electromagnetics**.

The project was created to make common vector calculus operations easier to calculate and visualize through a basic web interface. It uses Python and SymPy for the mathematical calculations and Flask to connect the backend with the frontend.

## Features

VecCal currently supports:

* Gradient
* Divergence
* Curl

The calculations are performed symbolically using SymPy.

## Technologies Used

* Python
* Flask
* SymPy
* Flask-CORS
* HTML
* CSS
* JavaScript

## Project Structure

```text
VecCal/
│
├── backend/
│   ├── app.py
│   └── utils/
│       └── vector_calculus.py
│
├── templates/
│   └── index.html
│
├── requirements.txt
├── README.md
├── LICENSE
└── report.md
```

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Tanish225/VecCal.git
cd VecCal
```

### 2. Create a virtual environment

#### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### Windows

```powershell
py -m venv .venv
.venv\Scripts\activate
```

### 3. Install the required packages

```bash
pip install -r requirements.txt
```

### 4. Start the application

#### macOS / Linux

```bash
python backend/app.py
```

#### Windows

```powershell
py backend\app.py
```

The Flask server will start on port `5050`.

Open the following address in your browser:

```text
http://localhost:5050
```

## How It Works

The user enters a mathematical expression and selects the required vector calculus operation from the web interface.

The frontend sends the input to the Flask backend. The backend then uses SymPy to perform the required symbolic calculation and sends the result back to the browser.

The basic flow is:

```text
User Input
    |
    v
Web Interface
    |
    v
Flask Backend
    |
    v
SymPy Calculation
    |
    v
Result
```

## Example

For a scalar function such as:

```text
x^2*y + y^2*z + z^2*x
```

VecCal can calculate its gradient.

For a vector field such as:

```text
(x*y, y*z, z*x)
```

it can calculate the divergence or curl.

## Course Context

This project was developed as part of my **Electromagnetics course during my second year of B.Tech**.

The main idea was to apply vector calculus concepts such as gradient, divergence, and curl in a practical programming project.

## Future Improvements

Some improvements that could be added in the future include:

* Better input validation
* More vector calculus operations
* Improved error handling
* Mathematical expressions rendered using LaTeX
* More interactive visualization of vector fields
* Unit tests for the calculation functions

## License

This project is licensed under the MIT License.

## Author

Tanish Sinha

GitHub: https://github.com/Tanish225
