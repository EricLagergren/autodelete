autodelete
==========

Goes through a directory and searches for files older than a specific date and deletes them

<h1> Overview: </h1>
<p>Simply 'walks' through the specified folder and deletes files (recursively) that are older than the specified date.

<h1> Instructions: </h1>
<h3> Requires: </h3>
<ul>
<li>os module</li>
<li>sys module</li>
<li>sh module</li>
<li>datetime module</li>
</ul>
<p>The script uses Python3. You'll find the 'path' variable about halfway through the file. Edit it to the correct path, and then run the script. Best used as a cron job. This script will want to write to an error log called 'autodelete.log', and it will try to place said log in /var/log/. You can edit this, but make sure that you either run the script as root (preferably with `sudo`) or use `chmod` so that the log file is writable.

<h1> To Install: </h1>

`git clone https://www.ericlagerg/autodelete`
<p>
`mv /path/to/autodelete/autodelete.py /where/you/want/the/script`
<p>
`sudo python3 ./autodelete.py`
<p><b>OR</b>
`touch /var/log/autodelete.log && chmod 666 autodelete.log`
