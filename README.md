# Bing Chat API Documentation

[![Multi-Modality](agorabanner.png)](https://discord.gg/qUtxnK2NMf)

## Bing Chat API

An all-inclusive API endpoint that harnesses the power of ChatGPT-4 for text completions, GPT-4 Vision for vision tasks, and DALL-E 3 for image creation. This comprehensive API is designed to provide a seamless experience for users looking to integrate advanced AI capabilities into their applications. Future integrations will include Windows Copilot, offering a way to control Windows in a manner similar to open-interpreter.

## Installation 🐠
---------------

You can install the Bing Chat API using pip:

```
pip3 install --upgrade bingchatapi
```

## Usage 🐡
--------

### ChatGPT-4 Usage:

```python
import logging
from bingchatapi import BingChat

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    chat = BingChat("")
    initial_message = "Hello, Bing!"
    messages = chat.run(initial_message)
    print("Chat history:", messages)
```

**Disclaimer**: Using this API excessively or in ways that violate Bing's terms of service may result in your account being banned. Always ensure you're adhering to platform guidelines and use the API responsibly.

## BingChat Documentation

### Table of Contents

1. [Introduction](#introduction)
2. [BingChat Class](#bingchat-class)
   - [Initialization Parameters](#initialization-parameters)
3. [Methods and Usage](#methods-and-usage)
   - [run Method](#run-method)
4. [Examples](#examples)
   - [Example 1: Creating a BingChat Instance and Running a Chat Session](#example-1-creating-a-bingchat-instance-and-running-a-chat-session)
5. [Additional Information](#additional-information)
6. [References and Resources](#references-and-resources)

(And so on...)

## Features 🌊
-----------

- **Easy to Use**: With just a few lines of code, you can start generating text completions.
- **Customizable**: Provide your own creative prompts to generate unique text completions.
- **Real-Time Updates**: The API provides real-time logging information about the chat session.
- **Multimodal Capabilities**: The API integrates ChatGPT-4 for text, GPT-4 Vision for vision tasks, and DALL-E 3 for image creation, offering a wide range of functionalities in a single endpoint.
- **Future Windows Copilot Integration**: Upcoming features will allow users to control Windows functionalities, making it a versatile tool for various applications.
- **Future voice activation for sending prompts
- 
## License 📜
----------

Bing Chat API is licensed under the MIT License. See the [LICENSE](https://domain.apac.ai/LICENSE) file for more details.

## Todo

- [ ] Add Automatic cookie finding seamlessly
- [ ] Simplify endpoints for ease of use
- [ ] Integrate more advanced features of ChatGPT-4
- [ ] Create tests for BingChat
- [ ] Implement human feedback loop for improved chat sessions
- [ ] Support different output formats
- [ ] Develop integration with Windows Copilot for enhanced control over Windows functionalities
- [ ] Develop voice activation for sending prompts 

This documentation provides a comprehensive guide on how to interact with the Bing Chat API, leveraging the combined capabilities of ChatGPT-4, GPT-4 Vision, and DALL-E 3.
