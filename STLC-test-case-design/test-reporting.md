
## 🐞 Bug Report: Age field left empty is not validated

**Priority:** Medium  
**Reporter:** Lucic Miroslav  
**Date:** 14-05-2025  

**Environment:** Test  
**Application:** GroceryMate Webshop  
**Page:** Age Verification Modal  
**Browser / OS:** Chrome / Windows 10  

### Steps to Reproduce:

1. Open the GroceryMate webshop.
2. Add an alcoholic product to the cart.
3. Proceed to checkout.
4. Wait for the age verification modal.
5. Leave the Date of Birth field empty.
6. Click the **Confirm** button.

### ✅ Expected Result:

System should show an error message:
`"Please enter your date of birth."`

### ❌ Actual Result:

System shows the message:
`"You are underage"`
—even though no birth date was entered.

### 📎 Attachments:

![image](https://github.com/user-attachments/assets/a4585e0e-2b22-4696-beec-5901a03cb0c3)
![image](https://github.com/user-attachments/assets/57ebb03d-4ac6-4a49-9460-b6e90e5e53aa)




### ℹ️ Additional Info:

This creates confusion for users. Empty field is not validated and leads to incorrect assumption.

--------------------------------------




## 🐞 Bug Report: Invalid date format is not handled

**Priority:** Medium  
**Reporter:** Lucic Miroslav  
**Date:** 14-05-2025  

**Environment:** Test  
**Application:** GroceryMate Webshop  
**Page:** Age Verification Modal  
**Browser / OS:** Chrome / Windows 10  

### Steps to Reproduce:

1. Open the GroceryMate webshop.
2. Add an alcoholic product to the cart.
3. Wait for the age verification modal.
4. Enter an invalid date like `32/12/2006`.
5. Click the **Confirm** button.

### ✅ Expected Result:

System should validate and show error:
`"Invalid date format. Please use DD/MM/YYYY."`

### ❌ Actual Result:

System accepts the invalid date and shows message:
`"You are underage"`

### 📎 Attachments:

![image](https://github.com/user-attachments/assets/c3bb3b4a-90dc-4e23-8e74-041f11e9ef3b)
![image](https://github.com/user-attachments/assets/252f261d-4135-4a7c-b9a6-1a991ad76941)



### ℹ️ Additional Info:

Missing validation for date format leads to false rejection of eligible users.


