# **Test Plan for Market Mate Webshop**

## **1. Analyze the Product**

### **Objective**

The objective of this test plan is to ensure the proper functionality and usability of the new features introduced in the Market Mate webshop. The focus is on validating the **Product Rating System, Age Verification for Alcoholic Products, and Shipping Cost Changes** to confirm they meet business and user requirements.

### **User Base**

The webshop is used by:

-   **Regular Customers** – Shoppers looking to buy various products, including alcoholic beverages.
    
-   **Administrators** – Responsible for managing product listings, reviews, and system configurations.
    
-   **Delivery Personnel** – Interacting with the order processing system.
    

### **Hardware and Software Specifications**

#### **Hardware Requirements:**

-   Devices: PCs, laptops, smartphones, tablets
    
-   Specifications: Minimum 4GB RAM, 2GHz processor for desktops, standard configurations for Android and iOS devices
    

#### **Software Requirements:**

-   Operating Systems: Windows, macOS, Android, iOS
    
-   Browsers: Chrome, Firefox, Safari, Edge
    
-   Dependencies: Backend services, payment gateways, authentication modules
    

### **Product Functionality**

The webshop allows users to:

-   Register and log in
    
-   Search for products and filter by price and category
    
-   Add products to favorites and the shopping cart
    
-   Complete the checkout process with various payment methods
    
-   Use newly introduced features:
    
    -   **Product Rating System:** Customers can rate and review products.
        
    -   **Age Verification for Alcoholic Products:** Users must confirm their age before purchasing alcohol.
        
    -   **Shipping Cost Changes:** Free shipping applies above a specific order threshold.
        

----------

## **2. Design the Test Strategy**

### **Scope of Testing**

#### **In Scope:**

-   Functional testing of new features (Product Rating, Age Verification, Shipping Cost)
    
-   GUI testing to ensure usability and UI consistency
    
-   API testing for backend interactions
    
-   Performance testing for checkout and review submission processes
    
-   Security testing for age verification and rating submission
    

#### **Out of Scope:**

-   Payment gateway functionality (assumed to be pre-tested and stable)
    
-   Backend infrastructure performance testing
    

### **Type of Testing**

-   **Functional Testing** – To verify that new features work as expected.
    
-   **Regression Testing** – To ensure no existing functionalities are broken.
    
-   **Security Testing** – For age verification and unauthorized access prevention.
    
-   **Usability Testing** – To check user experience improvements.
    
-   **Performance Testing** – To validate system responsiveness.
    

### **Risks and Issues**

-   **Delays in development** → Mitigation: Implement buffer period in the test schedule.
    
-   **Lack of test data** → Mitigation: Create mock user accounts and datasets.
    
-   **Resource unavailability** → Mitigation: Assign backup QA engineers.
    

### **Test Logistics**

-   **Test Manager:** [Name]
    
-   **QA Engineers:** [Team Members]
    
-   **End Users (UAT):** [Designated Users]
    

----------

## **3. Define Test Objectives**

### **Objectives**

-   **Functionality:** Ensure all new features work as per requirements.
    
-   **GUI:** Verify that the interface is user-friendly and meets design standards.
    
-   **Performance:** Confirm system response under expected loads.
    
-   **Security:** Ensure that unauthorized users cannot bypass age verification.
    
-   **Usability:** Validate ease of use and accessibility.
    

### **Expected Outcomes**

-   **All features function correctly.**
    
-   **User interface is intuitive and consistent.**
    
-   **System meets performance benchmarks.**
    
-   **No critical security vulnerabilities exist.**
    
-   **Users can easily navigate and use new features.**
    

----------

## **4. Define Test Criteria**

### **Suspension Criteria**

-   Testing will be halted if critical defects prevent further execution.
    
-   Test execution will pause if the test environment becomes unstable.
    

### **Exit Criteria**

-   All planned test cases have been executed.
    
-   95% of tests completed, with a pass rate of at least 90%.
    
