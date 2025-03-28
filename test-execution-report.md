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


### Additional Executed Test Cases (based on designed scenarios)

| Test Case ID | Test Description                                          | Status       | Notes / Bug ID                                  |
|--------------|-----------------------------------------------------------|--------------|--------------------------------------------------|
| TC_001       | Submit valid product rating (1–5 stars)                   | Not Executed |                                                  |
| TC_002       | Submit multiple ratings for same product                  | Not Executed |                                                  |
| TC_003       | Age verification – user exactly 18                        | Not Executed |                                                  |
| TC_004       | Age verification – under 18                               | Not Executed |                                                  |
| TC_005       | Free shipping threshold exactly met ($50)                | Not Executed |                                                  |
| TC_006       | Shipping falls below threshold after removing item       | Not Executed |                                                  |
| TC_007       | No rating selected, try to submit                         | Not Executed |                                                  |
| TC_008       | DOB field left empty                                      | Not Executed |                                                  |
| TC_009       | Invalid DOB format                                        | Not Executed |                                                  |
| TC_010       | Order above threshold ($51)                               | Not Executed |                                                  |
| TC_011       | Order just below threshold ($49.99)                       | Not Executed |                                                  |
| TC_012       | Apply discount, drops total below free shipping limit     | Not Executed |                                                  |
| TC_013       | Submit lowest rating (1 star)                             | Not Executed |                                                  |
| TC_014       | Submit highest rating (5 stars)                           | Not Executed |                                                  |
| TC_015       | Rating flow blocked on specific browser                   | Not Executed |                                                  |

##  Notes

- Tests were executed manually using Google Chrome on Windows 10.
- Test design techniques used: Equivalence Partitioning, Boundary Value Analysis, and Error Guessing.
- Bugs will be reported as GitHub Issues in this repository.
- Testing was performed on March 13th, 2025.
