# XPath Task 2 – XPath Expressions 

1. XPath for the highlighted icon/button given in the image below:  
    - `//img[@alt='logo']`

2. The XPath of all input fields, sign in button, Create a new account link, and Go to Home link:

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


