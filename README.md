CS223P - Python Programming

Author Name: Kathy Saad<br>
Project Title: Project 7 - RDB, Python Virtual Environments, PyPi, pip<br>
Project Status: Working<br>
External resources:<br>
- Class notes and handouts<br>
- https://www.snipplr.com/view/49167/<br>
- https://www.pypi.python.org/pypi/twitter/1.10.0/<br>
- https://www.pypi.python.org/pypi/twitter/1.15.0/<br>
- https://www.python.org/

*******************************************************************************************************************************************

Instructions:

The final exercise is to write a program named tweet-a-fortune.py. You must make a directory with this project which includes at least 5 images that you have the rights to use (i.e. take your own pictures). The program generates a random number using the random module, selects a fortune from the fortune database given the random number, verifies the text is less than 140 characters - if not it finds another random aphorism until it's length is less than 140 characters, then randomly selects one of the images you have included in your project and tweets this message to your Twitter account. (Students who finish early should look at how to tweet images from flickr.com)

*******************************************************************************************************************************************

https://twitter.com/KatProgramming

*******************************************************************************************************************************************

kat@ubuntu:~/Desktop/tweetafortune$ source env/bin/activate
(env)kat@ubuntu:~/Desktop/tweetafortune$ python3.4 tweet-a-fortune.py freebsd_fortunes_clean.sl3
(env)kat@ubuntu:~/Desktop/tweetafortune$ pip freeze > requirements.txt
(env)kat@ubuntu:~/Desktop/tweetafortune$ cat requirements.txt
twitter==1.15.0
(env)kat@ubuntu:~/Desktop/tweetafortune$ deactivate
(env)kat@ubuntu:~/Desktop/tweetafortune$ ls
1.jpg  3.jpg  5.jpg  env                         tweet-a-fortune.py
2.jpg  4.jpg  6.jpg  freebsd_fortunes_clean.sl3