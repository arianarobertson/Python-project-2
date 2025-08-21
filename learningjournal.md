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

## Exercise 2.3: Django Models
Learning Goals

Understand Django models, which form the "M" in Django’s Model-View-Template (MVT) architecture.

Create Django apps and define models that represent different entities of the web application.

Write and run automated tests to ensure application quality.

Reflection Questions

1. How do Django models work and what are their benefits?

Django models are Python classes that define the structure of data stored in a database. Each model maps to a single database table, and the attributes of the model represent the fields (columns) in that table. Django provides an Object-Relational Mapping (ORM) system, which means developers can interact with the database using Python code rather than SQL queries.

The benefits of Django models include:

Abstraction: Developers work with Python objects rather than raw SQL, which makes database interactions easier and more intuitive.

Automatic schema migrations: Changes in models can be translated into database schema changes using Django’s migration system.

Data validation: Models allow defining field types and constraints that help maintain data integrity.

Reusability: Models can be reused across different parts of the application, encouraging clean, maintainable code.

Integration: The Django admin interface automatically uses models to provide a management UI for the data, saving development time.

2. Why is it crucial to write test cases from the beginning of a project?

Writing test cases from the start is crucial because it helps ensure the application behaves as expected and prevents bugs from going unnoticed. Tests serve as a safety net for developers, especially when making changes or adding new features.

For example, in a Recipe application, if I write tests early to verify that recipes are created correctly with all required fields and that search functions return accurate results, I can confidently modify or extend the app without breaking core functionality. Automated tests save time in the long run by catching errors early, reducing debugging effort, and improving code quality. They also serve as documentation to explain how different parts of the code are expected to behave.

## Exercise 2.4: Django Views and Templates

Learning Goals

Summarize the process of creating views, templates, and URLs

Explain how the “V” (View) and “T” (Template) parts of the MVT architecture work

Create a frontend page for your web application

Reflection Questions
1. How do Django views work? (Explanation with example)

Django views act as the bridge between the user request and the response sent back to the browser. When a user visits a URL on a Django-powered website, the framework routes the request to the appropriate view based on URL patterns.

A Django view is essentially a Python function or class that:

Receives an HTTP request object as input

Processes any necessary data or logic (e.g., querying a database)

Returns an HTTP response, often rendering an HTML template

For example, a simple function-based view to display a homepage might look like this:

from django.shortcuts import render

def home(request):
    return render(request, 'sales/home.html')


Here, the home function accepts the request and uses Django's render shortcut to return an HTML page (sales/home.html) as the response.

2. When to use function-based views (FBVs) vs. class-based views (CBVs) for reusable code?

If I anticipate reusing a lot of code across various parts of the project, I would choose class-based views (CBVs).

Why?

CBVs provide an object-oriented approach to views, allowing developers to use inheritance and mixins to extend and reuse common functionality easily.

Django has many built-in generic CBVs (like ListView, DetailView) that can be customized for typical web actions, reducing code duplication.

CBVs help organize complex views better by separating different HTTP methods (get, post, etc.) into class methods.

However, for simpler or highly customized views, function-based views (FBVs) are often easier to read and quicker to write.

3. Notes on Django Template Language basics (from Django documentation)

The Django Template Language (DTL) is a lightweight, easy-to-use templating system that helps separate presentation (HTML) from Python code.

Key points:

Variables: Use {{ variable_name }} to insert dynamic content. For example:

<p>Hello, {{ user.username }}!</p>


Tags: Control flow, logic, and structure using tags enclosed in {% %}. Common tags include:

{% if condition %} ... {% else %} ... {% endif %} — conditional logic

{% for item in list %} ... {% endfor %} — loops

{% block %} and {% extends %} — for template inheritance and reuse

Filters: Modify variables' output with filters using the pipe |. For example:

<p>{{ name|lower }}</p>  <!-- converts name to lowercase -->


Comments: Add comments inside templates using {# comment #} which won’t appear in rendered HTML.

This language ensures templates remain secure by auto-escaping variables by default to prevent cross-site scripting (XSS) attacks.