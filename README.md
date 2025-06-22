# Praise-The-Loud

[insert responsive images] 

## 1. Introduction

## 2. Aim and Purpose

## 3. Target Audience

## 4. User Stories

## 5. Goals

## 6. Planning and Development

### 6.1 ERD (Entity Relationship Diagram)
The ERD was designed using [draw.io](https://app.diagrams.net/) to show the relationship between the different entities in the database.

![image](https://github.com/user-attachments/assets/1af79206-59d2-4762-8de9-dcd21d638399)

### 6.2 Wireframes
The wireframes were drawn using Balsamic. Both the larger screen and the mobile version were created at the same time. This allowed for a greater design initiative which took into account the overall layout of the website and how I wanted it to look on both screens. The wireframes were used throughout the design of the website and went through various iterations until I was happy with the final product.
 
![image](https://github.com/user-attachments/assets/21eeea6a-e21f-4bbb-a1ca-bf72876d2029)

### 6.3 Colour Palette
The colour palette chosen is the typical colour scheme of the rock and metal scene: red, white and black. However, I change the 'white' for a softer shade of light grey (#F5F5F5) so that it wasn’t so stark on the eyes and doesn't cause blurring and bleeding into the black or red. The red (#F50000) was chosen to reduce the brightness of the red and a dark grey (#5C5C5C) was chosen for the navigation bar so that it had prominance on the black background. 

The colours chosen from using this pallet [coolors.co](https://coolors.co/)

### 6.4 Typography

## 7. Features

### 7.1 The Home Page

### 7.2 The About Page

### 7.3 The Register and Login Page

### 7.4 The Profile Page

### 7.5 The Gig Review Page

### 7.6 The Gig Review Form

### 7.7 The Footer

#### 7.7.1 The Contact Modal

## 8. Debugging

## 9. Testing

## 10. Deployment

This section outlines the full process for deploying this project from GitHub to your local machine using VS Code, and then hosting it live on Heroku.

### 10.1 Create a GitHub Repository
- Go to *GitHub* and click the "+" icon to create a new repository
- Name the repository and optionally add a description
- Choose "Public" or "Private"
- Do not initialize with a README, .gitignore, or license
- Click "Create repository"

### 10.2 Clone the Repository to VS Code
- Open *VS Code* and its terminal
- Navigate to the folder where you want your project
- Copy the repository's URL from *GitHub* and use the "Clone Git Repository" option in *VS Code*
- Open the project folder in *VS Code*
- 
### 10.3 Create and Activate a Virtual Environment
- In your terminal, create a virtual environment inside your project folder
- Activate the environment depending on your system (*Windows*, *Mac*, or *Linux*)
- Your terminal prompt will change to show the environment is active

### 10.4 Install Project Dependencies
- Use the requirements.txt file to install all necessary *Python* packages
- If this file doesn’t exist yet, install your packages manually and then generate the file

### 10.5 Prepare the Project for Heroku
- Create a "Procfile" at the root of your project with the necessary *Heroku* command to run the app
- Ensure "gunicorn", "dj-database-url", and "psycopg2-binary" are installed
- Update your "requirements.txt" file with any new packages
- Commit all changes to *Git*

### 10.6 Set Up a Heroku Account and CLI
- Create an account at *Heroku.com*
- Download and install the *Heroku* CLI for your operating system
- Use the CLI to log into your *Heroku* account

### 10.7 Create a Heroku App
- Use the *Heroku* CLI to create a new app with a unique name
- *Heroku* will generate a remote *Git* URL for your project

### 10.8 Push Your Project to Heroku
- Add *Heroku* as a *Git* remote if it wasn’t automatically added
- Push your local codebase to *Heroku*’s remote repository

### 10.9 Configure Environment Variables on Heroku
- Go to your *Heroku* Dashboard and open your app
- Under "Settings", click "Reveal Config Vars"
- Add the following variables:
    - "DEBUG" = "False"
    - "SECRET_KEY" = your *Django* secret key
    - "ALLOWED_HOSTS" = your *Heroku* app's URL
    - Add any additional variables like database URLs, *Cloudinary* settings, or email credentials as needed

### 10.10 Final Project Setup on Heroku
- Run your database migrations from the *Heroku* CLI
- Create a "superuser" account to access the *Django* admin panel
- "Collectstatic" files if not done automatically

### 10.11 Open Your Live Site
- Use the *Heroku* CLI or browser to open your app
- Your project is now live and hosted at "your-app-name.herokuapp.com"

## 11. Furute Development

## 12. Credits

The following resources were used to help with the development of the website:
- [Adobe Express](https://new.express.adobe.com/?xProduct=&xProductLocation=&locale=en-US) for the logo creation
- [Balsamic](https://balsamiq.com/) for the wireframes
- [BootStrap](https://simple.wikipedia.org/wiki/Bootstrap_(front-end_framework)) - used for the layout and styling of the website
- [Bootstrap Docs](https://getbootstrap.com/) for reference to all Bootstrap syntax
- [Chat-GPT](https://chatgpt.com/) - An AI tool used for understanding where things went wrong, how to fix code and generally used for deeper understanding of software development and the principles and languages used for coding
- [coolors.co](https://coolors.co/) for the colour palette
- [CSS](https://en.wikipedia.org/wiki/CSS) - used for main content styling
- [Django](https://simple.wikipedia.org/wiki/Django_(web_framework)) - used for the backend of the website
- [draw.io](https://app.diagrams.net/) for the ERD
- [Google Fonts]() - for typology
- [Google Images]() - for the band and venue logos
- [HTML](https://en.wikipedia.org/wiki/HTML) - used to build main site content
- [JavaScript](https://simple.wikipedia.org/wiki/JavaScript) - used for all interactivity within the website
- [JSHint]() for Javascript validation
- [Lighthouse]() - for the performance and accessibility testing
- [MSWord]() - used for grammar and spelling checking
- [Perplexity]() - An AI tool used for general queries and learning
- [Python](https://simple.wikipedia.org/wiki/Python_(programming_language)) - used for the backend of the website
- [Slack Edit]() - for markdown references
- [Slack Overflow]() - for general queries
- [W3schools](https://www.w3schools.com/) a constant source of reference for all html, CSS, JavaScript, BootStrap and Django explanations
- [W3C Markup Validation Service](https://validator.w3.org/) for the html validation
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) for the CSS validation

## 13. Acknowledgements

This project could not have been possible without the support of the following people:

Julia Brown - my loving partner who took over the reins at home and kept me fed and watered throughout,

Julie, Paul, Paul B., Dave, Steph, Thambiso, Matthew & Elaine - thank you for your, sometimes brutal, honesty although it was frustrating at times it most definitely gave me the drive to push harder,

Richard Wells - Code Institute Mentor - who helped guide me through the process from start to finish,

My team mates on my course - Steve Powell, Robert Lewis and Jordan Acomba who provided continued support and motivation in our weekly study group, every Sunday evening, which gave us time to discuss different aspects of our projects as we went along, 

Code Institute for all the course materials and allowing my the opportunity to do this course, and by no means least

Barry (my dog) for reminding me that you can't be susuccessful at work without play times.

![Red rock horns image](praise_the_loud/Images/red-horns.png)
 
     Stay Loud