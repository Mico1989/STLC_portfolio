#  Test Execution Report – GroceryMate Webshop

This document provides the execution report for the assignment "Homework: Environment Setup, Test Execution, Test Reporting".

## 🔗 Tested Website:
https://grocerymate.masterschool.com/

---
| Test Case ID | Test Description                          | Status | Notes / Bug ID                          |
|--------------|-------------------------------------------|--------|------------------------------------------|
| TC_01       | Submitting valid product rating (4 stars) | Passed | Rating successfully saved and visible   |
| TC_02        | Submitting lowest valid rating (1 star)   | Passed | Rating saved and displayed correctly    |
| TC_03        | Submitting highest valid rating (5 stars) | Passed | Rating submitted and displayed correctly |
| TC_04        | Submit rating without selecting any stars (no rating input) | Passed | System returned: "Invalid input for the field 'Rating'. Please check your input." |
| TC_05        | Submit multiple ratings for same product | Passed | System allows editing an existing rating via “Edit Review” modal. New rating successfully replaces the previous one. |
| TC_06        | Age verification – exactly 18 years | Passed | Age = 12.05.2007. System granted access to alcoholic products. |
| TC_07        | Age verification – just under 18 (DOB: 13.05.2007) | Passed | System message: "You are underage. You can still browse the site, but you will not be able to view alcohol products." |
| TC_08        | Access alcoholic products – user age above 18 (DOB: 12/05/2006) | Passed | User successfully accessed alcoholic products |
| TC_09        | Leave Age field empty | Failed | System incorrectly returns "You are underage" instead of prompting user to enter date of birth. |
| TC_10        | Invalid date format (e.g., 32/12/2006)   | Failed  | No validation for invalid date format. System assumes underage. |
| TC_11        | Order value exactly meets free shipping threshold (20€) | Passed | Shipment cost correctly set to 0€, free shipping applied |
| TC_12        | Order exactly at threshold (€20)        | Passed | No shipping cost applied – system correctly grants free shipping at exact threshold |
| TC_13       | Order just below threshold (€19.99)     | Passed | Shipping fee correctly applied – system charges 5€ when order value is under the 20€ threshold |
| TC_14       | Remove item after reaching free shipping | Passed | Shipping fee applied after removing item and refreshing cart – UI doesn't update fee immediately without refresh. |





















##  Notes

- Tests were executed manually using Google Chrome on Windows 10.
- Test design techniques used: Equivalence Partitioning, Boundary Value Analysis, and Error Guessing.
- Bugs will be reported as GitHub Issues in this repository.
- Testing was performed on March 13th, 2025.
