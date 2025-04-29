****Web UI Testing Documentation****

**Objective**

To automate and validate core functionalities of a web-based e-commerce application using Selenium
WebDriver and Python (with Pytest). This project tests login, homepage navigation, and shopping cart
features. 
**Tools & Technologies Used**
- Python
- Selenium WebDriver
- Pytest - WebDriver Manager
- Page Object Model (POM)
- ChromeDriver
  
**Project Structure**

project_root/
test/
test_main.py
pom/
  page/
    login_page.py
      home_page.py
        cart_page.py
        
**Test Workflow Overview**
1. Login Tests
2. Home Page Navigation
3. Cart Functionality


**Test Cases Breakdown**

test_login: - Checks multiple login scenarios.

test_home: - Tests menu, cart, and sort actions. 

test_cart: - Adds/removes items and completes checkout.

**Test Cases**
1. Login Page
   ![image](https://github.com/user-attachments/assets/83ec2bba-3e47-4fee-87db-88907920f188)

3. Home Page
   ![image](https://github.com/user-attachments/assets/0b820d31-f923-4aae-a0bb-226ee96ef667)

5. Cart Page
   ![image](https://github.com/user-attachments/assets/ec9e4e67-b412-45ad-a73d-942667df8543)

Page Object Model (POM) Usage
- login_page: login functions
- home_page: navigation elements
- cart_page: cart and checkout
Error Handling & Validation
Login test includes try-except with 'product' in page check and assertions for test pass/fail. Test Results Summary
test_login (valid) - Passed
test_login (invalid) - Failed
test_home - Passed
test_cart - Passed

**Note:**Test cases are not actually correct and properly prepared.
