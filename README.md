# Circuit Solver README

## Overview

This project provides a web-based circuit solver built with **Flask** that can solve circuits using **Kirchhoff's Current Law (KCL)**. The solver allows users to input circuit components, specify the ground node, and solve the circuit. It then uses symbolic computation (via **SymPy**) to calculate the node voltages.

The project contains the following main components:
- **app.py**: The main Flask web application that handles the server-side logic and web routing.
- **kclsolve.py**: The Python module that contains functions for solving the circuit using Kirchhoff's Current Law.
- **index.html**: The front-end HTML page that allows users to input circuit components and specify the ground node.

---

## Project Structure
circuitsolver/
│
├── app.py                  # Flask app that handles routing and solving logic
├── kclsolve.py             # Module that implements circuit solving logic
├── templates/
│   └── index.html          # HTML form to input circuit data
└── requirements.txt        # Python package dependencies


---

## Requirements

To run this project, you need to have the following Python libraries installed:

- **Flask**: Web framework for building the application.
- **SymPy**: Symbolic mathematics library for solving the system of equations.

### Installation

You can install the required packages by running:

pip install -r requirements.txt   

### Running the Application
1. Clone or Download the Repository
First, make sure you've cloned or downloaded the repository to your local machine.

2. Navigate to the Project Directory
Use the terminal or command prompt to navigate to the project directory where app.py is located.

3. Install Dependencies
If you haven't done so already, install the necessary dependencies by running:

pip install -r requirements.txt

4. Run the Flask Application
Start the Flask web application by running:

python app.py

This will start the server on http://127.0.0.1:5000/ by default.

5. Open the Web Application
Once the application is running, open your web browser and go to http://127.0.0.1:5000/ to interact with the circuit solver.

### How to Use
Enter Circuit Components:

On the main page (index.html), you will be prompted to enter circuit components in the following format:

**<component_type>,<value>,<node1>,<node2>**

For example:

resistor,10,1,2

capacitor,0.001,2,0

voltage_source,5,1,0

This means:
A resistor with a value of 10 ohms between nodes 1 and 2.
A capacitor of 0.001 farads between nodes 2 and 0.
A voltage source of 5V between node 1 and ground (node 0).

Specify the Ground Node:

You must also specify which node is the ground (i.e., node 0). This is done via a numeric input box on the form.
Solve the Circuit:

After entering the components and the ground node, click the Solve Circuit button. The app will process the input, solve the circuit using Kirchhoff's Current Law, and generate the solution.
View Results:

The solution will display the node voltages (in symbolic form) on the page.





