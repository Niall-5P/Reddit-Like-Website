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
   ![Home Page Wireframe](static/images/HomePage.png)

2. **Testimonial Page**
   ![Testimonial Wireframe](static/images/TestimonialPage.png)

3. **Register account page**
   ![Register account](static/images/RegisterAccountPage.png)

4. **Login page**
   ![Login page](static/images/LoginPage.png)

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


| **Test Scenario**        | **Steps**                                                                                                                                               | **Expected Result**                                                                                   | **Actual Result**                                                      | **Pass/Fail** |
|--------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|--------------|
| **Register & Login**     | 1. Go to `/register` → enter valid details → submit.<br>2. Navigate to `/login` → enter correct username/password → submit.                             | User can register, then log in with valid credentials.                                                | Form submission succeeded; user authenticated as expected.             | Pass         |
| **Create Post (Django)** | 1. While logged in, visit `/add-post`.<br>2. Enter a title and content → submit.                                                                     | Post is saved to the database; appears on the homepage or post detail page.                            | Successfully created a new post; verified in DB and on the homepage.   | Pass         |
| **Add Comment (Django)** | 1. Open a post detail page.<br>2. Enter a comment in the text area → submit.                                                                             | Comment is saved to the database; displayed if auto-approved or after admin approval.                  | Comment stored properly; appears under the post.                       | Pass         |
| **Add Testimonial**      | 1. While logged in, visit `/add-testimonial`.<br>2. Enter testimonial content (and optional rating) → submit.                                        | Testimonial is saved to the database; success message shown; may remain pending for admin approval.    | Testimonial created as expected; appears in admin for approval.        | Pass         |
| **Responsive Layout**    | 1. Resize browser (mobile, tablet, desktop).<br>2. Check that navigation, text, and images adjust properly at different viewports.                       | The site remains legible; navbar and content adapt fluidly to screen size.                             | Layout remains consistent; no overlapping or cutoff elements.          | Pass         |
| **Error Handling**       | 1. Submit form(s) with empty or invalid fields (e.g., no `content`).<br>2. Attempt to access protected pages (e.g., add testimonial) when logged out.     | Relevant error messages appear; restricted pages redirect to login if user is not authenticated.       | Forms display validation errors as expected; unauthorized users redirected. | Pass         |



**Testimonial View Tests Overview**

- **Anonymous User**  
  Verifies that a user who is not logged in cannot access the testimonial creation page. The test expects either a redirect to the login page (`302` status) or a `403 Forbidden` response.

- **Logged-In User**  
  Confirms that a signed-in user can successfully post a new testimonial. After submitting valid data, the response should be a redirect (`302`) back to the testimonial list page, along with a success message indicating that the testimonial was created.

By testing these scenarios, we ensure that:
1. **Access Control**: Only authenticated users can create testimonials.
2. **Form Submission**: Testimonial data is correctly handled and saved to the database, and the user is appropriately redirected afterward.



### JavaScript Client-Side Testing

A simple **QUnit** test was implemented to validate a rating input on the client side. The test checks:

1. **Valid Rating**  
   Ensures that calling `validateRating(3)` returns `true`, confirming that 3 is accepted as a valid rating.

2. **Rating Below 1**  
   Calls `validateRating(0)` and expects `false`, ensuring ratings lower than 1 are rejected.

3. **Rating Above 5**  
   Calls `validateRating(6)` and expects `false`, verifying ratings higher than 5 are rejected.

All tests passed, confirming the function correctly enforces the **1–5 rating** constraint on the client side. The test file is accessed by simply opening the `.html` test file in a browser, which runs QUnit and displays the results.





## Manual Testing (Expanded)

Below is a more detailed breakdown of how the site was manually tested to ensure **functionality**, **usability**, and **responsiveness** across various user flows. All testing was performed locally in a development environment (VS Code + Django server) and partially on the deployed Heroku site.  

### Testing Environment

- **Browsers**: Chrome (desktop, mobile view), Firefox  
- **Devices/Screen Sizes**: Desktop (1920×1080), iPad simulation (~768×1024), mobile simulation (~375×667) using Chrome DevTools  
- **User States**: Logged out (anonymous), Logged in (regular user), Admin user  

### Manual Test Cases & Scenarios

1. **User Registration & Login**  
   - **Scenario**: A new user visits `/register`, fills in username/email/password, and submits. They are then directed to `/login`, where valid credentials are entered.  
   - **Acceptance Criteria**:  
     - User can successfully register and see a confirmation message.  
     - Logging in redirects to the homepage with a welcome message.  
   - **Outcome**:  
     - Registration displayed appropriate form errors if fields were left blank.  
     - Valid sign-up and subsequent login were successful.  
   - **Status**: **Pass**  

2. **Post Creation (Admin-Only)**  
   - **Scenario**: An admin user navigates to `/add-post` (or “Create Post” link) and fills out the title and content form fields.  
   - **Acceptance Criteria**:  
     - Only an admin user can see and access the “Add Post” feature.  
     - Submitting valid data creates a new post displayed on the homepage or post list.  
   - **Outcome**:  
     - Non-admin (regular) user was redirected or received a 403/302 response when attempting the URL.  
     - Admin successfully created a new post that immediately appeared on the homepage.  
   - **Status**: **Pass**  

