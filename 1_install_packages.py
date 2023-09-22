import subprocess

def install_packages():
    try:
        subprocess.run(["pip", "install", "requests", "pynput", "pyperclip"])
    except Exception:
        try:
            subprocess.run(["pip3", "install", "requests", "pynput", "pyperclip"])
        except Exception as e:
            print(f"Failed to install packages: {e}")
            return
    print("-" * 50)
    print("All requirements installed. Continue with creating config.")
    print("-" * 50)

if __name__ == "__main__":
    install_packages()
