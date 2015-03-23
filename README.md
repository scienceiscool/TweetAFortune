#CPSC 223P - Python Programming

__Author Name:__ Kathy Saad<br>
__Project Title:__ Project 7 - RDB, Python Virtual Environments, PyPi, pip<br>
__Project Status:__ Working<br>
__External resources:__<br>
- Class notes and handouts<br>
- https://www.snipplr.com/view/49167/<br>
- https://www.pypi.python.org/pypi/twitter/1.10.0/<br>
- https://www.pypi.python.org/pypi/twitter/1.15.0/<br>
- https://www.python.org/

*******************************************************************************************************************************************

__Instructions [for tweet-a-fortune.py]:__

The final exercise is to write a program named tweet-a-fortune.py. You must make a directory with this project which includes at least 5 images that you have the rights to use (i.e. take your own pictures). The program generates a random number using the random module, selects a fortune from the fortune database given the random number, verifies the text is less than 140 characters - if not it finds another random aphorism until it's length is less than 140 characters, then randomly selects one of the images you have included in your project and tweets this message to your Twitter account. (Students who finish early should look at how to tweet images from flickr.com)

Note: Instructions for other two files are within those files.

*******************************************************************************************************************************************

Twitter account used: https://twitter.com/KatProgramming

*******************************************************************************************************************************************

$ source env/bin/activate<br>
(env)$ python3.4 tweet-a-fortune.py freebsd_fortunes_clean.sl3<br>
(env)$ pip freeze > requirements.txt<br>
(env)$ cat requirements.txt<br>
twitter==1.15.0<br>
(env)$ deactivate<br>
(env)$ ls<br>
1.jpg  3.jpg  5.jpg  env  tweet-a-fortune.py<br>
2.jpg  4.jpg  6.jpg  freebsd_fortunes_clean.sl3<br>
