# iTerm2 Automatic Light/Dark Profile Switcher
This is an iTerm2 script for automatically changing between a light and a dark profile for all tabs and windows when macOS 10.14+ is switched between light and dark mode.

# Installation and Usage
- First get iTerm2 (the best terminal emulator there is!), as you obviously don't have much use for this script without that :) Get it here: https://iterm2.com
- Launch iTerm2 and install it's Python runtime from the Scripts menu
- Go to iTerm2's preferences, and to General, and then the Magic tab, and enable the Python API there
- Put light-dark.py in $HOME/Library/ApplicationSupport/iTerm2/Scripts/AutoLaunch/ (you may need to create the AutoLaunch folder)
- Decide on iTerm2 profiles you think works well with light and with dark mode in macOS
- Edit light-dark.py and put the names of your light and dark profiles in the variables lightProfile and darkProfile on top of the file
- Relaunch iTerm2, and it will now automatically change between your light and dark profiles when you switch between light and dark mode in macOS
- Only sessions/tabs that is set to one of your configured profiles will be changed when you switch between modes, so if you start a session with another profile, it will keep that profile even when you change the light/dark mode in macOS
- If you change the configured light or dark profiles in light-dark.py, you will need to relaunch iTerm2 for that change to take effect