# Exercise 2.1 – Getting Started with Django

## 📚 Overview

This exercise is part of **Achievement 2** in the Django learning path. The focus of this task is to get familiar with Django, understand its architecture, and prepare the local development environment using a virtual environment.

---

## 🎯 Objectives

- Understand Django's MVT (Model-View-Template) architecture
- Compare MVT with traditional MVC architecture
- Identify Django's benefits and drawbacks
- Install Python and Django in a virtual environment
- Verify the setup with version checks and screenshots
- Create a learning journal and reflective answers
- Upload all materials to GitHub

---

## 🛠️ Environment Setup

- ✅ Created a new project folder: `python-project-2`
- ✅ Set up virtual environment: `achievement2-practice`
- ✅ Installed Django using `pip`
- ✅ Verified installations using:
  - `python3 --version`
  - `django-admin --version`

Screenshots of each step are included in the [Exercise 2.1 PDF](./exercise-2.1.pdf).

---

## 📝 Files Included

- `exercise-2.1.pdf` – Contains answers to reflection questions and setup screenshots
- `learningjournal.md` – Personal reflection and learning goals for this achievement
- `README.md` – This file

---

## 📌 Notes

This setup is part of a larger Django learning journey. All code and documentation in this folder are for educational purposes and demonstrate basic environment setup and conceptual understanding.

---

# Task 2.2 – Django Recipe Application Setup

## Overview

This task involves setting up the initial structure for the Recipe application using Django. It includes creating a project folder, setting up a virtual environment, installing Django, creating the Django project, running initial migrations, starting the server, and creating a superuser to access the Django admin panel.

## Steps Completed

1. **Created project folder:** `A2_Recipe_App`  
2. **Set up virtual environment:** `a2-ve-recipeapp` created and activated  
3. **Installed Django** inside the virtual environment  
4. **Created Django project:** Named `recipe_project` inside `A2_Recipe_App`  
5. **Renamed project directory:** From `recipe_project` to `src` for better structure  
6. **Ran migrations:** Initialized the default SQLite database  
7. **Started Django development server:** Verified the project runs locally  
8. **Created superuser:** Set up admin account to manage the app through Django admin interface  
9. **Accessed admin dashboard:** Successfully logged in and verified superuser presence  

## Folder Structure

A2_Recipe_App/
│
├── src/ # Django project files
│ ├── manage.py
│ ├── db.sqlite3
│ ├── recipe_project/ # Django project settings (renamed)
│ └── ...
│
└── a2-ve-recipeapp/ # Virtual environment folder (not always committed)

markdown
Copy code

## Screenshots Included

- `proj_contents_before_renaming.jpg` – Initial project folder contents  
- `proj_contents_after_renaming.jpg` – After renaming `recipe_project` to `src`  
- `server_success_message.jpg` – Browser screenshot showing successful server run  
- `admin-dashboard.jpg` – Django admin dashboard highlighting the superuser  

## Next Steps

- Begin creating Django apps within the project for recipe management  
- Define models, views, and templates to enable recipe input and search functionality  
- Implement user authentication and permissions if needed  
- Continue development following the Achievement 2 Project Brief  

## How to Run Locally

