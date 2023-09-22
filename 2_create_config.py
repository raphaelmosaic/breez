import json
import os

def load_config():
    # Updated path to point to the breez directory
    config_dir = os.path.expanduser('~/breez')    
    if not os.path.exists(config_dir):
        os.makedirs(config_dir) 
    config_path = os.path.join(config_dir, 'config.json')
    
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            content = f.read().strip()  # Read and remove leading/trailing whitespaces
            if content:  # Check if the file is empty
                return json.loads(content)
            else:
                print("Warning: Config file is empty.")
                return None
    else:
        return None

def save_config(config_data):
    # Updated path to point to the breez directory
    config_dir = os.path.expanduser('~/breez')
    if not os.path.exists(config_dir):
        os.makedirs(config_dir)
    config_path = os.path.join(config_dir, 'config.json')

    with open(config_path, 'w') as f:
        json.dump(config_data, f)

def configure_app():
    config_data = load_config() or {}
    
    # Get OpenAI API Key
    enter_new_key = input("Do you want to enter a new OpenAI API Key? (y/n): ").lower() == 'y'
    if enter_new_key:
        config_data["api_key"] = input("Enter your OpenAI API Key: ")

    # Get hotkey configuration
    hotkey_options = ["CMD + .", "CMD + :", "F10"]
    print("\nSelect a hotkey:")
    for idx, option in enumerate(hotkey_options):
        print(f"{idx + 1}. {option}")
    selected_index = int(input("\nEnter the number of your choice: ")) - 1
    config_data["hotkey"] = hotkey_options[selected_index]

    # Save to JSON
    save_config(config_data)

if __name__ == "__main__":
    configure_app()
