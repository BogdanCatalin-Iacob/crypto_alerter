# Crypto currency alerter

## Description
Keep track of specified crypto coins in a specified bottom / top limits.
This mini project will track only Bitcoin and Ethereum. 
Other coins can be tracked due to live data collected from [Coingecko](coingeckeo.com).

## Resources
-   [Coingecko](https://www.coingecko.com/en/api) get live crypto coind data

## Project Creation

This project was developed using a [VS Code](https://code.visualstudio.com/). The code was committed to [Git](https://git-scm.com) and pushed to [GitHub](https://github.com) using the terminal.

The project was started by navigating to [GitHub](https://github.com) and creating a new repository by clicking `New` button. Under 'Repository name' I input 'crypto_alerter' and then clicked 'Create repository'.

I opened VS Code and initialized directory 'crypto_alerter': 
```
git init
git add README.md
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/BogdanCatalin-Iacob/crypto_alerter.git
git push -u origin main
```
The following commands were used throughout the project:
* `git status` - This command was used to see the modified files before adding them to staging area
* `git add` - This command was used to add files to the staging area before commiting.
* `git commit` -m *commit message explaining teh updates* - This command was used to commit changes to the local repository.
* `git push` - This command was used to push all commited changes to the GitHub repository.

## Local Development
### Making a Local Clone

1. Log in  to Github and locate the [GitHub Repository](https://github.com/BogdanCatalin-Iacob/crypto_alerter)
2. Click the 'Code' button and then choose the method
3. To clone the repository using HTTPS, under the 'HTTPS' tab copy the provided link. You could also choose to open it with GitHub Desktop, Visual Studio or download it as a zip file
4. Open command prompt on your computer
5. Go to the location where you want the clone to be created
6. Type `git clone`, and then paste the URL you copied in step 3
7. Press `Enter` and the clone will be created

### Forking the GitHub repository

Forking means making a copy of the original repository on your own GitHub account.
This gives you your own version to make changes without affecting the original repository.

1. Log in to GitHub and locate [GitHub Repository](https://github.com/BogdanCatalin-Iacob/crypto_alerter)
2. Locate the `Fork` button at the top right of the GitHub page
3. Click this to see the `Create a new fork` page. Click `Create fork` and you should now have a copy of the original repository in your GitHub account.

### Run locally
To run this project on your computer:
1. Open a terminal
2. Navigate to the project directory
3. Create a virtual environment with command `python -m venv <name of virtual environment>`
4. Activate the virtual environment
    * on windows `source <name of virtual environment>/Scripts/activate`
    * on mac `source <name of virtual environment>/bin/activate`
5. Install requirements `pip3 install -r requirements.txt`
6. Type: `python main.py` to run the program.