1. Activate the virtual environment:
   ```bash
   source a2-ve-recipeapp/bin/activate
2. Navigate to the src directory:
bash
Copy code
cd src
Run the Django development server:
3. 
bash
Copy code
python manage.py runserver
Access the app in your browser at:
4. 
cpp
Copy code
http://127.0.0.1:8000/
To access the admin panel:
5. 
arduino
Copy code
http://127.0.0.1:8000/admin/
Log in using the superuser credentials created earlier.

---

Recipe App

Welcome to the Recipe App, a Django-based web application designed to help users create, manage, and search for recipes with ease. Users can add detailed recipes including ingredients, cooking times, and step-by-step instructions. The app supports categorizing recipes, tagging them with custom labels, and rating them to find the best dishes quickly.

This project demonstrates key Django concepts such as model relationships, user authentication, and admin interface customization. Whether you're a beginner or an experienced developer, this app serves as a solid foundation for building more advanced culinary applications.

# Exercise 2.4: Django Views and Templates

## Overview

This exercise focuses on building a foundational part of a Django web application — creating views, templates, and URL routing to serve a custom welcome page. You will learn how to define function-based views, design HTML templates, and map URLs to views within your Django project structure.

---

## Objectives

- Understand the role of Django views and templates in the MVT architecture.
- Create a function-based view to handle HTTP requests.
- Develop a custom HTML template for the homepage.
- Configure URL routing to link the homepage URL to the corresponding view.
- Run the Django development server and verify the custom welcome page.

---

## Project Structure

<app>/
├── templates/
│ └── <app>/
│ └── recipes_home.html
├── views.py
├── urls.py
...
bookstore/
└── urls.py

yaml
Copy code

---

## Steps Completed

1. **Created a function-based view** (`home`) in `<app>/views.py` that renders the welcome page template.
2. **Designed the `recipes_home.html` template** with a clean, styled homepage including images and responsive layout.
3. **Defined URL patterns** in `<app>/urls.py` to map the root URL (`""`) to the `home` view.
4. **Included the app URLs** in the main project `bookstore/urls.py` using Django’s `include()` function.
5. **Ran the development server** and verified the custom welcome page loads successfully at `http://127.0.0.1:8000/`.
6. **Captured a screenshot** of the homepage (`welcome.jpg`) and organized it in the GitHub repository under `Exercise 2.4/screenshots/`.

---

## How to Run

1. Activate the virtual environment:

   ```bash
   source a2-ve-recipeapp/bin/activate  # Unix/MacOS
   # or
   .\a2-ve-recipeapp\Scripts\activate   # Windows
Navigate to the project src directory:

bash
Copy code
cd A2_Recipe_App/src
Run the Django development server:

bash
Copy code
python manage.py runserver
Open your browser and go to:

cpp
Copy code
http://127.0.0.1:8000/
Screenshots
Exercise 2.4/screenshots/welcome.jpg — Custom homepage view.

Reflection
For more details on the learning process and reflections, please refer to the learningjournal.md file.

License
This project is for educational purposes.

# 🧑‍🍳 Exercise 2.5 – Recipe App Development

This project is a continuation of the Recipe App, focusing on connecting the **backend models** with the **frontend views**. The exercise covers refining data models, managing data via the Django admin, creating frontend pages (welcome, recipe list, detail views), and writing tests to ensure reliability.

---

## ✅ Task Overview

This task includes the following key steps:

1. **Model Review and Updates**  
   Revisited models from Exercise 2.3 to ensure all necessary fields and relationships were in place. Any changes were documented in the `Task-2.5` file.

2. **Adding Data**  
   - Added records for at least **five recipes** using the Django admin panel.  
   - Each recipe includes categories, ingredients (with allergen flag), tags, ratings, and images.

3. **Frontend Development**  
   - Built a custom **welcome page** inspired by real-world recipe websites.  
   - Created a **recipe list page** displaying all recipe titles, each linking to a detail view.  
   - Designed a **recipe detail page** showing full information and dynamically calculating the **difficulty level**.

4. **Testing**  
   - Added and ran tests for all relevant models and views.  
   - Ensured that relationships (e.g., M2M with tags, ingredients) and view rendering are working correctly.

5. **Documentation and Uploads**  
   - Created a document `Task-2.5` outlining model changes and frontend inspirations.  
   - Captured and uploaded screenshots:
     - `welcome.jpg` – Homepage
     - `recipes-overview.jpg` – Recipe listing
     - `recipe1.jpg`, `recipe2.jpg` – Two recipe detail views  
   - All files uploaded to GitHub as part of the **Exercise 2.5** folder.

---

## 🗃️ Models Overview

### Recipe  
- `title`, `description`, `instructions`, `image`, `created_at`, `updated_at`  
- M2M: `categories`, `tags`, `ingredients` (via `RecipeIngredient`)  
- Method: `calculate_difficulty()` (based on number of ingredients and instruction length)

### Ingredient  
- `name`, `is_allergen`

### RecipeIngredient  
- Connects `Recipe` ↔ `Ingredient`  
- Fields: `ingredient`, `recipe`, `quantity`

### Category  
- `name`, `description`

### Tag  
- `name`

### Rating  
- `user`, `recipe`, `score`, `comment`

---

## 🧪 Running Tests

```bash
# Activate the virtual environment
source ../a2-ve-recipeapp/bin/activate

