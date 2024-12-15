1 Set Up a Python Environment
You can use a global Python installation, but it's often recommended to use a virtual environment for each project.

To create a virtual environment, open a terminal in VS Code by selecting Terminal > New Terminal from the top menu.

Run the following command to create a virtual environment:

bash
Copy code
python -m venv venv
Activate the virtual environment:

Windows: .\venv\Scripts\activate
macOS/Linux: source venv/bin/activate

2 Install NumPy
With the virtual environment activated, install NumPy using pip:

bash
Copy code
pip install numpy
If you are not using a virtual environment, simply run:

bash
Copy code
pip install numpy