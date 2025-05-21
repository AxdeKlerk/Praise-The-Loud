### 8. Debugging

Below are the various bugs that I encountered along the way and how I fixed them. In ever first instance, I would consult with chatGPT to see if it could help me fix the bug. As it is now becoming more common place to use ChatGPT for debugging in the industry, I decided that it would be good practice to use it as a tool to help me debug. For clarity and ease of use, I have broken the bugs down into the following categories:

- **Syntax Errors**
- **Logic Errors**
- **Runtime Errors**
- **Semantic Errors**
- **Design Errors**
- **Other Bugs**

#### 8.1 Syntax Errors

  - **Bug:** Incorrect spelling of module name. 
  
    The error occured when I was importing the first module in the project. The module name was misspelled in the import statement. What had happened was that I had pluralised the app name (gig_reviews) and then created the class  name (GigReview) using the singular form of the model name. This caused the error when trying to migrate the module to the database.
  
  - **Fix:** Corrected the spelling of the class module name in app.py, admin.py and urls.py to correspond with the app pluralisation and the class singular. 

  - **Lesson Learned:** It is important to be consistent with the naming conventions used in the project. 
  
    This will help to avoid errors such as this one in the future by creating different classes for the singular and plural forms of the model name. More importantly to make sure that I use different names for the app name and the class name to avoid confusion.

### 8.2 Logic Errors

- **Bug:** Sign-up, login and logout templates not loading on server.

  After checking my template structure multiplue times I could not understand why the templates were not loading. I had checked the urls.py file and the views.py file and they were both correct. I then realised that I had created the template and registration folders at the wrong level. This was a simple mistake but it took me a while to figure out.

- **Fix:** Moved template and registration folders to the root level of the project and left the signup html file in the app level templates folder.
- 
- **Lesson Learned:** Double check everything I do and make sure that I am using the correct logic and placement of my template folders.

- **Bug:** When I selected "Fan", "Artist", or "Venue" from the dropdown on my contact page, nothing happened. The correct form didn’t appear. I expected that choosing a contact type (e.g. "Fan") would show only the fan form and hide the other two, like it was doing earlier in testing.

  - **Fix:** The JavaScript function existed and didn’t crash, but it ran at the wrong time — before the dropdown element was ready. That meant the logic didn’t produce the expected result (the form showing), even though the code had no syntax errors. Thus, I wrapped it using DOMContentLoaded to ensure it ran only after the page was loaded.

  - **Lesson Learned:** I learned that it’s important to test my code thoroughly, even if it seems to work. I also learned that it’s important to understand the logic of my code and how it interacts with the DOM, and that JavaScript can’t find or interact with HTML elements unless the page is fully loaded first.

### 8.3 Runtime Errors

- **Bug:** Runtime error when trying to migrate the database.
  Django's migration history didn’t match the actual state of the database. It tried to create a table that already existed after I had added the fields 'location' and 'website' to the profile model and change the field's name from 'highlight' to 'title'. I got the following error message:
  psycopg2.errors.DuplicateTable: relation "gig_reviews_gigreview" already exists
  psycopg2.errors.UndefinedColumn: column "highlight" does not exist

- **Fix:** I used the following command to python manage.py migrate gig_reviews --fake 0001.
  This command faked the first migration where the table has all ready migrated and skipped the migration history. This allowed me to make the changes to the database and then run the migrations again. I had to repeat this process for the other two migrations (0002 for the change to the field 'highlight' to 'title'and 0003 for the addition of the 'location' and 'website' fields).

- **Lesson Learned:** Always check the migration history before making changes to the database.

- **Bug:** JS delete confirmation not triggering when clicking the "Delete Profile" button. The issue was created when I moved my static file location from my app to my global settings. However, there were no errors in the Django server output. So in order to diagnose why the JS was not working, I a console log to the top on my js file to say "script.js loaded!". As this was not appearing in the console in DevTools, I knew that the JS was not being loaded.
  
- **Fix:** I retraced my steps and found that I had not rerouted my script src in my base.html. I moved the static file location from 'my app/' and changed the path in the html file to the global location.
  
- **Lesson Learned:** Always check the console for errors and make sure that the JS is being loaded correctly before moving on with the project assuming that the error is not in the JS. I left the console.log at the top of my Js file as a reminder to check the console for errors at each step of the way.

### 8.4 Semantic Errors

- **Bug:** This bug continued throughout my project: spelling mistakes in the HTML, CSS, Js and Python code. I had to spend a lot of time debugging and fixing these errors.
  
- **Fix:** I used the following command to python manage.py check --deploy. This command checks for common errors in the project. It also checks for spelling mistakes in the HTML, CSS, Js and Python code.

- **Lesson Learned:** ALWAYS check the spelling of everything as you go along. This will save you a lot of time in the long run.

### 8.5 Design Errors

- **Bug:**
- **Fix:**
- **Lesson Learned:**

### 8.6 Other Bugs

- **Bug:**
- **Fix:**
- **Lesson Learned:**


![static file error message in console](image.png)