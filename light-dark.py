#!/usr/bin/env python3.7

import iterm2
import os
import time

async def main(connection):
    # Configure profiles for light and dark mode
    lightProfile = ""
    darkProfile = ""

    while (True):
        # Check if macOS is currently in light or dark mode
        AppleInterfaceStyle = os.popen("defaults read -g AppleInterfaceStyle 2> /dev/null || echo 'Light' ").read().partition('\n')[0]

        # Decide which profile to use
        newProfile = lightProfile
        oldProfile = darkProfile
        if (AppleInterfaceStyle == "Dark"):
            newProfile = darkProfile
            oldProfile = lightProfile

        # Get partial profile for the current default profile
        currentDefaultProfile = await iterm2.PartialProfile.async_get_default(connection)

        # Make changes only if the default profile is not already set to what we want it to be,
        # as that uses less resources then also going through all sessions every time this is run,
        # and that means we can check more often.
        if (currentDefaultProfile.name != newProfile):
            app = await iterm2.async_get_app(connection)

            # Get partial profiles first
            partialProfiles = await iterm2.PartialProfile.async_query(connection)
            
            # Go through all profiles
            for partial in partialProfiles:

                # If this profile is the one we want to change to
                if partial.name == newProfile:
                    
                    # Get full profile
                    profile = await partial.async_get_full_profile()

                    # Set this profile as default
                    await profile.async_make_default()

                    # Set this profile for all sessions in all tabs in all windows
                    for window in app.terminal_windows:
                        for tab in window.tabs:
                            for session in tab.sessions:
                                # Check this session's current profile and ignore sessions that are maually set to something different then the default
                                sessionProfile = await session.async_get_profile()
                                if (sessionProfile.name == oldProfile):
                                    # Change to the new profile for this session
                                    await session.async_set_profile(profile)
        # Check again in 5 seconds
        time.sleep(5)

iterm2.run_until_complete(main)
