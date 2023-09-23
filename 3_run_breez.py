import subprocess
import os

def run_breez():
    # Dynamically get the home directory
    home_directory = os.path.expanduser("~")
    
    # Append the 'breez' folder to it
    breez_home_folder = os.path.join(home_directory, "breez")
    
    # Full path to main.py (You might want to change this to run a different script)
    main_script = os.path.join(breez_home_folder, "main.py")
    
    try:
        print("Breez is running. Press the shortcut you selected to fix the current line in any application.")
        
        # Try running the script with Python
        subprocess.run(["python", main_script])
    except FileNotFoundError:
        try:
            # If Python failed, try Python3
            subprocess.run(["python3", main_script])
        except Exception as e:
            print(f"Failed to run Breez: {e}")

if __name__ == "__main__":
    run_breez()
