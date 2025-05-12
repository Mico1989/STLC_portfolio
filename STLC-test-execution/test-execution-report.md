#  Test Execution Report – GroceryMate Webshop

This document provides the execution report for the assignment "Homework: Environment Setup, Test Execution, Test Reporting".

## 🔗 Tested Website:
https://grocerymate.masterschool.com/

---
| Test Case ID | Test Description                          | Status | Notes / Bug ID                          |
|--------------|-------------------------------------------|--------|------------------------------------------|
| TC_001       | Submitting valid product rating (4 stars) | Passed | Rating successfully saved and visible   |
| TC_02        | Submitting lowest valid rating (1 star)   | Passed | Rating saved and displayed correctly    |
| TC_03        | Submitting highest valid rating (5 stars) | Passed | Rating submitted and displayed correctly |
| TC_004       | Submit rating without selecting any stars (no rating input) | Passed | System returned: "Invalid input for the field 'Rating'. Please check your input." |
| TC_005       | Submit multiple ratings for same product | Passed | System allows editing an existing rating via “Edit Review” modal. New rating successfully replaces the previous one. |
| TC_006       | Age verification – exactly 18 years | Passed | Age = 12.05.2007. System granted access to alcoholic products. |





##  Notes

- Tests were executed manually using Google Chrome on Windows 10.
- Test design techniques used: Equivalence Partitioning, Boundary Value Analysis, and Error Guessing.
- Bugs will be reported as GitHub Issues in this repository.
- Testing was performed on March 13th, 2025.
