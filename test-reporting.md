## Scenario 1: Invalid Expiration Date Format

As a user of GroceryMate, I want to purchase a product but I'm blocked due to the expiration date field not accepting a valid format.

| Step# | Action                                                                 | Expected Outcome                                               | OK/NOK | URL                                               | Link to issue                                     |
|-------|------------------------------------------------------------------------|----------------------------------------------------------------|--------|---------------------------------------------------|--------------------------------------------------|
| 1     | Go to checkout page                                                    | Checkout page loads                                            | OK     | https://grocerymate.masterschool.com             |                                                  |
| 2     | Fill in all shipment and payment details                               | Form filled                                                    | OK     |                                                   |                                                  |
| 3     | Enter expiration date as `02/26`                                       | System accepts date                                            | NOK    | /checkout                                         | [#3](https://github.com/Mico1989/STLC_portfolio/issues/3) |
| 4     | Click "Buy now"                                                        | Order should be processed                                      | NOK    |                                                   |                                                  |

---

 **Bug Summary:**  
Expiration field incorrectly requires 7 or more characters, even though `MM/YY` is a valid format.  
Validation message: "Please lengthen this text to 7 characters or more (you are currently using 5 characters)."


###  Scenario 2: Product Rating Not Accessible

> As a user of GroceryMate, I want to leave a rating for a purchased product, but I am blocked from completing the purchase, so the rating option is not available.

| Step# | Action                                   | Expected Outcome                        | OK/NOK | URL                                       | Link to issue |
|-------|------------------------------------------|------------------------------------------|--------|--------------------------------------------|---------------|
| 1     | Go to checkout page                      | Checkout page loads                      | OK     | https://grocerymate.masterschool.com      |               |
| 2     | Fill in all shipment and payment details | Form filled                              | OK     | /checkout                                 |               |
| 3     | Enter expiration date as `02/26`         | System accepts date                      | NOK    | /checkout                                 | [#3](https://github.com/Mico1989/STLC_portfolio/issues/3) |
| 4     | Try to complete purchase                 | Order should be processed                | NOK    | /checkout                                 | [#3](https://github.com/Mico1989/STLC_portfolio/issues/3) |
| 5     | Navigate to product page and try to rate | Rating option is available               | NOK    | /product                                  |               |

---

###  Bug Summary:
Rating functionality is blocked because the purchase flow is not completed.  
Since the user cannot complete the order due to a bug in the expiration field, rating becomes inaccessible.  

**Blocked functionality:** ⭐ Product Rating (Test Case TC_03)
