# CMPT 370 Project

**Instruction file for OMAS**

###Frontend
Currently, the frontend just displays an interactive interface for the user to work with, but is not linked with the backend.

How to run-
  - If you're running the application for the first time, right-click and run 'frontend/first_time.ps1' with PowerShell. This will automatically install node_modules and create a build.
  - For running it again, right-click and run 'frontend/run_regular.ps1' with PowerShell.

###Backend
Backend is almost fully implemented. We only need to implement database analysis algorithms and set up integration.

How to run-
- Just run 'backend/Main.py'. (I recommend using an IDE, since it has a lot of dependencies. We tried to package it, need to work on that a bit more)
- Note- If the server does not run, you need to install Django using `python -m pip install Django` (you also need to install Python)

___

### User stories targeted in this deliverable
1. Ability to track attendees and absentees
2. Ability to get the duration for which the attendees stayed in the meeting
3. Functionality to log reports into an external database (Excel workbook)
4. Ability to provide reports in a simple text file
5. Provide ability to autocorrect misspelled participant names

### User stories targeted for the next deliverable
1. Provide a meaningful visual representation of the processed records
2. Provide hints & suggestions through the entire process
3. Ability to revert changes (to a certain extent)
4. Provide an easy-to-use interface using color coding & specific arrangement of buttons
5. Provide visual cues for changes (alerts & change of button colors)