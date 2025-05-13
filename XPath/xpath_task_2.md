# XPath Task 2 

## 1. XPath for the highlighted icon/button given in the image:
- `//img[@alt='logo']`

---

## 2. XPath of all input fields, "Sign In" button, "Create a new account" link, and "Go to Home" link:

- **Email address field:**  
  `//input[@type='email' and @placeholder='Email address']`

- **Password field:**  
  `//input[@type='password' and @placeholder='Password']`

- **"Sign In" button:**  
  `//button[@type='submit' and text()='Sign In']`

- **"Create a new account" link:**  
  `//a[contains(@class, 'switch-link') and text()='Create a new account']`

- **"Go to Home" link:**  
  `//a[contains(@class, 'home-link') and text()='Go to Home']`

---

## 3. XPath for "Create a new account" form – all input fields and "Sign Up" button:

- **Full Name input field:**  
  `//input[@type='text' and @placeholder='Full Name']`

- **Email Address input field:**  
  `//input[@type='email' and @placeholder='Email address']`

- **Password input field:**  
  `//input[@type='password' and @placeholder='Password']`

- **"Sign Up" button:**  
  `//button[@type='submit' and text()='Sign Up']`

---

## 4. XPath of the "Confirm" button (in modal window):

- `//div[@class='modal-content']//button[text()='Confirm']`

---

## 5. XPath for **Oranges** – Quantity input, "Add to Cart" button, and "Add to Wishlist" button:

- **Quantity input field:**  
  `//div[h3[text()='Oranges']]//input[@type='number']`

- **"Add to Cart" button:**  
  `//div[h3[text()='Oranges']]//button[contains(text(), 'Add to Cart')]`

- **"Add to Wishlist" button:**  
  `//div[h3[text()='Oranges']]//button[contains(@class, 'btn-outline-dark')]`




