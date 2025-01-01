
This Bank App is a financial transaction application where user is able to create an account, debit, credit and  display the balance of money in the bank account. The options are displayed in the App where you can make a choice on what transaction you are interested in.

Account number are generated and details stored in the google speadsheet.

<img src="image/Screenshot (9).png" alt="The Bank account spreadsheet">

<img src="image/Screenshot (14).png" alt="Difficulty to validate via python heroku">

<img src="image/Screenshot (16).png" alt="Bank App functionality">

## Technologies Used

The main technology used to create this program are:
- Python 
- Google API
- Google Sheets

### Resources

- GitHub 
- GitPod
- Heroku

### Libraries
[random](https://docs.python.org/3/library/random.html) - to generate random numbers.


## Future Updates

The next update of the app will include the option to choose for the user to  "Print Database"  statement of account as New option.

## Validation

PEP8 - Python style guide checker imported - https://pypi.org/project/pep8/
All code validated and where lines were showing as too long they were adjusted. Some line adjustments caused bugs in the code and it stopped working so they were left as longer lines to avoid this issue.

## Deployment

### Heroku

The Application has been deployed from GitHub to Heroku by following the steps:

1. Create or log in to your account at heroku.com
2. Create a new app, add a unique app name ( for example corri-construction-p3) and then choose your region
3. Click on create app
4. Go to "Settings"
5. Under Config Vars add the private API key information using key 'CRED' and into the value area copy the API key information added to the .json file.  Also add a key 'PORT' and value '8000'.
6. Add required buildpacks (further dependencies). For this project, set it up so Python will be on top and Node.js on bottom
7. Go to "Deploy" and select "GitHub" in "Deployment method"
8. To connect Heroku app to your Github repository code enter your repository name, click 'Search' and then 'Connect' when it shows below.
9.  Choose the branch you want to build your app from
10. If preferred, click on "Enable Automatic Deploys", which keeps the app up to date with your GitHub repository
11. Wait for the app to build. Once ready you will see the “App was successfully deployed” message and a 'View' button to take you to your deployed link.

### Branching the GitHub Repository using GitHub Desktop and gitpod
1. Go to the GitHub repository.
2. Click on the branch button in the left hand side under the repository name.
3. Give your branch a name.
4. Go to the CODE area on the right and select "Open with GitHub Desktop".
5. You will be asked if you want to clone the repository - say yes.
6. GitHub desktop will suggest what to do next - select Open code using Gitpod.



<h2>Credits</h2> 

<P>I used various youtube tutorials <a href="https://www.youtube.com/watch?v=8aW3tkIul-8&t=705s">Bro Code</a>  to find more options as to solution when i am stocked </P>
<p>I knowledged code aquired from <a href="www.codeinstitute.net"> Code Institute</a> to for my webpage.</p>

Peer-review slack channel for help trying to find any issues/break the code.

Tutor support for help with figuring out how to round numbers in typeError for int and str.

Jubril Akolade - My Code Institute Mentor for his understanding.