-   No severity 1 or severity 2 defects remain open.
    
-   UAT sign-off has been obtained.
    

----------

## **5. Resource Planning**

-   **Human Resources:** QA team, developers, UAT users
    
-   **Hardware:** PCs, smartphones, tablets
    
-   **Software:** Browsers (Chrome, Firefox, Safari, Edge), automation tools (Selenium, Postman)
    
-   **Infrastructure:** Test environments, bug tracking tools (JIRA, TestRail)
    

----------

## **6. Plan Test Environment**

-   **Test Environments:** Development (DEV), Testing (TEST), User Acceptance Testing (UAT)
    
-   **Tools:** Selenium, Postman, TestRail, JIRA
    
-   **Devices:** Android, iOS, Windows, macOS
    

----------

## **7. Schedule and Estimation**




## **8. Determine Test Deliverables**

| Activity             | Start Date | End Date   | Environment | Responsible      | Estimated Effort |
|----------------------|------------|------------|-------------|------------------|------------------|
| Test Planning       | 01/03/2024 | 05/03/2024 | All         | Test Manager     | 20h              |
| Test Case Design    | 06/03/2024 | 12/03/2024 | All         | QA Team          | 40h              |
| Functional Testing  | 13/03/2024 | 20/03/2024 | TEST        | QA Team          | 60h              |
| Regression Testing  | 21/03/2024 | 25/03/2024 | TEST        | QA Team          | 30h              |
| Performance Testing | 26/03/2024 | 28/03/2024 | TEST        | QA Team          | 20h              |
| Security Testing    | 29/03/2024 | 30/03/2024 | TEST        | QA Team          | 15h              |
| UAT                 | 01/04/2024 | 05/04/2024 | UAT         | End Users        | 50h              |
| Production Release  | 06/04/2024 | 06/04/2024 | PROD        | DevOps Team      | 10h              |



### **Documents & Tools**

-   **Test Plan Document** – This document
    
-   **Test Cases** – For functional, regression, and performance testing
    
-   **Test Data** – Mock user accounts and input datasets
    
-   **Test Reports** – Summary of test execution results
    
-   **Defect Reports** – Logged issues in JIRA
    
-   **UAT Sign-off** – Formal approval from business stakeholders




# **Test Case Design for Market Mate Webshop**

## **1. Product Rating System**

**Test Design Techniques:** Equivalence Partitioning (EP), Boundary Value Analysis (BVA), Error Guessing

### **Test Cases:**

1.  **Equivalence Partitioning (EP)**
    
    -   **Test Case:** Verify that a user can submit a valid product rating (1 to 5 stars).
        
        -   **Input:** User selects a rating of 4 stars and submits.
            
        -   **Expected Outcome:** Rating is saved successfully and displayed under the product.
            
2.  **Boundary Value Analysis (BVA)**
    
    -   **Test Case:** Verify behavior when the user tries to submit the lowest valid rating (1 star).
        
        -   **Input:** User selects 1 star and submits.
            
        -   **Expected Outcome:** Rating is saved successfully and displayed.
            
3.  **Boundary Value Analysis (BVA)**
    
    -   **Test Case:** Verify behavior when the user tries to submit the highest valid rating (5 stars).
        
        -   **Input:** User selects 5 stars and submits.
            
        -   **Expected Outcome:** Rating is saved successfully and displayed.
            
4.  **Error Guessing**
    
    -   **Test Case:** Verify system behavior when the user does not select a rating and tries to submit.
        
        -   **Input:** No rating is selected, user clicks submit.
            
        -   **Expected Outcome:** Error message "Please select a rating before submitting."
            
5.  **Error Guessing**
    
    -   **Test Case:** Verify system behavior when the user submits multiple ratings for the same product.
        
        -   **Input:** User submits a 3-star rating, then tries to submit a 5-star rating for the same product.
            
        -   **Expected Outcome:** Either the last submitted rating overrides the previous one or an error message appears.
            

