
### 8. Debugging

Below are the various bugs that I encountered along the way and how I fixed them. In ever first instance, I would consult with *ChatGPT* to see if it could help me fix the bug. As it is now becoming more common place to use AI for coding in the industry, I decided that it would be good practice to use it as a tool to help me debug. One thing I did not do was to dump huge copies of code into *ChatGPT*, but rather asked it questions like *what does this mean?* and *why does this do this?* to enhance my understanding. Fair to say that I used *ChatGPT* as a tutor/study buddy.

For clarity and ease of use, I have broken the bugs down into the following categories:


-  **8.1 Syntax Errors**

-  **8.2 Logic Errors**

-  **8.3 Runtime Errors**

-  **8.4 Semantic Errors**

-  **8.5 Design Errors**

-  **8.6 Validation Errors**

-  **8.7 Other Bugs**

-  **8.8 Bugs Unresolved**

  ### 8.1 Syntax Errors

  -  **Bug:** Incorrect spelling of module name error occured when I was importing the first module in the project. The module name was misspelled in the import statement. What had happened was that I had pluralised the app name (gig_reviews) and then created the class name (GigReview) using the singular form of the model name. This caused the error when trying to *migrate* the module to the database.

-  **Fix:** Corrected the spelling of the class module name in app.py, admin.py and urls.py to correspond with the app pluralisation and the class singular.

-  **Lesson Learned:** It is important to be consistent with the naming conventions used in the project.

-  **Bug:** While integrating Cloudinary into my *Django* project, I encountered a TypeError when using os.environ.setdefault() in my env.py file. I had mistakenly passed only one argument instead of the required key-value pair. After correcting that, a second issue appeared — an IndentationError in settings.py. I had written an if statement to check for the presence of env.py but forgot to indent the import env line beneath it, which prevented the project from running.

-  **Fix:** I resolved the TypeError by replacing setdefault() with a direct environment variable assignment. I then resolved the IndentationError by indenting the import env line so it sat within the if block.

-  **Lesson Learned:** Syntax errors like these can completely stop *Django* from running, even if the actual mistake is minor. I was reminded to pay close attention to indentation, especially in conditional blocks, and to always check that function calls are written with the correct number of arguments. Stepping through each issue methodically helped isolate and fix the problems without getting overwhelmed by the complexity of the project.

-  **Bug:** After deploying my project and trying to test the search functionality, I kept getting a *500 internal server error*. The search page had previously worked fine, so this was unexpected. The *Heroku* logs showed:

	*TemplateSyntaxError: Invalid filter: cloudinary* which pointed to the line trying to render the image for an artist logo using a Cloudinary transformation filter.

-  **Fix:** I checked the Cloudinary documentation and found that the filter syntax was incorrect because it does not exist in the **django*-cloudinary-storage* package. It turns that the correct way to access *Cloudinary* image URLs from a *CloudinaryField* is simply:

		*<img  src="{{ item.logo.url }}"...>*

	I updated the filter to use the new syntax and the error was resolved.

-  **Lesson Learned:** The *CloudinaryField* in *Django* already provides a direct .url property, and there’s no need to apply a special filter or load a custom tag unless using a different *Cloudinary* library. I’ll stick with .url going forward and avoid introducing template filters that don’t exist.

### 8.2 Logic Errors

-  **Bug:** Sign-up, login and logout templates not loading on server. After checking my template structure multiplue times I could not understand why the templates were not loading. I had checked the urls.py file and the views.py file and they were both correct. I then realised that I had created the template and registration folders at the wrong level. This was a simple mistake but it took me a while to figure out.

-  **Fix:** Moved template and registration folders to the root level of the project and left the signup *html* file in the app level templates folder.

-  **Lesson Learned:** Double check everything I do and make sure that I am using the correct logic and placement of my template folders.

  -  **Bug:** When I selected "Fan", "Artist", or "Venue" from the dropdown on my contact page, nothing happened. The correct form didn’t appear. I expected that choosing a contact type (e.g. "Fan") would show only the fan form and hide the other two, like it was doing earlier in testing.

