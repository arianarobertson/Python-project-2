# Exercise 2.1: Getting Started with Django

---

## 🎯 Learning Goals

- Explain the MVT (Model-View-Template) architecture and compare it with MVC (Model-View-Controller)
- Summarize Django’s benefits and drawbacks
- Install and get started with Django in a virtual environment

---

## 💭 Reflection Questions

### 1. Vanilla Python vs Django: What are the trade-offs?

Using **vanilla Python** for web development offers complete control and minimal overhead, making it ideal for small scripts, learning purposes, or lightweight applications. However, it lacks built-in tools for managing complex features like user authentication, URL routing, and database interactions, requiring everything to be built from scratch.

In contrast, **Django** provides a full-featured framework with a clear structure, security best practices, and an admin interface out of the box. This makes it ideal for larger or production-ready web applications. The trade-off is reduced flexibility and a steeper learning curve for beginners, as you work within Django’s conventions.

---

### 2. MVT vs MVC: What’s the biggest advantage of MVT?

The **most significant advantage of Django's MVT architecture** over traditional MVC is the way Django handles the "View" and "Template" layers. In Django, the "View" contains the business logic (like a Controller in MVC), while the "Template" is used strictly for rendering the user interface. This separation allows developers to keep presentation logic (HTML, CSS) separate from Python code, which improves readability and maintainability. It also aligns closely with how web development is naturally structured.

---

### 3. Personal Learning Goals for This Achievement

1. **Understand Django's Core Concepts**  
   I want to get a strong grasp of Django’s foundational components, including models, views, templates, and how they interact through the MVT architecture.

2. **Build a Real Django App**  
   I aim to complete a basic but functional Django project by the end of this Achievement, using routes, templates, and database models to build confidence in full-stack development.

3. **Prepare for Real-World Web Development**  
   After completing this Achievement, I want to be comfortable enough with Django to take on small freelance projects or contribute to open-source Django apps on GitHub.

---

# Exercise 2.2: Django Project Set Up

## Learning Goals

- Describe the basic structure of a Django project  
- Summarize the difference between projects and apps  
- Create a Django project and run it locally  
- Create a superuser for a Django web application  

---

## Reflection Questions

### 1. Suppose you’re in an interview. The interviewer gives you their company’s website as an example, asking you to convert the website and its different parts into Django terms. How would you proceed?

I would start by identifying the major components of the website and consider each as a **Django app**. For example, if the company website has a blog section, a product catalog, and a user account system, I would model these as separate apps like `blog`, `products`, and `accounts`. The entire website would be the **Django project** that ties these apps together, managing overall configurations like URLs and settings. Each app would be responsible for its specific functionality, making the code modular and reusable. This approach follows Django’s design principle that projects contain multiple apps which can be developed independently but work together.

---

### 2. In your own words, describe the steps you would take to deploy a basic Django application locally on your system.

First, I would create a new folder for my project and set up a **virtual environment** to isolate dependencies. Next, I would activate the virtual environment and install Django. Using `django-admin startproject`, I would create a new Django project. Then I would navigate into the project directory, run database migrations with `python manage.py migrate` to set up the default database tables, and create a **superuser** account with `python manage.py createsuperuser` for admin access. Finally, I would start the development server with `python manage.py runserver` and access the app locally in the browser.

---

### 3. Do some research about the Django admin site and write down how you’d use it during your web application development.

The Django admin site is a built-in web interface that provides a powerful and user-friendly way to manage a Django application's data. It allows developers and site administrators to add, update, and delete database records through a graphical interface without writing additional code. During development, I would use the admin site to quickly create and modify data models, test database interactions, and manage users and permissions. It is highly customizable, enabling me to register models to the admin and define how they appear and behave. This speeds up development and simplifies maintenance by providing ready-to-use CRUD functionality out of the box.
