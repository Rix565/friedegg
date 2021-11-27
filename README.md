# FriedEgg
An hobbyist social network written from scratch using python & Django.
## RoadMap
To see the roadmap, **<a href="/Rix565/friedegg/blob/main/docs/roadmap.md">go here.</a>** 
## Quick start
To get your FriedEgg instance up and running, you'll need:
<ul>
  <li>Python (download it <a href="http://python.org/downloads">here</a>)</li>
  <li>Django (download it with this command, once python is installed : "pip install django")</li>
  <li>If you're using a webhost : an shell access</li>
</ul>

**NOTE : This are the currently needed requirements for this build, these can (and for sure) change in the future.**

If all these requirements are met, you can continue following this guide.

### Step 1
Get the source code of the project by clicking on Code->Download zip.
Extract it on a folder.
### Step 2
Go to that folder, and go to the folder name friedegg (not friedegg_main), and open settings.py. Configure this file the way you'll like to.
### Step 2
Open your terminal (or cmd, if you're using Windows), go to the folder of the installation of your instance, and type this command:
```python manage.py makemigrations```

Once this is done, do that command :
```python manage.py migrate```

Then, finally, finish your installation by doing that command:
```python manage.py createsuperuser```

Follow the on-screen instructions.
### You're done!
If you want to start your server, type this command :
```python manage.py runserver```

If you're using an website hosting that supports Django websites, follow the instructions given by your host to start your server.
