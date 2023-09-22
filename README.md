# breez

## what is breez
1. Selects the current line in the currently active application anywhere on macOS (Apple Notes, Gmail, Notion, Obsidian...)
2. Grammar fixes the sentence using GPT 3.5 Turbo
3. Pastes the selection

All of this happens by just tapping a single shortcut, so you can focus on the thoughts you want to convey instead of fixing typos!
It works much better than traditional autocorrection as it fixes a sentence within its complete context.


[![Demo Video](https://img.youtube.com/vi/A49u4Lu2meU/0.jpg)](https://www.youtube.com/watch?v=A49u4Lu2meU)
[Video Link](https://www.youtube.com/embed/A49u4Lu2meU?si=RDgcsnZ5riG8DfMT)

## roadmap
- Shortcut for offline dictation using Whisper
- Offline LLM running on macOS
- Windows support

## install
1. Clone the repository into **the root of your home folder**
	1. Should look like this:
	2. ![600](https://i.imgur.com/BSKXrBs.png)
2. In the **dist** folder right click on **1_install_packages** and click on "Open" - to install the required packages on your computer
	1. ![](https://i.imgur.com/7HhRX4q.gif)
	2. You can then close the terminal window
3. Next right click on the **2_create_config** script and click on "Open" again
	1. When the script ask you if you want to enter a new OpenAI api key press `y` on the keyboard and then `Enter`
	2. Paste your OpenAI API Key which you can find here https://platform.openai.com/account/api-keys
	3. If you dont have an API Key yet, create one ![](https://i.imgur.com/jiQyTjr.png)
	4. Copy the Key ![](https://i.imgur.com/Ka9Apse.png)
4. Finally select the shortcut you want to use to execute Breez - right now you can choose between `CMD + .`,  `CMD + :` and `F10` ![](https://i.imgur.com/a6PB9XL.gif)
5. Open the Breez folder again and right click on **3_run_breez**, then click on "Open with Terminal" ![](https://i.imgur.com/WhQ9urU.gif)
	1. Don't close this terminal window - so that breez can run in the background.
6. When you now trigger Breez for the first time by pressing the shortcut you selected, you will see the following window.
	1. ![](https://i.imgur.com/cO3SttJ.png)
	2. Open System Settings and check the checkbox for terminal
	3. ![](https://i.imgur.com/9viKts6.png)
	4. You will also need to **Quit & Reopen** the terminal now
		1. ![](https://i.imgur.com/oHUF48Q.png)
		2. ![](https://i.imgur.com/B80XZoY.png)
\begin{align*}
7. As the final step, you now need to enable Accessibility in the privacy options of the terminal.
\end{align*}
	1. Go to settings and click on **Privacy & Security** ![](https://i.imgur.com/gldNjbF.png)
	2. Click on **Accessibility** ![](https://i.imgur.com/vW5jpjK.png)
	3. Checkmark the **Terminal** ![](https://i.imgur.com/de6UdIY.png)
8. **Close all previous terminal windows** - then run Breez by right-clicking and opening the **run_breez** file
	1. ![](https://i.imgur.com/Z4qWjhi.png)

You are able to use Breez with your selected shortcut now. Enter a note-taking application and try it out.

If you want to run Breez at autostart check this out: [How to run a python script on login using pyautostart for macOS | by Aero Byte | Medium - aerobyte.medium.com/](https://aerobyte.medium.com/how-to-run-a-python-script-on-login-using-pyautostart-for-macos-539a4384a240)
