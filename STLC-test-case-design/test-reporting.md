
##  Bug Report

### Title:
System returns incorrect validation when Age field is left empty

### Priority:
Medium

### Reporter:
Lucic Miroslav

### Date:
14-05-2025

### Environment:
Test

### Application:
GroceryMate Webshop

### Page:
Age Verification Modal

### Browser / Operating System:
Chrome / Windows 10

### Steps to Reproduce:
1. Open the GroceryMate webshop.
2. Add an alcoholic product to the cart.
3. Proceed to checkout.
4. Wait for the age verification modal to appear.
5. Do **not** enter any date into the Date of Birth field.
6. Click the **Confirm** button.

### Expected Result:
System should display an error message like:  
`"Please enter your date of birth."`

### Actual Result:
System incorrectly returns the message:  
`"You are underage"`  
—even though no date was entered.

### Screenshots / Attachments:
* (Insert screenshot showing the modal and error message here, if available)

### Additional Information:
This bug can confuse users by falsely indicating they are underage, even if they never entered a birth date. Proper validation for empty input is missing.






##  Bug Report

### Title:
Invalid Date Format Not Handled – System incorrectly assumes underage

### Priority:
High

### Reporter:
Lucic Miroslav

### Date:
14-05-2025

### Environment:
Test

### Application:
GroceryMate Webshop

### Page:
Age Verification Modal

### Browser / Operating System:
Chrome / Windows 10

### Steps to Reproduce:
1. Open the GroceryMate webshop.
2. Add an alcoholic product to the cart.
3. Wait for the age verification modal to appear.
4. Enter an invalid date format in the input field, e.g. `32/12/2006`.
5. Click the **Confirm** button.

### Expected Result:
System should display an error like:  
`"Invalid date format. Please use DD/MM/YYYY."`  
and not proceed with verification.

### Actual Result:
System assumes user is underage and displays the message:  
`"You are underage"`

### Screenshots / Attachments:
* (Insert screenshot showing invalid input and resulting message)

### Additional Information:
There is no validation for invalid or impossible dates. This leads to false negatives for age eligibility and may block valid users who mistype their birth date.


