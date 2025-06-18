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

**9.1.1.2** As a **fan**, I can **view consistent and clearly styled password instructions** so that **I feel confident when setting up my account and know exactly what is required**.

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

As a **fan**, I want to **be able to update or delete my profile** so that **I can have full control over my presence on the website**.

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
- [x] Updated information is visible on the public-facing profile *(This was tested later in development, but included here as it part of this user story)*  

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

**9.1.5 What Was Tested**

This user story covers the fan’s ability to view reviews associated with an artist, displayed directly beneath the artist's bio after selecting them from the search bar.

As a **fan**, I can **view artist reviews** so that **I can see what others think about their performances**.

**Acceptance Criteria 1: Search for artist profile**

- [x] Search bar includes an option to select “artist”
- [x] Entering a valid artist name displays the correct artist bio
- [x] Artist details appear at the top of the results section

**Acceptance Criteria 2: Display associated reviews**

- [x] Reviews appear directly below the artist bio
- [x] Only reviews linked to the selected artist are shown
- [x] No other artists’ reviews are displayed

**Acceptance Criteria 3: Responsive layout**

- [x] Review section layout remains consistent across screen sizes
- [x] Reviews remain visually grouped with the artist bio on mobile and desktop
- [x] No overlapping or broken layout issues were found

**Tasks Completed**

- [x] Verified context data passed artist and related reviews correctly to the template
- [x] Placed reviews section directly after the bio block in the HTML structure
- [x] Checked that the reviews used the correct foreign key relationship to the artist

**Notes**

The reviews were initially not appearing under the artist bio due to incorrect template placement and a missing query for related reviews. After adjusting the HTML structure and passing the correct context, the reviews displayed in the right location and matched the selected artist as intended.

#### 9.2 Manual Testing

#### 9.2.1 User Experience Testing

#### 9.2.2 What Was Tested

For my first round of user experience testing, I conducted a usability test with a friend who had no prior experience with the site. The test was conducted at Call of the Wild Festival (COTW). I asked four friends to set up fake profiles and submitted reviews on the app. I asked them to use it naturally in a live music setting and report anything they found confusing, broken, difficult and some general feedback.

- [x] Tested the app in a live music setting at Call of the Wild Festival
- [x] Collected detailed feedback from Paul, Dave, and Julie
- [x] Reviewed screenshots from Julie to identify UI/UX issues
- [x] Compiled feedback into actionable criteria for future testing

**Feedback Summary:**

Paul pointed out that putting spaces in the username during profile setup caused the page to reload without a clear error message. He also noted that his uploaded review image appeared oversized on mobile, requiring multiple swipes to scroll past. Additionally, he felt the review text box was too small, lacking a visible character limit and cutting his input short.

Dave had issues uploading photos, receiving an error that there wasn’t enough memory. He also mentioned that “Lesbian Bed Death” was missing from the band list, and “Brave Revival” was not listed either. He suggested it may be helpful to allow users to suggest bands if admin-only entry is the current setup. Overall, he found the app simple and easy to use.

Julie submitted a review but said the submit button behaved oddly, and her uploaded photo also displayed strangely. She confirmed the text input cut her off before she could finish her thought and suggested there may be a character limit issue. When asked, she said she preferred to avoid “waffle” but still needed room to round off the review properly. She also sent screenshots of the odd behavior for further analysis.

**Profile Setup**

- [x] Users should be informed if their chosen username is invalid (e.g. contains spaces)
- [x] Profile creation page should provide helpful error feedback
- [x] Users can upload a profile image

**Review Submission**

- [x] Review form should accept and store text input
- [ ] Review form should provide a clear character limit notice (e.g. "Max 1000 characters")
- [x] Review form should allow enough text to feel complete without being too long
- [x] Image uploads should scale correctly for mobile
- [x] Users should be able to select a band from a list
- [ ] Band list should be comprehensive or allow suggestions. All known bands (like “Lesbian Bed Death” and “Brave Revival”) are included in the dropdown list
- [x] Review submission button should be consistently responsive
- [x] Image upload should work smoothly without memory issues

**Actional Criteria**

**Profile Setup**
- [ ] Add validation feedback for username errors (e.g. if spaces are included)
- [x] Ensure the profile creation page clearly highlights and explains any input errors

**Review Submission**

- [x] Increase character limit slightly to allow more complete thoughts
- [x] Ensure uploaded images are automatically resized or scaled down for mobile viewing
- [x] Investigate and fix memory-related issues with photo uploads (possibly related to file size or client-side limitations)
- [x] Improve feedback or retry logic when review submission fails or button misbehaves
- [ ] Add a feature or form to allow users to suggest missing bands (optional, depending on admin workflow)

These were then turned into actionable criteria for future testing as *'Github Issues'* and *'Issues'* in the project repository.
  
Tested using:
- Mobiles (iPhone 12, iPad, Galaxy S20, Motorola Edge, iPhone XR)
- OS (Windows, Firefox and Safari)


#### 9.3 Automated Testing

#### 9.3.1 LightHouse

##### 9.3.1.1 Home Page

![Home Page](lh-home-page.png)

##### 9.3.1.2 About Page

![About Page](lh-about-page.png)

##### 9.3.1.3 Wall of Chaos (Gallery)

![Wall of Chaos](lh-wall-of-chaos.png)

##### 9.3.1.4 Login Page

![Login Page](lh-login-page.png)

##### 9.3.1.5 Sign Up Page

![Sign Up Page](image-5.png)

##### 9.3.1.6 Contact Page

![Contact Page](image-6.png)

##### 9.3.1.7 Profile Page

![Profile Page](image-7.png)

![Error Message](image-8.png)

##### 9.3.1.7.1 Profile Edit Page

![Profile Edit Page](image-9.png)

##### 9.3.1.8 Gig Review Form Page

![Gig Review Form Page](image-10.png)

##### 9.3.2 CSS Validation

![CSS Validation](image-11.png)

##### 9.3.3 HTML Validation

##### 9.3.3.1 Home Page

![Home Page](image-13.png)

##### 9.3.3.2 About Page

![About Page](image-14.png)

##### 9.3.3.3 Wall of Chaos (Gallery)

![Wall of Chaos - Gallery page](image-15.png)

##### 9.3.3.4 Login Page



##### 9.3.3.5 Sign Up Page



##### 9.3.3.6 Contact Page



##### 9.3.3.7 Profile Page



##### 9.3.3.7.1 Profile Edit Page



##### 9.3.3.8 Gig Review Form Page



##### 9.3.3.9 Logout Page



##### 9.3.4 Responsive Testing

##### 9.3.4.1 Home Page



##### 9.3.4.2 About Page



##### 9.3.4.3 Wall of Chaos (Gallery)



##### 9.3.4.4 Login Page



##### 9.3.4.5 Sign Up Page



##### 9.3.4.6 Contact Page



##### 9.3.4.7 Profile Page



##### 9.3.4.7.1 Profile Edit Page



##### 9.3.4.8 Gig Review Form Page

##### 9.3.5 JSHint

![JSHint](image-12.png)



