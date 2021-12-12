# Python Functional Testing
This project has a collection of Web UI tests, and API tests using **pytest**.  
For documentation on **pytest**, visit https://docs.pytest.org/en/6.2.x/getting-started.html.

## Installation

* Install the latest *python* version  
  For Mac OSX - using *homebrew*  
  `brew update`  
  `brew install python`  
  `python --version`  
  `brew info python`  this should display the latest python version installed. If the latest version installed does not match with the *python --version* copy the path of the latest python and update the PATH.  
  For example,
  > Unversioned symlinks `python`, `python-config`, `pip` etc. pointing to
`python3`, `python3-config`, `pip3` etc., respectively, have been installed into
  /usr/local/opt/python@3.9/libexec/bin  

  add the path to the .zshrc file 
  ```
  export PATH=/usr/local/opt/python@3.9/libexec/bin:$PATH
  ```  
* Clone the repo  
  `git clone [url]`
   
* Install *pytest*  
  `pip install -U pytest`  
  `pytest --version`
* Install the other dependencies with *-U* switch to *Upgrade* if exists
  `brew cask install chromedriver`  
  `pip install -U selenium`  
  `pip install -U requests`  
  or run the *requirements.txt*  
  `pip install -r requirements.txt`

  
## Running Tests
`pytest`
`pytest -s` to show output