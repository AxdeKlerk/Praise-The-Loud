### 9. Testing
All functionality was tested manually by walking through user stories. Testing was carried out in Google Chrome and Firefox across desktop and mobile screen sizes. DevTools were used to check responsiveness and console errors. Forms and dynamic elements were tested for validation, correct behaviour, and feedback.

#### 9.1 User Stories

##### 9.1.1 What Was Tested

This user story covers the full flow of registration, profile creation, and social link input.

As a **fan**, I can **register an account** so that I can **create a profile**.

**Acceptance Criteria 1: Register an account**
- [x] Register page loads without errors
- [x] All required fields (username, email, password) are present
- [x] Password confirmation matches check is working
- [x] Error messages appear for duplicate usernames or mismatched passwords

**Acceptance Criteria 2: Create a profile**
- [x] After registering, the user is directed to a profile form
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
- [ ] Updated information is visible on the public-facing profile  

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

#### 9.2 Manual Testing

#### 9.3 Automated Testing

#### 9.4 Code Validation

#### 9.5 Performance Testing

##### 9.5.1 Responsive Testing

Tested using:
- Chrome DevTools (iPhone 12, iPad, Galaxy S20)
- Windows desktop, MacBook, iPhone XR
- Layout and forms adapt well across screen sizes