-  **Fix:** The *JavaScript* function existed and didn’t crash, but it ran at the wrong time — before the dropdown element was ready. That meant the logic didn’t produce the expected result (the form showing), even though the code had no syntax errors. Thus, I wrapped it using DOMContentLoaded to ensure it ran only after the page was loaded.

  -  **Lesson Learned:** I learned that it’s important to test my code thoroughly, even if it seems to work. I also learned that it’s important to understand the logic of my code and how it interacts with the DOM, and that *JavaScript* can’t find or interact with *HTML* elements unless the page is fully loaded first.

  -  **Bug:** The delete confirmation popup stopped appearing when I clicked the “Delete Profile” button. This happened after I moved my static files to a global directory. There were no errors in the **Django* server output, so I initially assumed the problem was with the *JavaScript* logic itself.


-  **Fix:** I reviewed my base.*html* template and found that I hadn’t updated the path to the *JS* file after moving it. I had been using a hardcoded path like */static/js/script.js*, but *Django* wasn’t recognizing it. I replaced it with the correct *{% static %}* tag:

		<script  src="{% static 'js/script.js' %}"></script>

-  **Lesson Learned:** If *JavaScript* code isn’t running, always verify whether the script is actually being loaded by checking the console. A console.log() at the top of the file is a quick way to test this. Also, whenever static file paths are changed or files are moved, it's important to update all related template references using *{% static %}* rather than hardcoded paths, especially when working within *Django*.

### 8.3 Runtime Errors

  -  **Bug:** 	**Django**'s migration history didn’t match the actual state of the database. It tried to create a table that already existed after I had added the fields 'location' and 'website' to the profile model and change the field's name from 'highlight' to 'title'. I got the following error message:

	  		psycopg2.errors.DuplicateTable: relation "gig_reviews_gigreview" already exists
			psycopg2.errors.UndefinedColumn: column "highlight" does not exist

-  **Fix:** I used the following command to *python manage.py *migrate* gig_reviews --fake 0001*. This command faked the first migration where the table has all ready migrated and skipped the migration history. This allowed me to make the changes to the database and then run the migrations again. I had to repeat this process for the other two migrations (0002 for the change to the field 'highlight' to 'title' and 0003 for the addition of the 'location' and 'website' fields).

  -  **Lesson Learned:** Always check the migration history before making changes to the database.

-  **Bug:** *JS* delete confirmation not triggering when clicking the "Delete Profile" button. The issue was created when I moved my static file location from my app to my global settings. However, there were no errors in the *Django* server output. So in order to diagnose why the *JS* was not working, I wrote a *console log* statement to the top on my *JS* file to say "script.js loaded!". As this was not appearing in the console in *DevTools*, I knew that the *JS* was not being loaded.

-  **Fix:** I retraced my steps and found that I had not rerouted my script src in my base.*html*. I moved the static file location from 'my app/' and changed the path in the *html* file to the global location.

-  **Lesson Learned:** Always check the console for errors and make sure that the *JS* is being loaded correctly before moving on with the project assuming that the error is not in the *JS*. I left the console.log at the top of my *Js* file as a reminder to check the console for errors at each step of the way.

-  **Bug:** After moving my static files (*CSS* and *JavaScript*) from an app-level directory to a global static/ folder, the browser console reported MIME *ype errors* and *404 responses* for both *style.*css** and *script.js*. Despite the files existing in the correct location, *Django* was returning *HTML* instead of the expected static file content. There were no errors in the *Django* server log, which made the issue harder to diagnose. The *CSS* and *JS* files were not being applied or executed at all.

-  **Fix:** I first confirmed that my file structure and template paths were correct using *{% static %}*. Then I ran *python manage.py findstatic *css*/style.*css**, which confirmed *Django* could locate the file. This pointed to the fact that *Django* simply wasn’t serving the static files during development. To fix this, I updated urls.py to explicitly serve static files by adding the following block at the bottom of the file:

		from *django*.conf import settings
		from *django*.conf.urls.static import static
		if settings.DEBUG:
		urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])

