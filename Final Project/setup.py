#!/usr/bin/env python3
"""
Setup script for the Next Word Prediction Streamlit App
"""

import os
import sys
import subprocess

def install_requirements():
    """Install required packages"""
    print("Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Requirements installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing requirements: {e}")
        return False
    return True

def check_model_exists(model_path="./streamlit_model"):
    """Check if the fine-tuned model exists"""
    if os.path.exists(model_path):
        required_files = ["config.json", "pytorch_model.bin", "tokenizer.json"]
        existing_files = os.listdir(model_path)
        
        missing_files = []
        for file in required_files:
            if file not in existing_files:
                missing_files.append(file)
        
        if missing_files:
            print(f"⚠️ Model directory exists but missing files: {missing_files}")
            return False
        else:
            print("✅ Model files found successfully!")
            return True
    else:
        print(f"❌ Model directory '{model_path}' not found!")
        print("Please run the training script first to create the fine-tuned model.")
        return False

def create_sample_model_info(model_path="./streamlit_model"):
    """Create a sample model_info.json file if it doesn't exist"""
    info_path = os.path.join(model_path, "model_info.json")
    
    if not os.path.exists(info_path):
        print("Creating sample model_info.json...")
        
        import json
        model_info = {
            "model_type": "GPT2LMHeadModel",
            "vocab_size": 50257,
            "max_length": 512,
            "pad_token_id": 50256,
            "eos_token_id": 50256
        }
        
        with open(info_path, "w") as f:
            json.dump(model_info, f, indent=2)
        
        print("✅ Sample model_info.json created!")

def main():
    """Main setup function"""
    print("🚀 Setting up Next Word Prediction Streamlit App")
    print("=" * 50)
    
    # Check Python version
    if sys.version_info < (3, 7):
        print("❌ Python 3.7 or higher is required!")
        sys.exit(1)
    
    # Install requirements
    if not install_requirements():
        sys.exit(1)
    
    # Check if model exists
    model_exists = check_model_exists()
    
    if model_exists:
        # Create model info if missing
        create_sample_model_info()
        
        print("\n🎉 Setup complete!")
        print("\nTo run the Streamlit app:")
        print("streamlit run streamlit_app.py")
        print("\nThe app will open in your default web browser.")
        
    else:
        print("\n📝 Next steps:")
        print("1. Run the training script to create the fine-tuned model")
        print("2. Ensure the model is saved in './streamlit_model' directory")
        print("3. Run 'streamlit run streamlit_app.py' to start the app")

if __name__ == "__main__":
    main()
