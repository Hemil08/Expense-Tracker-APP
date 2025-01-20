Category and Subcategory System with Recursive Display
This Django application implements a category and subcategory system using a self-referencing model, allowing categories to have multiple subcategories. These subcategories can also have their own subcategories, creating a recursive structure. The system displays the categories and subcategories in a nested format similar to a threaded comment system.

**Features**
Recursive Structure: Categories can have subcategories, which can also have their own subcategories.
Django Admin Integration: Easy creation and management of categories and subcategories through the Django Admin interface.
Nested Display: Categories and subcategories are displayed in a hierarchical format on the webpage.
Template Recursion: Recursive display of categories and subcategories using Django template tags.

**Technologies**
HTML,CSS,BOOTSTRAP, DJANGO JINJA FORMATE, PYTHON

Requirements
Python 3.x
Django 3.x or higher
SQLite (default database used by Django, can be switched to other databases)
Installation Guide
Step 1: Clone the Repository
Clone the repository to your local machine.

bash
Copy
Edit
git clone https://github.com/yourusername/category-subcategory-system.git
cd category-subcategory-system
Step 2: Set Up Virtual Environment (Optional but Recommended)
Create and activate a virtual environment to isolate the dependencies.

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Step 3: Install Dependencies
Install the required Python packages listed in requirements.txt.

bash
Copy
Edit
pip install -r requirements.txt

Step 4: Apply Migrations
Run the migrations to set up the database schema.

bash
Copy
Edit
python manage.py migrate

Step 5: Create a Superuser (Optional)
To access Django Admin, create a superuser account.

bash
Copy
Edit
python manage.py createsuperuser
Follow the prompts to create the superuser credentials.

Step 6: Run the Development Server
Start the development server to run the project locally.

bash
Copy
Edit
python manage.py runserver
Navigate to http://127.0.0.1:8000/ in your browser to view the categories and subcategories.

Step 7: Access Django Admin
To manage categories and subcategories, open the Django Admin interface at http://127.0.0.1:8000/admin/. Log in using the superuser credentials you created earlier.

Step 8: Add Categories and Subcategories



File Descriptions
models.py: Contains the Category model with a self-referencing relationship to support subcategories.
views.py: Contains the view logic to retrieve and display categories and subcategories.
admin.py: Registers the Category model for easy management in Django Admin.
templates/: Contains HTML files for rendering categories and subcategories.
urls.py: Defines the URL routing for the application.
License
This project is licensed under the MIT License. See the LICENSE file for more information.

Let me know if you need any further details added to the README file!
