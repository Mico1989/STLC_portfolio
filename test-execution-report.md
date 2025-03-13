#  Test Execution Report – GroceryMate Webshop

This document provides the execution report for the assignment "Homework: Environment Setup, Test Execution, Test Reporting".

## 🔗 Tested Website:
https://grocerymate.masterschool.com/

---

##  Executed Test Cases

| Test Case ID | Test Description                                           | Status   | Notes / Bug ID                                               |
|--------------|------------------------------------------------------------|----------|---------------------------------------------------------------|
| TC_01        | Entering postal code or CVV with less than required characters | Passed   | Validation message shown correctly                            |
| TC_02        | Entering expiration date as 02/26                          | Failed   | BUG_001 – Expiration field incorrectly requires 7+ characters |
| TC_03        | Submitting valid rating (4 stars)                          | Blocked  | Purchase flow incomplete – cannot access rating               |

---

##  Notes

- Tests were executed manually using Google Chrome on Windows 10.
- Test design techniques used: Equivalence Partitioning, Boundary Value Analysis, and Error Guessing.
- Bugs will be reported as GitHub Issues in this repository.
- Testing was performed on March 13th, 2025.
