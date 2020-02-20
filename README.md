# Email Keep

A Python script that I wrote for sending the contents of a Google Keep list to an email address using the unofficial Google Keep API: "gkeepapi". Fill in the email and password for the account you want to use next to the empty variables in the Python script.

**Note: This method of storing the password instead of taking it as input every time is not secure, and probably shouldn't be done on a device without encryption and a solid password. I don't have any other options (to my knowledge, please let me know if you've got any suggestions) because I run mine using the Termux:Tasker plugin which is triggered by the Autovoice plugin on a tablet that I use for home control.**

If you are also using this with the Termux:Tasker plugin make sure you have Python and the gkeepapi installed, then place the Python script in the root of your Termux directory, create the required directory using  the command `mkdir -p ~/.termux/tasker` and place the shell script in that folder.
