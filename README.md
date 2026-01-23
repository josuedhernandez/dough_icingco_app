# Dough & Icing Co. 🧁
**Home Bakery Website**

A Flask-based web application to manage and showcase the Dough & Icing Co. bakery.

---

## 🚀 Getting Started

Follow these instructions to get your local development environment set up.

### 1. Clone the repository
```bash
git clone [https://github.com/josuedhernandez/dough_icingco_app.git](https://github.com/josuedhernandez/dough_icingco_app.git)
cd dough_icingco_app

### 2. Create a Virtual Environment
```bash
python3 -m venv venv

### 3. Activate the Virtual Environment
```bash
source venv/bin/activate


### 4. Setup Git Ignore
```bash
echo "venv/" >> .gitignore


### 5. Install Dependencies
```bash
pip install -r requirements.txt


🛠️ Running the Application
```bash
python3 app.py

Once running, visit: http://127.0.0.1:5000

📂 Project Structure
* app.py - The main Flask application entry point.

* requirements.txt - List of Python dependencies.

* .gitignore - Tells Git which files to ignore (like venv/).

* templates/ - HTML files (to be created).

* static/ - CSS and Image files (to be created).


📝 Development Notes
Always run pip freeze > requirements.txt after installing new packages.

Do not commit your .env file if it contains sensitive bakery credentials.
