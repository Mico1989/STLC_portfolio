# XPath Task 2 – XPath Expressions 

# 1. XPath for the highlighted icon/button given in the image below:  
    - `//img[@alt='logo']`

# 2. The XPath of all input fields, sign in button, Create a new account link, and Go to Home link:

   - Email address field:  
     `//input[@type='email' and @placeholder='Email address']`

   - Password field:  
     `//input[@type='password' and @placeholder='Password']`

   - "Sign In" button:  
     `//button[@type='submit' and text()='Sign In']`

   - "Create a new account" link:  
     `//a[contains(@class, 'switch-link') and text()='Create a new account']`

   - "Go to Home" link:  
     `//a[contains(@class, 'home-link') and text()='Go to Home']`

# 3. The XPath (Create a new account) for all input fields, Sign Up button:

    
                     - XPath for the "Full Name" input field:

                            `//input[@type='text' and @placeholder='Full Name']`

                     - XPath for the "Email Address" input field:

                            `//input[@type='email' and @placeholder='Email address']`

                     - XPath for the "Password" input field:

                            `//input[@type='password' and @placeholder='Password']`

                     - XPath for the "Sign Up" button:

                            `//button[@type='submit' and text()='Sign Up']`


# 4. The XPath of Confirm button

  - `//div[@class='modal-content']//button[text()='Confirm']`



# 5.  The XPath for quantity input of Oranges, Add to cart button for Oranges, and add to wish list for Oranges

    - Quantity Input Field:   //div[h3[text()='Oranges']]//input[@type='number'] 

    - Add to Cart button:     //div[h3[text()='Oranges']]//button[contains(text(), 'Add to Cart')]

    - Wish List button:       //div[h3[text()='Oranges']]//button[contains(@class, 'btn-outline-dark')]




