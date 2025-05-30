### 9. Testing
All functionality was tested manually by walking through user stories. Testing was carried out in Google Chrome and Firefox across desktop and mobile screen sizes. DevTools were used to check responsiveness and console errors. Forms and dynamic elements were tested for validation, correct behaviour, and feedback.

#### 9.1 User Stories

##### 9.1.1 What Was Tested

**9.1.1.1** This user story covers the full flow of registration, profile creation, and social link input.

As a **fan**, I can **register an account** so that I can **create a profile**.

**Acceptance Criteria 1: Register an account**
- [x] Register page loads without errors and shows a *Hello User* message in navbar
- [x] All required fields (username, email, password) are present
- [x] Password confirmation matches check is working
- [x] Error messages appear for duplicate usernames or mismatched passwords

**Acceptance Criteria 2: Create a profile**
- [x] After registering, the user can navigate to a profile form
- [x] The form includes fields for bio, photo upload, and social links
- [x] Submitting the profile form creates a new Fan Profile linked to the user
- [x] Validation prevents submission of incomplete or empty required fields

**Acceptance Criteria 3: Add a photo and bio**
- [x] File upload works (tested with PNG and JPG)
- [x] Image is uploaded to Cloudinary
- [x] Bio field saves and displays on the profile page

**Acceptance Criteria 4: Add links to Facebook and Instagram**
- [x] Fields for social media links are present and optional
- [x] Submitted links save correctly and are clickable
- [x] Links open in a new tab

**Tasks Completed**
- [x] Installed Django authentication with registration and login functionality
- [x] Created profile page with support for photo upload and bio
- [x] Added input fields for Facebook and Instagram links

**Notes**
Initial Cloudinary image uploads failed due to incorrect environment variable setup. This was resolved by configuring *'env.py'* and using *'CloudinaryField'* in the model. Also ran into an issue where the JS for delete confirmation didn't work due to broken static file paths — this was fixed by correcting the path with *'{% static %}'* and ensuring static files were served via *'urls.py'*.

**9.1.1.2** As a fan, I can view consistent and clearly styled password instructions so that I feel confident when setting up my account and know exactly what is required.

**Acceptance Criteria 5: Password help text styling**

- [x] The password help text appears using Django’s default validation messages
- [x] Bullet points are removed using CSS without modifying Django’s logic
- [x] The spacing between the password input and help text matches the spacing on other fields
- [x] Help text is styled to match the form's colour scheme and font
- [x] No unwanted margin or list styling appears in the final rendered form
- [x] All password validation rules still apply on form submission

Tasks Completed

- [x] Reverted from using CustomUserCreationForm to Django’s built-in UserCreationForm
- [x] Applied CSS to style and space .helptext and remove list bullets
- [x] Tested signup page to ensure visual consistency and validator functionality remained intact

**Notes**
Originally attempted to override the password help text using a custom form and <p> tags for cleaner output. This was rolled back to preserve Django’s default behavior and reduce complexity, relying instead on CSS for full visual control.



**Screenshots**


##### 9.1.2 What Was Tested

This user story covers the ability for fans to edit or delete their profile, including image updates and confirmation before deletion.

As a **Fan**, I want to **be able to update or delete my profile** so that **I can have full control over my presence on the website**.

**Acceptance Criteria 1: Profile form can be edited and updated**

- [x] Update button appears when viewing an existing profile  
- [x] Clicking the button loads the profile form with existing data  
- [x] Updating text fields and submitting saves changes correctly  
- [x] Success message is shown after update  

**Acceptance Criteria 2: Profile image can be changed**

- [x] Existing image is displayed on the update form  
- [x] Selecting a new image replaces the old one after submission  
- [x] Updated image is stored in Cloudinary  

**Acceptance Criteria 3: Update form shows existing profile data and changes are saved and displayed correctly**

- [x] All profile fields pre-fill with the user's current data  
- [x] Edited data persists after refresh  
- [ ] Updated information is visible on the public-facing profile *(This was tested later in development, but included here as it part of this user story)*  

