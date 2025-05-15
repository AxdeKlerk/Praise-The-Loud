### 8. Debugging

Below are the various bugs that I encountered along the way and how I fixed them. In ever first instance, I would consult with chatGPT to see if it could help me fix the bug. As it is now becoming more common place to use ChatGPT for debugging in the industry, I decided that it would be good practice to use it as a tool to help me debug. For clarity and ease of use, I have broken the bugs down into the following categories:

- **Syntax Errors**
- **Logic Errors**
- **Runtime Errors**
- **Semantic Errors**
- **Design Errors**
- **Other Bugs**

#### 8.1 Syntax Errors

  - **Bug:** SyntaxError: incorrect spelling of module name. 
  
    The error occured when I was importing the first module in the project. The module name was misspelled in the import statement. What had happened was that I had pluralised the app name (gig_reviews) and then created the class  name (GigReview) using the singular form of the model name. This caused the error when trying to migrate the module to the database.
  
  - **Fix:** Corrected the spelling of the class module name in app.py, admin.py and urls.py to correspond with the app pluralisation and the class singular. 

  - **Lesson Learned:** It is important to be consistent with the naming conventions used in the project. 
  
    This will help to avoid errors such as this one in the future by creating different classes for the singular and plural forms of the model name. More importantly to make sure that I use different names for the app name and the class name to avoid confusion.

