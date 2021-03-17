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
   
 ******************What is the difference between append and extend in python.****************************
=>Append: Adds its argument as a single element to the end of a list. The length of the list increases by one.

my_list = ['geeks', 'for'] 
my_list.append('geeks') 
print my_list
Output:
['geeks', 'for', 'geeks']
NOTE: A list is an object. If you append another list onto a list, the parameter list will be a single object at the end of the list.
my_list = ['geeks', 'for', 'geeks'] 
another_list = [6, 0, 4, 1] 
my_list.append(another_list) 
print my_list 
Output:
['geeks', 'for', 'geeks', [6, 0, 4, 1]]

extend(): Iterates over its argument and adding each element to the list and extending the list. The length of the list increases by number of elements in its argument.
my_list = ['geeks', 'for'] 
another_list = [6, 0, 4, 1] 
my_list.extend(another_list) 
print my_list 
Output:
['geeks', 'for', 6, 0, 4, 1]
A string is an iterable, so if you extend a list with a string, you’ll append each character as you iterate over the string.
my_list = ['geeks', 'for', 6, 0, 4, 1] 
my_list.extend('geeks') 
print my_list 
Output:
['geeks', 'for', 6, 0, 4, 1, 'g', 'e', 'e', 'k', 's']