# Navigate to the src folder
cd A2_Recipe_App/src

# Run tests
python manage.py test
Tests cover:

String representations

Relationships (M2M and FK)

View responses and template rendering

📷 Screenshots (uploaded to GitHub)
📄 Task-2.5 – Document with model updates and frontend inspirations

🖼️ Screenshots (in /Exercise 2.5/Screenshots/):

welcome.jpg

recipes-overview.jpg

recipe1.jpg

recipe2.jpg

💡 Frontend Inspirations
Documented in Task-2.5, with links and commentary on real-world recipe websites that influenced the design.

🚀 Getting Started
To run this project locally:

Clone the repo

bash
Copy code
git clone <your-repo-url>
cd A2_Recipe_App/src
Activate virtual environment

bash
Copy code
source ../a2-ve-recipeapp/bin/activate
Apply migrations and start the server

bash
Copy code
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
Visit in browser:

Home: http://127.0.0.1:8000/recipes/

Admin: http://127.0.0.1:8000/admin/

📂 GitHub Structure
Achievement 2/Exercise 2.5/Task-2.5 – Model updates and design references

Achievement 2/Exercise 2.5/Screenshots/ – All screenshots

src/ – Django project code (recipe_project, recipes, ingredients, etc.)

🔗 Submission Links
🔹 Exercise 2.5 Folder on GitHub

🔹 Recipe App GitHub Repository

📝 License
This project is for educational purposes only – part of Achievement 2 coursework.

# 🍲 Recipe Haven – Task 2.6

## 📌 Overview
This project is part of **Task 2.6** for the Recipe App.  
The goal of this task was to extend the app with **user authentication features** (login, logout, logout success) and style them consistently with the rest of the app.  

Users can now:
- 🔑 Log in to their account
- 🚪 Log out and be redirected to a **successfully logged out page**
- 🏠 Navigate easily with styled buttons/links (Home, Login, Logout)
- 👀 Browse all recipes with recipe name, image, and details preview

---

## ⚙️ Features Implemented
- **Login Page**  
  - Styled to match the welcome page and recipes pages  
  - Centered form with matching button styles  
  - Includes “Back to Home” button  

- **Logout Functionality**  
  - Custom logout handling with a **logout success page**  
  - Styled message confirming successful logout  
  - Buttons to **Login again** or return to **Home**  

- **All Recipes Page (list.html)**  
  - Now displays recipe **name, image, and description preview**  
  - Logout button included in the navigation bar  

---

## 🛠️ Project Structure (Relevant Files)
src/
└── recipes/
└── templates/
├── recipes/
│ ├── welcome.html
│ ├── list.html
│ └── logout_success.html # ✅ new template
└── registration/
└── login.html # ✅ styled login page

yaml
Copy
Edit

---

## 🚀 How to Run the Project

1. **Activate the virtual environment** (if not already active):
   ```bash
   source a2-ve-recipeapp/bin/activate
Run the Django development server:

bash
Copy
Edit
python manage.py runserver
Open in browser:

cpp
Copy
Edit
http://127.0.0.1:8000/
🔑 Authentication Flow
Navigate to Login (🔑 button in nav bar or /login/)

Enter valid credentials

Once logged in, you can browse recipes and see the Logout (🚪) button

On logout, you’ll be redirected to /logout_success/ with styled confirmation and quick links

✅ Task 2.6 Requirements Completed
Added and styled login page

Added logout functionality with redirect

Created logout success page with matching styling

Updated navigation (login/logout/home links)

Styled buttons consistently across pages

