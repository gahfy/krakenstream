# KrakenCLI

This is a Python module for interacting with Kraken's REST and WebSocket APIs.

## Usage

### Setting Up API Credentials

To use kraken-python, you need to provide your API credentials through environment variables. For security reasons, using a .env file is not allowed.

Set the following environment variables in your terminal:

- **KRAKEN_PYTHON_API_KEY**: Your Kraken API key.
- **KRAKEN_PYTHON_API_SECRET**: Your Kraken API secret.

To set them in your terminal (Linux/macOS):

```bash
export KRAKEN_PYTHON_API_KEY="your_api_key_here"
export KRAKEN_PYTHON_API_SECRET="your_api_secret_here"
```

On Windows (Command Prompt):

```cmd
set KRAKEN_PYTHON_API_KEY="your_api_key_here"
set KRAKEN_PYTHON_API_SECRET="your_api_secret_here"
```

## Contributions

All contributors are welcome! Since we are still in the early stages of development, we will be writing a guide about contributing soon.

In the meantime, just make sure you fork the repo, run the tests, and ensure that coverage is not reduced.

We understand that this process may be frustrating, especially for those making the effort to raise a PR and receiving unexpected comments. Once we have a proper guide, these issues should be mitigated. If you're not comfortable with this for now, it's perfectly okay to hold off on contributing.