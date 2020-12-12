# Joshua Haberzettl's Semester Project

**How to use this project:**

1. Make sure you're in the right directory.

Once you have the project in your Visual Studio, you have to go to the correct directory in your terminal, which in this case is called "SemesterProject". 

2. Open the virtual environment.

Before you start it up, you should make sure you're in a virtual environment. To do this, simply type "venv/Scripts/activate" in the terminal and it should activate the one bundled with the project. Sometimes Visual Studio just straight up doesn't work how it should, so you may have to go forward to venv in the directory, then type "Scripts/activate" to get it to recognize it.

3. Tell flask the file you're running

Type "$env:FLASK_APP = "application.py" in the terminal to tell flask which file it should be running.

4. Run flask

From there, all you have to do is type "flask run" into the terminal to run the file. It will give you a link to click to be redirected to the website in a browser.

5. Exit

To exit the file, hit ctrl+c while in the terminal and it will stop running the file. You can also type "deactivate" to get out of the virtual environment once you're finished.