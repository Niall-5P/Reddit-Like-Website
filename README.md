# Reddit-Like Website

A community-driven, news and discussion website, where users can create posts, comment on articles, and engage in meaningful discussions. This project was built as part of the Full-Stack Toolkit Portfolio requirement, showcasing Django as the main framework with additional libraries and services.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Live Demo / Deployment](#live-demo--deployment)
3. [Design](#design)
   - [Wireframes and Mockups](#wireframes-and-mockups)
   - [Design Rationale](#design-rationale)
4. [User Experience (UX)](#user-experience-ux)
   - [User Stories](#user-stories)
   - [Site Goals](#site-goals)
5. [Features](#features)
   - [Existing Features](#existing-features)
   - [Future Features](#future-features)
6. [Data Model](#data-model)
7. [Technologies Used](#technologies-used)
8. [Testing](#testing)
9. [Deployment](#deployment)
10. [Credits](#credits)
11. [Bug](#bug)


---

## Project Overview

This project aims to create a Reddit-like news and discussion platform, allowing users to:

- Read and post articles or discussion topics.
- Comment on existing posts.
- Manage their own content through editing or deleting comments.

Developed throughout the **Code Institute** Full-Stack Toolkit learning path, this project demonstrates the use of Django’s MTV (Model-Template-View) pattern, user authentication, and CRUD functionality on both the front and back end.

**GitHub Repository:**  
[Reddit-Like Website GitHub Repo](https://github.com/Niall-5P/Reddit-Like-Website.git)

---

## Live Demo / Deployment


- [https://git.heroku.com/reddit-like-site.git](#) 

---


## Design

### Wireframes and Mockups
Below are the wireframes created to plan the layout and user flow of the site.

1. **Home Page**
   ![Home Page Wireframe](/Users/student/Desktop/Reddit-Like-Website/static/images/HomePage.png)

2. **Testimonial Page**
   ![Testimonial Wireframe](/Users/student/Desktop/Reddit-Like-Website-main/static/images/TestimonialPage.png)

3. **Register account page**
   ![Register account](/Users/student/Desktop/Reddit-Like-Website-main/static/images/RegisterAccountPage.png)

4. **Login page**
   ![Login page](/Users/student/Desktop/Reddit-Like-Website-main/static/images/LoginPage.png)

### Design Rationale
To capture the familiar feel of a Reddit-style platform, a predominantly white background is used throughout the site. This choice helps ensure that text-based content, such as post titles and comments, remains the main focal point. A white background also mirrors Reddit’s clean, minimalist appearance, offering a sense of familiarity for users who may have experience with the original platform. Additional accent colors can be placed strategically for navigation elements or buttons, helping them stand out against the background while maintaining an overall clean and modern aesthetic.

## User Experience (UX)

### User Stories

1. **As a Site User**, I want to sign up and log in so that I can create my own posts and interact with content.  
2. **As a Site User**, I want to be able to comment on posts so that I can engage with other users.  
3. **As a Site User**, I want to edit or delete my own comments so I can correct mistakes or remove content.  
4. **As a Site Admin**, I want to moderate posts and comments via the admin panel for inappropriate content.  

### Site Goals

- Provide a clean, responsive interface for reading, creating, and commenting on user-generated content.
- Make site moderation simple for administrators, ensuring a positive community environment.

---

## Features

### Existing Features

1. **Home Page & Blog Posts**  
   - Displays a list of published posts with pagination.  
   - Shows post titles, excerpts, authors, and timestamps.

2. **Post Detail Page**  
   - Displays the full post content.  
   - Shows approved comments and a form for authenticated users to add new comments.

3. **User Authentication**  
   - Utilizes Django’s `allauth` for account registration, login, and logout.  
   - Logged-in users can create posts, comment, and edit/delete their comments.

4. **Comment Moderation**  
   - Site Admin can approve or reject comments in the admin panel.  
   - Users see only approved comments.

5. **Custom Testimonials**  
   - Users can submit testimonials (a custom model) to share site feedback.  
   - Admin reviews and approves testimonials for public display.

6. **Responsive Layout**  
   - Built with Bootstrap 5, ensuring a mobile-friendly layout.

### Future Features

- **Search & Filter**: To quickly find posts by keywords or categories.  
- **User Profiles**: Show user statistics, such as number of posts or comments.  
- **Categories/Tags**: Organize posts into topics for easier navigation.

---

## Data Model

Below is an overview of key models in the project:

1. **Post**  
   - `title` (CharField, unique)  
   - `slug` (SlugField, unique)  
   - `author` (ForeignKey → User)  
   - `featured_image` (CloudinaryField / placeholder)  
   - `content` (TextField)  
   - `excerpt` (TextField, optional)  
   - `status` (IntegerField: Draft/Published)  
   - `created_on` (DateTimeField)  
   - `updated_on` (DateTimeField)

2. **Comment**  
   - `post` (ForeignKey → Post)  
   - `author` (ForeignKey → User)  
   - `body` (TextField)  
   - `approved` (BooleanField)  
   - `created_on` (DateTimeField)

3. **Testimonial** *(Original Custom Model)*  
   - `author` (ForeignKey → User, nullable)  
   - `content` (TextField)  
   - `rating` (IntegerField, optional)  
   - `approved` (BooleanField)  
   - `created_on` (DateTimeField)

---

## Technologies Used

1. **Front-End**  
   - [HTML5](https://developer.mozilla.org/en-US/docs/Web/HTML)  
   - [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS)  
   - [Bootstrap 5](https://getbootstrap.com/)

2. **Back-End**  
   - [Python 3](https://www.python.org/)  
   - [Django 4+/5+](https://www.djangoproject.com/)  
   - [PostgreSQL](https://www.postgresql.org/) (Production DB)  
   - [Cloudinary](https://cloudinary.com/) (For image hosting)

3. **Authentication**  
   - [Django Allauth](https://django-allauth.readthedocs.io/) for user registration/login.

4. **Deployment Tools**  
   - Hosting platform (e.g., Heroku)  
   - [Gunicorn](https://gunicorn.org/) for production server.  
   - [Whitenoise](https://pypi.org/project/whitenoise/) for static files.

5. **Version Control**  
   - [Git](https://git-scm.com/) & [GitHub](https://github.com/) for source control.


## Testing

   **Manual Testing**
   - Responsiveness: Verified using Chrome DevTools for various screen sizes.
   - User Flows: Registered a new user, created test posts, left comments, edited, and deleted them.
   - Error Handling: Checked 404 pages, form validation, protected routes (only logged-in users can 
     submit posts/comments).

   **Code Validation**
   - HTML/CSS: Validated with W3C validators.
   - Python (PEP8): Utilized Flake8 or a similar linter for style checks



## Credits
   - Code Institute walkthroughs and documentation for foundational guidance.
   - Django Documentation for best practices on models, views, and deployment.
   - Bootstrap for quick, responsive UI development.
   - Cloudinary for image management.
   - YouTube channel Desphixs - https://www.youtube.com/watch?v=TIDldj2BDuY
   - ChatGpt
   **Acknowledgement**
   - Mentors & Peers for reviews and advice
   - Friends & Family for UI/UX testing and feedback
   - Student Support code institute.

## Bug
   - When attempting to delete a testimonial, a NameError is raised because message is undefined in testimonials/views.py. This issue occurs due to the incorrect use of message.success instead of messages.success in the testimonial_delete view.

   **Unresolved bug**
   - Some articles from 'I think therefore I blog' appeared on my site when I ran some migrations I believe. I just had to delete them.