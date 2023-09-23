import rumps
import subprocess
import os

# Function to run the Breez script
def run_breez(sender):
    home_directory = os.path.expanduser("~")  # Dynamically get the home directory
    breez_home_folder = os.path.join(home_directory, "breez")  # Append the 'breez' folder to it
    
    # Full path to main.py
    main_script = os.path.join(breez_home_folder, "main.py")
    
    try:
        print("Breez is running. Press the shortcut you selected to fix the current line in any application.")
        subprocess.run(["python", main_script])  # Try running the script with Python
    except FileNotFoundError:
        try:
            subprocess.run(["python3", main_script])  # If Python failed, try Python3
        except Exception as e:
            print(f"Failed to run Breez: {e}")

# Create the menubar app
class BreezApp(rumps.App):
    def __init__(self):
        super(BreezApp, self).__init__("Breez")
        self.menu = ["Run Breez"]
        
    @rumps.clicked("Run Breez")
    def on_run(self, sender):
        run_breez(sender)

if __name__ == "__main__":
    BreezApp().run()