-  **Lesson Learned:** Always check the console for errors and make sure that the *JS* is being loaded correctly before moving on with the project assuming that the error is not in the *JS*. I left the console.log at the top of my *Js* file as a reminder to check the console for errors at each step of the way.

	Even when static files exist and are referenced correctly in templates, *Django* won’t serve them during development unless explicitly told to. It’s important to use *findstatic* to confirm the path and then make sure the urls.py is properly configured. MIME errors in the browser usually indicate that something is being returned with the wrong content type — often a *404 *HTML** page — so checking the browser’s *DevTools* network tab is an essential part of debugging static file issues.

  -  **Bug:** I had written the SearchForm class in forms.py but mistakenly tried to import it from models.py and got an *ImportError* caused by trying to import SearchForm from the wrong file.

			ImportError: cannot import name 'SearchForm' from 'gig_reviews.models' 
			(C:\Users\axdek\Documents\vscode-projects\Project 3\Praise-The-Loud\gig_reviews\models.py)

  -  **Fix:** I fixed the bug by importing the SearchForm class from forms.py instead of models.py by updating the import statement in views.py.

-  **Lesson Learnes:** Always import classes from the correct file. This was a simple mistake but it took me a while to figure out what was causing the error, but I used the trace back to identify the issue.

-  **Bug:** **Django** threw a *TemplateDoesNotExist* error when loading the search results page. I had already created the search_results template in the templates folder, but I had not routed it in the views correctly.

-  **Fix:** I fixed the render call in the view to point th the correct folder.

-  **Leason Learned:** Always check the render call in the view to make sure that the template is being rendered correctly, like this:

	   return render(request, *gig_reviews/search_results.*html**, {'form': form, 'results': results})

-  **Bug:** After deploying to *Heroku*, I got an *“Internal Server Error”* when trying to load the site. The *Heroku* logs showed:

		*django*.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

	-**Fix:** I realized that *Heroku* didn’t have my *SECRET_KEY* set as a config variable. To fix this, I ran the following command in the terminal: *'heroku config:set SECRET_KEY=mysecretkey*. This sets the *SECRET_KEY* environment variable in *Heroku*. After restarting the app, the error was fixed.

 -  **Lesson Learned:**  *Django* will crash if *SECRET_KEY* is missing or empty in production, and *Heroku* doesn’t use my local *env.py*. Any environment variables I rely on locally must also be set explicitly in *Heroku* using *heroku config:set*. I’ll now make sure all production secrets are safely configured in the *Heroku* environment, not hardcoded in my files.