----------

## **2. Age Verification for Alcoholic Products**

**Test Design Techniques:** Boundary Value Analysis (BVA), Equivalence Partitioning (EP), Error Guessing

### **Test Cases:**

1.  **Boundary Value Analysis (BVA)**
    
    -   **Test Case:** Verify that a user exactly 18 years old can access alcoholic products.
        
        -   **Input:** Date of Birth = (Today - 18 years)
            
        -   **Expected Outcome:** User is granted access.
            
2.  **Boundary Value Analysis (BVA)**
    
    -   **Test Case:** Verify that a user just below 18 years old is denied access.
        
        -   **Input:** Date of Birth = (Today - 17 years, 11 months, 30 days)
            
        -   **Expected Outcome:** Error message "You must be at least 18 years old to access this category."
            
3.  **Equivalence Partitioning (EP)**
    
    -   **Test Case:** Verify that users above 18 years old can access alcoholic products.
        
        -   **Input:** Date of Birth = (Today - 19 years)
            
        -   **Expected Outcome:** User is granted access.
            
4.  **Error Guessing**
    
    -   **Test Case:** Verify system behavior when Date of Birth field is left empty.
        
        -   **Input:** No date entered.
            
        -   **Expected Outcome:** Error message "Please enter your date of birth."
            
5.  **Error Guessing**
    
    -   **Test Case:** Verify system behavior when an invalid date format is entered.
        
        -   **Input:** Date of Birth = "32/12/2006"
            
        -   **Expected Outcome:** Error message "Invalid date format. Please use DD/MM/YYYY."
            

----------

## **3. Shipping Cost Changes**

**Test Design Techniques:** Equivalence Partitioning (EP), Boundary Value Analysis (BVA), Error Guessing

### **Test Cases:**

1.  **Equivalence Partitioning (EP)**
    
    -   **Test Case:** Verify that orders above the free shipping threshold do not incur a shipping fee.
        
        -   **Input:** Order value = $51 (free shipping threshold is $50)
            
        -   **Expected Outcome:** No shipping cost applied.
            
2.  **Boundary Value Analysis (BVA)**
    
    -   **Test Case:** Verify that an order exactly at the free shipping threshold gets free shipping.
        
        -   **Input:** Order value = $50
            
        -   **Expected Outcome:** No shipping cost applied.
            
3.  **Boundary Value Analysis (BVA)**
    
    -   **Test Case:** Verify that an order just below the threshold incurs a shipping fee.
        
        -   **Input:** Order value = $49.99 (free shipping threshold is $50)
            
        -   **Expected Outcome:** Shipping fee is applied.
            
4.  **Error Guessing**
    
    -   **Test Case:** Verify system behavior when a user removes items from the cart, causing the total to fall below the free shipping threshold.
        
        -   **Input:** User initially adds $55 worth of products (free shipping applies), then removes an item worth $10.
            
        -   **Expected Outcome:** Shipping fee is applied again.
            
5.  **Error Guessing**
    
    -   **Test Case:** Verify system behavior when a user applies a discount that lowers the order total below the free shipping threshold.
        
        -   **Input:** Order value = $55, user applies a $10 discount.
            
        -   **Expected Outcome:** Shipping fee is applied again.
            


## Automation Considerations

### Test Cases to Automate and Why:

| Test Case ID | Feature          | Reason for Automation                                      |
|-------------|------------------|------------------------------------------------------------|
| TC-001      | Product Rating    | Frequently executed, ideal for regression testing         |
| TC-005      | Product Rating    | Edge case scenario, prevents duplicate ratings            |
| TC-002      | Age Verification  | Compliance testing, needs consistency                     |
| TC-004      | Age Verification  | Common user mistake, automating saves manual effort      |
| TC-003      | Shipping Cost     | Affects user experience, must always work correctly       |
| TC-005      | Shipping Cost     | Price calculations are error-prone, automation ensures accuracy |