**Acceptance Criteria 4: Form deletion shows a pop-up warning before confirming deletion**

- [x] Delete button appears alongside the update button  
- [x] Clicking the delete button triggers a JS confirmation popup  
- [x] Profile is only deleted if user confirms  
- [x] User is redirected to homepage after deletion  

**Tasks Completed**

- [x] Created update and delete buttons in profile view  
- [x] Enabled image update functionality with Cloudinary  
- [x] Added confirmation message after update  
- [x] Implemented JavaScript delete confirmation popup  

**Notes**

The delete confirmation popup initially failed to appear after static files were moved to a global directory. This was resolved by fixing the path to *'scripts.js'* in *'base.html'* using *'{% static %}'* and confirming the file was being loaded by checking for a *'console.log'* message in the browser console.

**Screenshots**

**9.1.3 What Was Tested**

This user story covers the fan login process, viewing an existing profile, and accessing the review form through the navigation bar.

As a **fan**, I can **login** so that I can **view my profile and leave a review**.

**Acceptance Criteria 1: Successfully log in**

- [x] Login page loads with fields for username and password  
- [x] Error messages appear for incorrect credentials  
- [x] Successful login redirects to the homepage or dashboard  
- [x] User session persists across navigation  

**Acceptance Criteria 2: View already created profile**

- [x] 'Profile' link is visible in the navigation bar after login  
- [x] Clicking the link shows the fan’s profile  
- [x] Profile displays correct image, bio, and social links  

**Acceptance Criteria 3: Navigate to the gig review form**

- [x] 'Gig Review' link appears in the navbar after login  
- [x] Clicking the link loads the review form page  
- [x] Form loads correctly and is accessible to logged-in users  

**Tasks Completed**

- [x] Created navigation bar with 'Profile' and 'Gig Review' links in *'base.html'*  
- [x] Used Django’s template inheritance to extend *'base.html'* across all pages  
- [x] Ensured navigation links only appear to logged-in users using template logic  

**Notes**

No major issues were encountered during testing. The login, profile access, and review navigation worked as expected. Session persistence and conditional display of nav links based on login state were verified through manual testing.

**Screenshots**

**9.1.4 What Was Tested**

This user story covers the fan's ability to log in, navigate to the review form, write a review for an artist, and see the review immediately appear on their profile page after submission.

As a **fan**, I can **log in** so that **I can leave a review for the artist**.

**Acceptance Criteria 1: Navigate to the gig review form**

- [x] 'Gig Review' link appears in the navigation bar after login  
- [x] Clicking the link loads the review form  
- [x] Form is only accessible to logged-in users  

**Acceptance Criteria 2: Write review**

- [x] Form contains fields for artist, venue, date, title, photo and review text
- [x] Date field uses a browser-native calendar picker 
- [x] User can select a gig date without typing manually  

**Acceptance Criteria 3: Submit review and view it on profile**

- [x] Review is saved to the database  
- [x] User is redirected to their profile page after submission  
- [x] Submitted review appears immediately on the profile page  

**Tasks Completed**

- [x] Created form using Django's *'ModelForm'* for the *'GigReview'* model  
- [x] Set *'type="data"'* for the gig date widget  
- [x] Added *'imput_formats'* to match browser submission format  
- [x] Ensured review appears on profile page after submission  

**Notes**

The review form initially rejected valid dates with a *“Enter a valid date”* error because the input format was incorrectly set. This was corrected to to match the format sent by the browser's calendar picker. After this fix, the form submitted successfully and the review appeared immediately on the profile page.

**Screenshots**

#### 9.2 Manual Testing

#### 9.3 Automated Testing

#### 9.4 Code Validation

#### 9.5 Performance Testing

##### 9.5.1 Responsive Testing

Tested using:
- Chrome DevTools (iPhone 12, iPad, Galaxy S20)
- Windows desktop, MacBook, iPhone XR
- Layout and forms adapt well across screen sizes

