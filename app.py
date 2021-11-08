# This call will import the declared 'app' object from the market directory/package.
from graphxl import app

# Checks if the app.py file has executed directly and not imported
# The statement if __name__ == “__main__” is used in any python script 
# to make it standalone script (the main functiona). 
# When the interpreter executes python file, the __name__ variable 
# is set to “__main__” value. If the script or file is 
# imported as module in the another file then the value of __name__ is set 
# to module name instead of “__main__”.
# Here we want the app.run() to be executed when Python launches this file.
# The app object is created in the __init__.py file when the market package is initialized.
if __name__ == '__main__':
    # By including app.run (flask) we can now run our Flask webapp using
    # the command 'python app.py' instead of 'python -m flask run' command.
    # This calls the first python executable on PATH, and passes app.py as argument. 
    # It will make python run the app.py script, which may or may not have 
    # app.run() (This is what starts Flask). If you don't have anything inside app.py, 
    # it won't call Flask's server.
    app.run(debug=True)