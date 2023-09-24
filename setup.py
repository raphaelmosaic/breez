from cx_Freeze import setup, Executable

# Build options
build_options = {
    'packages': ['rumps', 'subprocess', 'os'],  # Include any other dependencies you have
    'excludes': []
}

# Executables
executables = [
    Executable("/Users/rv/breez/breez-runner.py", target_name="BreezApp")
]

# Main setup
setup(
    name="Breez",
    version="1.0",
    description="Typing made effortless",
    options={'build_exe': build_options},
    executables=executables
)
