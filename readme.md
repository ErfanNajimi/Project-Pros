# <span class="logo-highlight">Pro</span>ject <span class="logo-highlight">Pro</span>

<img src="doc-assets/screenshots/image.png" width="100%" height="100%">

A full-stack project built using the Django framework with Python, JavaScript, HTML and CSS. The aim was to create a functional website for users to add deployed projects and github repos that serves as a source of inspiration and help to others, as well as a place where users can celebrate each others achievements.

# ABOUT

<img src="doc-assets/screenshots/image.png" width="100%" height="100%">

Project Pro is an app for users to celebrate each others' coding achievement, get inspiration from other developers, get tips from our tips section on problems they are currently facing in a project. 

# UX
--
We started with strategy, focusing on the features the target audience would enjoy and find useful.

The target audience for the Project Pro App is:

Professional developers, students

Anyone interested in adding their project on our app

Anyone looking to get tips from the app for a current project or find help for someone else

Anyone looking to have celebrate in a recent milestone they made

These users will be looking for:

A clear and informative website, with intuituve navigation and seeing what the website is at first glance.

A UI/UX that is minimalistic and emphasises the content and theme.

The ability to make a user account in order to add a project.

The ability to log out and login when needed. 

Given the desire to appeal to as broad an audience as possible, UX/UI philosophy will be simple with a focus on content and painless navigation.

# USER STORIES
As a user is the purpose of the app clear at a glance.

As a user can I successfully login/create an account to use the app.

As a user am I notified when I log in and logout.

As a user am I notified when I successfully add a new project on the dashboard.

As a user am I notified when other users like my project.
As a user can I successfully add the github link to my project and the deployed version of my project.

As a user am I directed to another page when I click on the social media links.

As a user can I easily navigate the website through the navbar.

As a user can I easily see other people's projects once i'm logged in.

As a user am I privy to the top tips provided on the website.


# WIREFRAMES
All wireframes were created using Balsamiq.

<img src="doc-assets/screenshots/balsamiq image.png" width="100%" height="100%">

# FEATURES

# Home Page
# Navigation bar: 

<img src="doc-assets/screenshots/navbar image.png" width="100%" height="100%">

The navigation bar appears on every page allowing users to easily navigate through the site.
Navigation bar has links for 'Home', 'Logout' and 'Login/Register'.
Logged in users will also have a 'Logout' and 'home' button highlighted in the navbar.
The navbar is responsive, collapsing into a toggle menu for medium and small screen size.

# Login Page: 

<img src="doc-assets/screenshots/signin page.png" width="100%" height="100%">

The login page takes users to a new page where they can login to their account to add or update existing todo items, or if they have not registered find a link to register before logging in.

# Logout Page

<img src="doc-assets/screenshots/signout page.png" width="100%" height="100%">

This page confirms if the user wants to logout of their account which covers any instance where the user made a mistake in clicking the signout button. 

# FOOTER

<img src="doc-assets/screenshots/footerimage.png" width="100%" height="100%">

The footer page shows the social media icons where users can click and redirects them to a different page.

# Project Page

<img src="doc-assets/screenshots/project page.png" width="100%" height="100%">

The project page has features such as title to add the name of the project, spaces to add the deployed link and github repo, checklist to add favourite, emoji for users to show some love for the project.

# Structure
This website is made of two apps: The Project App which handles the functions linked to adding the project, and another app for the tips.


# Database Schema

<img src="doc-assets/screenshots/erd image.png" width="100%" height="100%">

# Technology Stack

HTML - For page structure

CSS - For custom styling

Python - for the backend

Javascript - for event listeners on buttons

Django - framework used to build this project

Bootstrap 5 - front end framework used for styling

Heroku PostgreSQL - used as the database

Balsamiq - for wireframes

Font Awesome - for social media icons

Lucidchart - for database ER diagrams

Google Fonts- for custom font styling

GitHub - for storing the code and for the Kanban board

Heroku - for hosting and deployement of this project

Git - for version control

# Testing and Validation

# Responsiveness
We used the dev tools on chrome to test the website for responsiveness. We captured screenshots to demonstrate responsive design across mobile, tablet and laptop using UI Dev. On smaller screens the screen collapses to show a toggle bar for the nav links.

<img src="doc-assets/screenshots/image.png" width="100%" height="100%">

# Testing and Validation
We used the W3 HTML Validator  to check the HTML on each of my site pages by Direct Input. However, the only error pointed out was the django language used.

We used the W3 CSS Validator to check my CSS script by Direct Input. We found no errors!.

# Manual Testing Results
We were not able to do any manual testing due to time constraints.




# Deployment
Deployment Guide for Project Pro's Todo App

Deployment Steps:

Creating the Heroku App

Begin by signing up or logging in to Heroku.

In the Heroku Dashboard, click on 'New' and then select 'Create New App'.

Choose a unique name for your project, like "Travelling Scribbles".

Select the EU region.

Click on "Create App".

In the "Deploy" tab, choose GitHub as the deployment method.

Connect your GitHub account and find/connect your GitHub repository.

# Setting Up Environment Variables

Create env.py in the top level of the Django app.

Import os in env.py.

Set up necessary environment variables in env.py, including the secret key and database URL.

Update settings.py to use environment variables for secret key and database.

Configure environment variables in the Heroku "Settings" tab under "Config Vars".

Migrate the models to the new database connection in the terminal.

Configure static files and templates directories in settings.py.

Add Heroku to the ALLOWED_HOSTS list.

# Creating Procfile and Pushing Changes
Create a Procfile in the top level directory.

Add the command to run the project in the Procfile.

Add, commit, and push the changes to GitHub.

# Heroku Deployment
In Heroku, navigate to the Deployment tab and deploy the branch manually.

Monitor the build logs for any errors.

Upon successful deployment, Heroku will display a link to the live site.

Make sure to resolve any deployment errors by adjusting the code as necessary.


# Credits and Acknowledgement

Code Institute Walkthrough Project

Code recycling from individual full stack project.

Team mates for always volunteering to pick up any tasks to get this done.