3. **Commenting on Posts**  
   - **Scenario**: A logged-in user navigates to a specific post’s detail page, enters a comment, and submits.  
   - **Acceptance Criteria**:  
     - Comment is saved to the database.  
     - If auto-approved, it appears immediately; otherwise awaits admin approval.  
   - **Outcome**:  
     - Comment posted successfully under the post.  
     - Invalid or blank comments triggered a form validation error.  
   - **Status**: **Pass**  

4. **Editing & Deleting Comments**  
   - **Scenario**: A user who created a comment returns to the post detail page, clicks “edit” or “delete” on their own comment.  
   - **Acceptance Criteria**:  
     - Only the comment’s author sees edit/delete options.  
     - Edits or deletions are reflected immediately after submission.  
   - **Outcome**:  
     - Regular user could not edit another user’s comments.  
     - Deletions and edits worked as expected with success messages.  
   - **Status**: **Pass**  

5. **Adding Testimonials**  
   - **Scenario**: A logged-in user navigates to `/add-testimonial`, enters testimonial text and (optionally) a rating (1–5), then submits.  
   - **Acceptance Criteria**:  
     - Testimonial is saved to DB with `approved=False` by default (or until admin approval).  
     - A success message is shown, redirecting the user appropriately.  
   - **Outcome**:  
     - Anonymous user was blocked from creating testimonials (redirected to login).  
     - Logged-in user submitted a testimonial successfully, appearing on the admin page to be approved.  
   - **Status**: **Pass**  

6. **Responsiveness & Layout**  
   - **Scenario**: The tester resizes the browser to various breakpoints and also checks on mobile simulation.  
   - **Acceptance Criteria**:  
     - The navigation bar collapses or toggles on smaller screens.  
     - Page content reflows without overlapping or cutoff text.  
   - **Outcome**:  
     - No significant layout issues were observed.  
     - All buttons and text remain legible on mobile screens.  
   - **Status**: **Pass**  

7. **Error Handling**  
   - **Scenario**: Submit forms with invalid data (empty fields, missing required info), and attempt to access pages that require login.  
   - **Acceptance Criteria**:  
     - Proper error messages appear (e.g., “This field is required.”).  
     - Anonymous users are redirected to login if they attempt to create posts, comments, or testimonials.  
   - **Outcome**:  
     - Validation messages worked correctly.  
     - Non-logged-in attempts triggered a login redirect.  
   - **Status**: **Pass**  

8. **404 & Miscellaneous Checks**  
   - **Scenario**: Navigate to non-existent URLs (e.g., `/random-page`), or remove slug portion from a post URL.  
   - **Acceptance Criteria**:  
     - A custom 404 page or default Django 404 is displayed.  
     - The site does not crash.  
   - **Outcome**:  
     - 404 displayed as expected; site remained stable.  
   - **Status**: **Pass**  

### Conclusions & Observations

- **All Core Flows** (registration, login, post creation by admin, commenting, testimonials) functioned correctly.  
- **Responsiveness** was consistent across tested devices and screen sizes.  
- **Permission Checks**: Non-admin or logged-out users could not access restricted pages (e.g., create post, create testimonial).  
- **Error Handling**: Form and page-level errors guided the user appropriately, avoiding confusion.  

Overall, these **manual tests** confirm the application meets its **intended user stories** and **site goals**, providing a stable and user-friendly Reddit-like experience.

   **Code Validation**
   - HTML/CSS: Validated with W3C validators.
   - Python (PEP8): Utilized Flake8 or a similar linter for style checks



### Deployment Summary (Heroku)

1. **Create a Heroku App**  
   - Log in to your Heroku account and click **New → Create new app**.  
   - Choose an app name (unique across Heroku) and region.
   - Click add buildpack (determine which buildpack you will need (python etc))

2. **Set Up Environment Variables**  
   - In the Heroku dashboard, go to **Settings → Reveal Config Vars**.  
   - Add keys like `SECRET_KEY` and `DATABASE_URL` (if using Postgres).  
   - This prevents storing sensitive info in your codebase.

3. **Install Required Packages**  
   - In your Django project’s `requirements.txt`, ensure you have:
     - `gunicorn` (production web server)
     - `dj-database-url` (if using Postgres)
     - `whitenoise` (for static files)
   - Commit and push these changes to GitHub.

4. **Procfile**  
   - In your project root, create a file named **Procfile** (no extension) containing:
     ```bash
     web: gunicorn your_project_name.wsgi
     ```
   - This tells Heroku how to run your Django app.

5. **Connect GitHub to Heroku**  
   - Under your Heroku app’s **Deploy** tab, choose **GitHub** as the deployment method.  
   - Find your repo and connect it.  
   - Optionally, enable automatic deploys so each push to `main` triggers a new build.

6. **Static Files Setup**  
   - Add `whitenoise.middleware.WhiteNoiseMiddleware` to `MIDDLEWARE` in `settings.py`.  
   - Set `STATIC_ROOT` in your Django settings (already done if following best practices).  
   - Run `collectstatic` automatically when Heroku builds by ensuring it’s set as a release step or in the default Django build process.

7. **Deploy**  
   - Click **Deploy Branch** (if manual) or push your code to GitHub (if auto-deploy).  
   - Heroku will install dependencies, run collectstatic, and launch your app using `gunicorn`.

8. **Verify**  
   - Once the build completes, open your app’s URL on Heroku.  
   - Confirm your site is reachable, static files load, and all env variables (like `SECRET_KEY`) are working properly.

By following these steps, your Django application is hosted on **Heroku** with secure environment variables, properly managed static files, and a robust production server (`gunicorn`).




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