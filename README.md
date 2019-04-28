# PeekABoo
PeekABoo tool can be used during internal penetration testing when a user needs to enable Remote Desktop on the targeted machine. It uses PowerShell remoting to perform this task. 

Note: Remote desktop is disabled by default on all Windows operating systems. User would require local administrator password or administrator privileges on the server to enable RDP on a targeted machine.

Any suggestions or ideas for this tool are welcome - just tweet me on [@ManiarViral](https://twitter.com/maniarviral)

# Screenshots

Targeted machine on an internal network has RDP disabled:

![image](https://user-images.githubusercontent.com/3501170/56864171-968fdc00-6a02-11e9-94cd-3baff007850b.png)

Enabling remote desktop service on a targeted machine by pressing:

![image](https://user-images.githubusercontent.com/3501170/56864277-e0c58d00-6a03-11e9-81b4-0b2d1de715be.png)

Successfully enabled remote desktop service on a targeted machine:

![image](https://user-images.githubusercontent.com/3501170/56864731-2f295a80-6a09-11e9-8bf2-7bcef805b577.png)

# How to install?
<pre>
- git clone https://github.com/Viralmaniar/PeekABoo.git
- cd PeekABoo
- python peekaboo.py
</pre>

# How do I use this?
- Press 1: This will set the PowerShell to unrestricted mode.
- Press 2: It enables the `Remote Desktop` on the targeted machine and shows the RDP port (3389) status.
- Press 3: It disables the `Remote Desktop` on the targeted machine.
- Press 4: To exit from the program.

# My Windows machine do not have Python installed, what should I do?

- Download an exe from the release section of the Github along with PowerShell files available [here](https://github.com/Viralmaniar/PeekABoo/releases) or do it on your own using PyInstaller after reviewing the source code.

- Compile `peekaboo.py` into an executable using [Pyinstaller](https://github.com/pyinstaller/pyinstaller)

- PyInstaller is available on PyPI. You can install it through pip:

<pre>
pip install pyinstaller
</pre>

# Questions?

Twitter: https://twitter.com/maniarviral <br>
LinkedIn: https://au.linkedin.com/in/viralmaniar

# Contribution & License

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/80x15.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.</br>
Want to contribute? Please fork it and hit up with a pull request.

Any suggestions or ideas for this tool are welcome - just tweet me on [@ManiarViral](https://twitter.com/maniarviral)
