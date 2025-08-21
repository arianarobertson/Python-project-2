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

