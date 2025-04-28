# Requirements: GroceryMate

## **The software**

You will test a webshop, which can be found here: [https://grocerymate.masterschool.com/](https://grocerymate.masterschool.com/)

The webshop has the following basic functionalities:

-   Register and login functionality
-   Searching for products, sorting on price, categories of products
-   Add products to favorites
-   Add products to basket
-   Check-out process: billing and sending information in a form, choose payment method. Calculation of costs (calculate total price)

## Product Rating System

**Vaque Requirement**
Users should be able to rate products with a 5-star system and have the option to add written feedback.

**Questions**
1. Can a user modify or delete their rating after submitting it? 
2. Can users rate a product without purchasing it first?
3. Is there a character limit for written reviews, and how does the system handle exceeding it?

**Detailed Requirement**
Users must be able to rate products using a **0 to 5-star** rating system.
Users should have the option to **add a written review**.
Users should be able to **view the average rating** of a product based on all submitted ratings.

## Age Verification for Alcoholic Products

**Vaque Requirement**
Alcoholic products require age verification. A modal should appear when navigating to the alcoholic products category asking if the user is 18+. Users must input their age before accessing the alcoholic products.

**Questions**
1. Does the user have to enter their date of birth every time they access the alcoholic products category, or is the age verification stored in a session?
2. What happens if a user enters an incorrect date of birth? Can they retry immediately or after a cooldown period?
3. How does the system prevent underage users from bypassing verification (e.g., using private/incognito mode or clearing cookies)?
4. Can users retry the verification process if they initially enter incorrect information?

**Detailed Requirement**
- The system must display a **modal pop-up** whenever a user attempts to access alcoholic products.
- The modal should include a **date of birth input field** (DD/MM/YYYY format).
- If the user enters a date indicating they are **under 18**, access must be denied, and an appropriate message should be displayed.
- The system should **store verification status** for the session to prevent users from re-entering their age multiple times.
- Users should not be able to bypass verification by **clearing cookies, using incognito mode, or refreshing the page**.
- The modal should have a **clear "Cancel" or "Exit" button** to allow users to leave the verification process if they choose not to proceed.

## Shipping Cost Changes

**Vaque Requirement**
Free shipping for orders above a certain amount. Orders below this amount will incur a shipping fee.

**Questions**
1. What is the exact threshold amount for free shipping, and can it be changed dynamically? 
2. How is the user notified when they qualify for free shipping? 
3. What happens if a user removes an item from the cart, reducing the total below the free shipping threshold?

**Detailed Requirement**
- The system must define a **configurable threshold amount** for free shipping (e.g., $50).
- If the **order total exceeds the threshold**, the shipping fee should be **waived automatically**.
- The user should receive a **real-time notification** (e.g., a banner in the cart or checkout page) when they qualify for free shipping.
- The free shipping threshold should be **customizable** by administrators in the system settings.
- Shipping costs and conditions should be clearly displayed on the **checkout page**.
- If the **order total drops below the threshold** (e.g., by removing an item), the system must:
-   **Reapply the shipping fee** and update the total price.
-   **Display a notification** informing the user of the change.
- 

