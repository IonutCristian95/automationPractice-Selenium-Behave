<h1>﻿# Automation Practice</h1>
 
 
<h2>﻿#Project Description:</h2>

<h5>An automation testing project using Python, Selenium and Behave Framework(Gherkin syntax).
 
You need a "credentials.txt" file located in features folder with your account's credentials from http://automationpractice.com/index.php . The file should contain the email in the first row and the password in the second row with no blank spaces.</h5>
Example credentials.txt:

*test@test.com*<br>
*password123*

<hr>
<h2>﻿# Installation:</h2>
 <ul><li>pip install selenium</li>
 <li>pip install behave</li>
 <li>pip install nose</li>
 <li>pip install behave-html-formatter</li>
 </ul>

<h2>﻿# How to run:</h2>
 Command to run the tests: behave -f html -o destination [--tags=tag-name]
 
[destination] - usually at *reports/file-name.html* <br>
 *\*optional\** [--tags=tag-name] - run a specific test with @tag-name at the top <br>
 
 Example: <br>
<pre>
 @tag-name <br>
 Scenario: User adds an element to the list<br>
      When: user clicks the add to the list button <br>
      Then: the element is added to the list <br>
</pre>
<hr>
In case Google Chrome gets an update, you can download the latest version at https://chromedriver.chromium.org/downloads . <br>
In this case, you need to update the variable driver in *features/browser.py* . <br>

<code>
  driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
</code> <br>
The executable_path will be the path to the chromedriver.exe file. Either change the chromedriver.exe file with the latest, or change the path to point to the chromedriver file with the latest version.
<hr> <br>
The behave.ini file is needed to avoid the error:
<code>behave: error: format=html is unknown.</code>