-  **Bug:** When I set up my *custom 404 error handler*, everything seemed fine with *DEBUG = True*. But after switching *DEBUG = False* to test the actual *404 page*, *Django* crashed with a *500 Internal Server Error*. The console showed:

		  The custom handler404 view '404.*html*' could not be imported.
			HINT: No module named '404
	
	Even after correcting the handler path to point to the correct view function, I still got a *500 error* when visiting a broken URL like */seach/*. No helpful error message was shown because *DEBUG = False*.

-  **Fix:** The root cause was that I wrote this in my view: *

		return render(request, '404.*html*', status=404)*. 
	
	But my actual template was stored inside: *
	
		gig_reviews/templates/gig_reviews/404.*html**

	Because of that, *Django* couldn’t find the file — it was silently failing during template rendering, leading to a *500 error*.

	To fix it, I changed the view to: *return render(request, 'gig_reviews/404.*html*', status=404)* This matches the real location of the template, and then everything worked correctly. When I visit a broken URL with *DEBUG = False*, I see my custom *404 page* instead of *Django*'s default error screen or a *500*.

-  **Lesson Learned:** When using *render()* with templates, the path is always relative to the top of the template search path (i.e. what’s defined in *TEMPLATES['DIRS']*). If the file is inside an app's *templates/app_name/* folder, I need to include the app name in the path string unless the app’s template folder is directly in the global templates directory. Always double-check the template path when using *DEBUG = False*, because *Django* won't show helpful messages for template errors in production mode.

### 8.4 Semantic Errors

-  **Bug:** This bug continued throughout my project: spelling mistakes in the *HTML*, *CSS*, *Js* and *Python* code. I had to spend a lot of time debugging and fixing these errors.

-  **Fix:** I used the following command to *python manage.py check --deploy*. This command checks for common errors in the project. It also checks for spelling mistakes in the *HTML*, *CSS*, *Js* and *Python* code.

  -  **Lesson Learned:** ALWAYS check the spelling of everything as you go along. This will save you a lot of time in the long run.

  -  **Bug:** After deploying to *Heroku*, the contact form did not appear when selecting "Fan", "Artist", or "Venue". The modal buttons were unresponsive, even though everything worked correctly in local development.

  -  **Fix:** I Opened *Chrome* DevTools* and saw multiple MIME type and 404 errors in the console. *Heroku* was serving the *JavaScript* and *CSS* files as *HTML* instead of the correct MIME types because *collectstatic* was not running, and *WhiteNoise* was not configured to serve static files. These were the steps taken to fix the issue at the bottom of the settings.py file:

	  	Added *STATIC_ROOT = BASE_DIR / "staticfiles"*
		Installed *whitenoise* in *MIDDLEWARE*
		Set *STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"*
		Removed *DISABLE_COLLECTSTATIC = 1* from *Heroku*
		Committed all changes and deployed successfully after verifying *collectstatic* ran

  -  **Lesson Learned:** *Heruko* does not serve static files out of the box. I need to set the *STATIC_ROOT* correctly, use *whitenoise* to handle the static assets in production, and confirm that *{% static %}* is linked in my *CSS* and *JavaScript* files. Using *DevTools* to inspect the network tab and check for *MIME* errors is also helpful.

### 8.5 Design Errors

-  **Bug:** After reopening the project folder, *Bootstrap* styles and interactivity broke unexpectedly. The site appeared unstyled, and navbar toggles no longer worked. No recent manual changes had been made to the *base.*html** file.

-  **Fix:** I discovered that the *bootstrap.bundle.min.js* script tag at the bottom of *base.*html** contained a broken *integrity attribute (sha384-...)*. I replaced it with the full, correct version copied from the official *Bootstrap* CDN, which restored all styling and *JS* interactivity.

	 To prevent this I must:
	1. Save all files before switching folders
	2. Restart the editor when switching projects
	3. Use *Git* to track *html* changes, even for template files

-  **Lesson Learned:** Closing and reopening *Django* project folders in *VS Code* without restarting the programme can cause cached or unsaved versions of files to reload incorrectly. In this case, the long integrity attribute was truncated when switching between projects, silently breaking the script load.

-  **Bug:** After a meeting with my mentor he noticed that I had accidentally committed my *SECRET_KEY* and *env.py* file to my *GitHub* repo, exposing sensitive credentials. I noticed that the key was still visible in the commit history even after I had removed it from the most recent version. I also saw that *env.py* was still being tracked by *Git* and visible in the online repository.

  -  **Fix:** I generated a new *SECRET_KEY* using a secure key generator and moved it into a local-only *env.py* file. I then made sure that *env.py* was included in *.gitignore* to prevent it from being tracked again.

	  To remove the old key from *GitHub*’s full history, I used *BFG Repo-Cleaner*:

		1. I cloned a mirror of my repo with *git clone --mirror*
		2. Created a *secrets.txt* file listing the exact secret I wanted removed
		3. Ran *BFG* to replace it with *REMOVED*
		4. Cleaned the *reflog* and *force-pushed* the cleaned history back to GitHub

  		After that, I ran *git rm --cached env.py* to stop *Git* from tracking the file, committed the change, and pushed again. I confirmed that *env.py* is still working locally but is no longer visible or tracked online.

  -  **Lesson Learned:** Never commit sensitive credentials to *GitHub*. Always use a local-only *env.py* file to store them, and make sure it's excluded from *Git* tracking. If you accidentally commit a secret, use *BFG Repo-Cleaner* to remove it from the full history. It is also a good idea to use a key generator to create a new key and update it in the *env.py* file and periodically audit my repo to check for anything that shouldn't be tracked. This was a simple error that took over a day to fix with the help of *Chat GPT* after I failed over three times to try and come to grips with the documentation and help from the *Slack* community.

-  **Bug:** When using the navbar with *Bootstrap*’s hamburger toggler, the search form would disappear after clicking "Search" and navigating to the results page. It only reappeared when manually reopening the hamburger menu. This broke the experience, especially since I want the navbar layout to remain consistent across all screen sizes.

-  **Fix:** I removed the responsive collapse logic by keeping the navbar fully expanded on all screen sizes. I placed the search form next to the nav links and moved the hamburger toggler to the right of it. Then, I added a close (X) icon that toggles dynamically when the hamburger menu is opened and closed.

	  Specifically:
	1. I removed collapse-related responsiveness from the nav links and search form.
	2. I added a second *span* with an "X" (&times;) beside the hamburger icon.
	3. I wrote *JavaScript* to toggle visibility between the hamburger icon and the close icon based on the collapsed menu state.

-  **Lesson Learned:** Just because *Bootstrap* supports collapsing by default doesn't mean it's always the best choice — especially when combining navigation and custom forms. When layout consistency matters more than mobile responsiveness, it’s okay to override Bootstrap's behaviour. Also, small *JavaScript* tweaks like toggling icons can improve UX significantly without breaking core functionality.

-  **Bug:** When using *Chrome*'s autofill to select saved input values (like name or email), the selected text wouldn't appear in the input field — it looked like the form was blank. This was happening across all input fields site-wide, including login, contact, and review forms.

	  I was using an autofill override targeting only *input:-webkit-autofill*, but it didn’t account for *textarea* and *select fields* or properly handle *Chrome*’s aggressive autofill behaviour.

  -  **Fix:** I replaced my original *CSS* with an expanded version that targets all input types and forces the text to show correctly by using *webkit-text-fill-color and a shadow override* and moved it to the bottom of my *CSS* file to make sure that it forced the *autofill overrides*.

-  **Lesson Learned:** Autofill styling in modern browsers (especially *Chrome*) overrides normal input behaviour unless it’s explicitly reset. I also learned that *-webkit-text-fill-color* is crucial for making autofilled text actually visible against a custom background, and that it’s best to override all input-like elements, not just *input*.

### 8.6 Validation Errors

  -  **Bug:** While validating my *base.htm*l using the W3C *HTML* Validator*, I initially encountered errors like:

		1. “Non-space characters found without seeing a doctype first”
		2. “Stray doctype”
		3. “Element *<head>* is missing a required instance of child element *<title>*”
		4. “Cannot recover after last error”

		Even though the structure in my *Django* template was correct, the validator acted like it was broken from the very first line. Later, after fixing that issue and revalidating the rendered output from my browser, I got a second error:

		  "Attribute *`row` not allowed on element `div` at this point."

This pointed to line 88 in the rendered source of my homepage. The layout still looked fine in the browser, but something was clearly wrong according to the validator.

-  **Fix:** The first issue came from copying and pasting raw *Django* template code *({% load static %} and {% static '...' %})* directly into the validator. *HTML* validators don’t recognize *Django* tags and treat them as invalid markup.

	To fix that, I opened my site in the browser, right-clicked the page, chose *“View Page Source”*, and pasted the fully rendered *HTML* into the validator. This solved the false errors caused by *Django*’s template syntax.

	The second issue was a genuine *HTML* bug. In my hero section I had this:

		<div  row  class="row mx-auto justify-content-center align-items-center">

	I had accidentally typed *row* as its own attribute outside the class declaration. That’s not valid *HTML*. I fixed it by removing the stray *row*. After this fix, the page validated cleanly.

  -  **Lesson Learned:** When validating *HTML* in a *Django* project:

		1. Never paste raw *Django* templates into an *HTML* validator — especially files like *base.*html* which aren't full pages.
		2. Always validate the rendered *HTML* by viewing page source in the browser and pasting that into the validator.
		3. Be careful of stray words like *row* outside of *class=""*. These can be hard to spot visually but will break validation.
		4. The *base.*html* can’t be validated directly, because it’s not a full *HTML* document until *Django* renders it with a child template. Trying to validate it raw will always produce misleading errors.

-  **Bug:** Submitting the gig review form gave an error saying "Enter a valid date," even though the date was selected using the calendar input. The form would not save. I had previously changed the date format in my settings file to *DD-MM-YYYY*, so I knew that wasn't the issue.

-  **Fix:** The form was using *input  type="date"* which submits dates in *YYYY-MM-DD* format. However, the form's *input_formats* was incorrectly set to expect *DD-MM-YYYY*. I corrected the *input_formats* to *%Y-%m-%d* and the form started working correctly, as I had previously add the init method, of the form class, as *%d-%m-%Y*.

-  **Lesson Learned:** When using *input  type="date"* in a form widget, always expect *%Y-%m-%d* as the input format. The browser handles formatting, but *Django* needs to know the exact formatting being submitted.
  
-  **Bug:** I wanted to replace *Django*'s default password help text with a custom set of *p* tags so that the styling would match the entire he sign up form. I tried overring the *self.fields["password1"].help_text* using *password_validators_help_texts()*, but *Django* still rendered the original *ul & li* help list. I decided to rollback and avoid customizing the form too deeply, as the logic behind *Django*'s password validation system felt too complex to change confidently and I started to break my code.

-  **Fix:** I rolled back to using *Django*’s built-in *UserCreationForm* and left the default help text rendering untouched. Instead of replacing the *HTML* structure, I used *CSS* to remove the bullets, collapse the spacing, and visually match the default help list with the rest of the form. This gave me full control over the appearance without needing to override the form logic or validators.

-  **Lesson Learned:** Not every problem needs a code-level fix. Sometimes it's better to work with *Django*’s defaults and solve presentation issues using *CSS*. This approach is simpler, more maintainable, and avoids breaking built-in functionality — especially when the underlying logic is complex or abstracted away.

### 8.7 Other Bugs

**Field error**

-  **Bug:** The website links weren't showing up in the search results, even though the template had the correct code and the values were entered via the admin panel.

-  **Fix:** I descovered that the field in both the Artist and Venue models were misspelled *webbsite* instead of *website*. I corrected the spelling in both models and then ran *makemigrations* and *migrate* to update the database.

-  **Lesson Learned:** Model field typos don’t raise obvious errors — they just silently break things in views and templates. Always double-check the spelling of everything as you go along. This will save you a lot of time in the long run.

**Version Control Issue**

-  **Bug:** After committing several changes locally (including fixes for static files), the *git push heroku main:main* command returned "Everything up-to-date", but *Heroku* kept failing with the same *STATIC_ROOT error*. It became clear that *Heroku* was not building from the latest local code. I had made a mistake in my local *Git* repository, which caused a merge conflict when I tried to push my changes to *GitHub*.

-  **Fix:** I had to merge the changes from the main branch into my local branch, resolve the merge conflict, and then push the changes to *GitHub*.

-  **Lesson Learned:** Always make sure your local git repository is up-to-date with the main branch before pushing changes to *GitHub*.

-  **Bug:** I wanted to replace *Django*'s default password help text with a custom set of *p* tags so that the styling would match the ntire he sign up form. I tried overring the *self.fields["password1"].help_text* using *password_validators_help_texts()*, but *Django* still rendered the original *ul & li* help list. I decided to rollback and avoid customizing the form too deeply, as the logic behind *Django*'s password validation system felt too complex to change confidently and I started to break my code.

-  **Fix:** I rolled back to using *Django*’s built-in *UserCreationForm* and left the default help text rendering untouched. Instead of replacing the *HTML* structure, I used *CSS* to remove the bullets, collapse the spacing, and visually match the default help list with the rest of the form. This gave me full control over the appearance without needing to override the form logic or validators.

-  **Lesson Learned:** Not every problem needs a code-level fix. Sometimes it's better to work with *Django*’s defaults and solve presentation issues using *CSS*. This approach is simpler, more maintainable, and avoids breaking built-in functionality — especially when the underlying logic is complex or abstracted away.

**Display Issue**

-  **Bug:** Artist reviews were not appearing directly underneath the artist's bio section as intended. Instead, they were either not rendering at all or were appearing outside of the artist profile layout.

-  **Fix:** I adjusted the template logic and ensured that the artist object and related reviews were passed correctly to the context. I also confirmed that the *HTML* structure placed the reviews section within the same container as the bio, immediately following it.

  -  **Lesson Learned:** Always check the *HTML* structure and context variables when debugging display issues. It's easy to overlook subtle changes in the template logic that can break the layout. Even if the query returns the correct data, the layout won't work unless everything is placed inside the correct blocks in the template.

**Layout Issue**

-  **Bug:** The review sections on my author, artist, and venue profile pages all looked slightly different. Some were centred, others weren’t, and the column layout didn’t behave consistently across screen sizes. The artist reviews especially looked off when arriving from the Wall of Chaos, even though the data was loading correctly.

-  **Fix:** I created a shared partial template called reviews_section.*html* and included it in all profile pages using *{% include 'partials/reviews_section.*html*' %}. I moved the review layout code into that file and updated the grid system to use *Bootstrap*’s column classes with consistent wrappers:

-  **Lesson Learned:** Even when templates are rendering the same data, layout inconsistencies can easily sneak in if markup and class structure aren’t unified. Using a shared partial not only solved the inconsistency but also cleaned up my code. It’s better to centralize layout logic when the content structure is reused across multiple views.

### 8.7 Validation testing Errors

- **Bug:** When I ran the sign-up page through the W3C HTML validation checker, I received an error saying:

	*Element button must not contain interactive content (such as anchor elements)*

	This pointed to the line in my template where I had a *button* wrapping an *a* tag, like this:

		<button type="submit"><a href="{% url 'login' %}">Log in again</a></button>

	This is invalid HTML because *a* is interactive, and interactive elements shouldn’t be nested inside each other (like inside a *button*). The validator flagged this as a structural error.

- **Fix:** I restructured the code to separate the button from the anchor tag. Instead of nesting one inside the other, I used a regular *a* tag styled like a button:

		<a href="{% url 'login' %}" class="btn page-btn">Log in again</a>

	This keeps the look consistent with my other buttons and avoids HTML validation errors.

- **Lesson Learned:** Always avoid putting interactive elements (like *a*, *input*, *button*, tags etc.) inside one another. It might work visually in the browser, but it’s not valid HTML and can cause unexpected issues — especially with screen readers, keyboard navigation, or automated testing.


### 8.8 Bugs Unresolved

-  **Bug:** I wanted to change the highlight colour that appears when selecting or hovering over options in a native *select* dropdown. My goal was to make the selection styling match the custom colour scheme used across the rest of the site.

-  **Fix:** This could not be fixed using standard *CSS*. Most modern browsers (especially *Chrome*, *Safari*, and *Firefox*) render *select* dropdowns and their option lists using native OS UI components, which are not styleable via *CSS*. I considered rebuilding the dropdown as a fully custom component using *JavaScript* and *HTML*, but chose not to pursue this due to the added complexity and time constraints.

-  **Lesson Learner** Some UI elements like native *select* options are outside the scope of *CSS* styling due to how browsers and operating systems render them. In these cases, it’s better to accept the default behaviour or switch to a fully custom solution — which may not be worth it if the rest of the experience is consistent and functional.
