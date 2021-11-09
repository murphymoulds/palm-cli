## Palm CLI: The extensible CLI at your fingertips

_Palm_ is a universal CLI developed to improve the life and work of data professionals. 

[What is Palm?](https://www.loom.com/share/88903b106e724221b5d45b8dc27270de)

### Installing Palm

1. You will need [Docker](https://docs.docker.com/get-docker/)
   You can check to see if you already have it with `docker --version`

2. You will need [Python3](https://www.python.org/downloads/) 
   You can check to see if you already have it with `python3 --version`

**Fastest Method: Using Pip**
Run this from the command line:
```
python3 -m pip uninstall palm || true
python3 -m pip install git+https://github.com/palmetto/palm-cli.git
```
It will ask you to log into Github, and then `palm` will be installed

**If you have the repo on your computer** 
This will install whatever version you have checked out at the moment.

```
cd path/to/this/repo &&
python3 -m pip uninstall palm || true # for new installs
python3 -m pip install . 
```

You can verify the install with
```
palm --help
```

*note for mac users*: if you get this warning:
```
  WARNING: The script palm is installed in '/Users/yourname/Library/Python/3.8/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  ```
you will need to add `'/Users/yourname/Library/Python/3.8/bin'` to your path for `palm` to work. 

you can do that with this command:
```
echo "\nexport PATH=$PATH:/Users/yourname/Library/Python/3.8/bin\n" >> ~/.zprofile
```


### Setting up Palm
Now that it is installed, create an `.env` file in the root of your dbt project(s) by copying the existing `.env.template` file.

You can either set the specified environment variables in the `.env` file or hardcode values directly in there (`.env` is not in source control for that reason).

You are now all set to use palm!
