# Smart Email Guardian: AI-Powered Spam & Phishing Detection

Ever wondered if that "urgent" email asking for your bank details is legitimate? Or if that "congratulations, you've won!" message is too good to be true? Smart Email Guardian has your back! This intelligent email scanner uses cutting-edge AI to help you identify malicious emails before they can cause any damage.

## What Does This Project Do?

Smart Email Guardian is like having a cybersecurity expert sitting right next to you, analyzing every suspicious email. The system leverages advanced machine learning to scan email content and instantly classify whether it's spam, phishing, or legitimate communication. Think of it as your personal email bodyguard that never sleeps!

The beauty of this project lies in its versatility - whether you're a developer who prefers command-line tools, a user who loves clean web interfaces, or someone building their own email security system, we've got you covered with three different ways to interact with the AI.

## Key Features

**🤖 AI-Powered Detection**: Built on the robust `mrm8488/bert-tiny-finetuned-sms-spam-detection` model from Hugging Face, our system understands the subtle patterns that make malicious emails tick.

**💻 Command-Line Interface**: Perfect for developers and power users who want quick, scriptable email analysis.

**🌐 Web Interface**: A beautiful, user-friendly Streamlit frontend that anyone can use - just paste and scan!

**🔌 RESTful API**: Clean, well-documented API endpoints for integrating email scanning into your own applications.

## Technologies That Power the Magic

This project brings together some of the best tools in the Python ecosystem:

- **Python 3.8+**: The backbone of our entire system
- **Flask**: Powers our lightweight yet robust API backend
- **Streamlit**: Creates our intuitive web interface
- **Hugging Face Transformers**: Gives us access to state-of-the-art AI models
- **BERT**: The brain behind our email analysis capabilities

## Getting Started - Let's Build This Together!

### Prerequisites

Before we dive in, make sure you have:
- **Python 3.8 or higher** installed on your system
- **pip** package manager (usually comes with Python)

### Step 1: Clone the Repository

First, let's get the code onto your machine:

```bash
git clone https://github.com/yourusername/email_guard.git
cd email_guard
```

### Step 2: Set Up Your Virtual Environment

Creating a virtual environment is crucial - it keeps your project dependencies isolated and prevents conflicts with other Python projects:

```bash
python -m venv venv
```

Now activate it:

**On Windows:**
```bash
.\venv\Scripts\activate
```

**On macOS/Linux:**
```bash
source venv/bin/activate
```

You'll know it worked when you see `(venv)` at the beginning of your command prompt!

### Step 3: Install Dependencies

This is where the magic happens - we'll install all the required packages:

```bash
pip install -r requirements.txt
```

*Note: The first time you run the application, it will download the AI model automatically. This might take a few minutes depending on your internet connection, but it's a one-time setup.*

## Running the Application Locally

Here's where things get exciting! We're going to run three components that work together seamlessly.

### Step 1: Fire Up the Backend API

The API is the heart of our system - it's where all the AI processing happens.

1. **Open a new terminal window**
2. **Navigate to your project directory and activate the virtual environment**
3. **Set the Flask application variable:**

   **Windows (PowerShell):**
   ```bash
   $env:FLASK_APP="backend.app"
   ```
   
   **Windows (Command Prompt):**
   ```bash
   set FLASK_APP=backend.app
   ```
   
   **macOS/Linux:**
   ```bash
   export FLASK_APP=backend.app
   ```

4. **Launch the Flask server:**
   ```bash
   flask run
   ```

You should see something like `Running on http://127.0.0.1:5000`. **Keep this terminal open** - this is your API server running!

### Step 2: Launch the Streamlit Frontend

Now for the beautiful web interface that makes everything user-friendly.

1. **Open another new terminal window**
2. **Navigate to your project directory and activate the virtual environment**
3. **Start the Streamlit app:**
   ```bash
   streamlit run frontend\app.py
   ```

Streamlit will automatically open your default browser and navigate to the app (usually at `http://localhost:8501`). If it doesn't open automatically, just click the URL shown in the terminal.

### Step 3: Test the CLI Tool (Optional but Fun!)

Want to see the AI in action from the command line? Let's test it:

1. **Open a third terminal window**
2. **Navigate to your project directory and activate the virtual environment**
3. **Try analyzing a suspicious email:**
   ```bash
   python ai/email_guard.py "Claim your free prize now! Click here immediately!"
   ```

Watch as the AI quickly identifies this as spam!

## How to Use the Web Interface

Using Smart Email Guardian is incredibly straightforward:

1. **Open the Streamlit app** (it should be running in your browser)
2. **Paste any email text** into the text area - this could be the subject line, body content, or both
3. **Click the "Scan Email" button**
4. **Get instant results** with confidence scores and explanations

The interface is designed to be intuitive - even your grandmother could use it to check suspicious emails!

## Project Structure - Understanding the Architecture

Here's how the project is organized, and why each component matters:

- **`ai/`**: The brain of the operation - contains our core AI model and email classification logic
- **`backend/`**: Houses our Flask API that serves the AI functionality to other components
- **`frontend/`**: The beautiful Streamlit web interface that users interact with
- **`docs/`**: Comprehensive documentation and guides (because good docs save lives!)
- **`tests/`**: Test suites to ensure everything works perfectly (we believe in quality!)

## Deployment (Coming Soon!)

We're working on making Smart Email Guardian available online so you can use it anywhere, anytime. Once deployed, you'll be able to access:

- **Live Web Application**: [Streamlit Cloud URL coming soon]
- **Public API Endpoint**: [Render/Heroku URL coming soon]

Stay tuned for updates!

## Contributing

Found a bug? Have an idea for a new feature? We'd love your input! This project thrives on community contributions, whether it's code improvements, documentation updates, or simply sharing your experience using the tool.

## Why This Project Matters

In an era where email-based attacks are becoming increasingly sophisticated, having an accessible, AI-powered detection tool isn't just convenient - it's essential. Smart Email Guardian democratizes advanced cybersecurity, putting enterprise-level email protection in the hands of everyone.

Whether you're protecting your family from phishing scams, securing your small business communications, or learning about AI applications in cybersecurity, this project serves as both a practical tool and an educational resource.

---
