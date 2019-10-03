# bedrock-server-backup
Some python code that uses subprocess to backup my bedrock server every couple of hours
Previously I had been using pyautogui to type into the server console save hold and save resume, and then os.system to run a batch file that would copy the files.
Now, I wrote something new using subprocess so that I wouldn't have to be in the server console window all the time.
