# Python-Programming
Basic Python Programming

To install any library from internet will get the command. To execute that command from pycharm we can execute.

1.Exception Handling :
https://docs.python.org/3/tutorial/errors.html
https://docs.python.org/3/library/exceptions.html
__________________________________________________________________________

1. What are branches 
2. How to create branch
3. How to checkout branch
4. How to merge branch to master
5. How to delete branch (local and remote)
_________________________________________

1. What are branches 
=> Whenever want to do some changes in code or created some new feature, better not to do any changes on main/master branch.
   Recomanded to create a new branch and checkout that branch,make all the changes in that branch. After testing and validating that everything is fine
   marge those changes to main/master branch.

Step 1 : Create branch 
   git branch “branch name”

Step 2 : Checkout branch
   git checkout “branch name”

Step 3 : Merge new branch in master branch
   git merge “branch name”
   
Step 4: Push file to new branch
   git push -u origin "new branch name"

Step 5 : Delete branch
   git branch -d “branch name”    — delete from local
   git push origin —delete “branch name”   — delete from remote
