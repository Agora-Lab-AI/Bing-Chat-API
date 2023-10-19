# Bing API Documentation

[![Multi-Modality](agorabanner.png)](https://discord.gg/qUtxnK2NMf)

## Bing API

A radically simple Bing API for both text and image completions using ChatGPT-4 and DALL-E 3.

## Installation 🐠
---------------

You can install the Bing API using pip:

```
pip3 install --upgrade bingapi
```

## Usage 🐡
--------

Here's a simple example of how to use the Bing API for DALL-E 3:

```python
import logging
from bingapi import Dalle

# Define cookie using env or empty string
cookie = ""

# Set up logging
logging.basicConfig(level=logging.INFO)

# Instantiate the Dalle class with your cookie value
dalle = Dalle(cookie)

# Open the website with your query
dalle.create(
    "Fish hivemind swarm in light blue avatar anime in zen garden pond concept art anime art, happy fish"
)

# Get the image URLs
urls = dalle.get_urls()

# Download the images to your specified folder
dalle.download(urls, "images/")
```

## `Dalle` Documentation

### Table of Contents

1. [Introduction](#introduction)
2. [Dalle Class](#dalle-class)
   - [Initialization Parameters](#initialization-parameters)
3. [Methods and Usage](#methods-and-usage)
   - [get_time Method](#get-time-method)
   - [get_time_save Method](#get-time-save-method)
   - [download Method](#download-method)
   - [create Method](#create-method)
   - [get_urls Method](#get-urls-method)
   - [run Method](#run-method)
4. [Examples](#examples)
   - [Example 1: Creating a Dalle Instance](#example-1-creating-a-dalle-instance)
   - [Example 2: Running the Whole Process](#example-2-running-the-whole-process)
5. [Additional Information](#additional-information)
6. [References and Resources](#references-and-resources)

(And so on...)

## Features 🌊
-----------

- **Easy to Use**: With just a few lines of code, you can start generating images or text completions.
- **Customizable**: Provide your own creative prompts to generate unique images or text completions.
- **Automated Download**: The API automatically downloads the generated images to your specified folder.
- **Real-Time Updates**: The API provides real-time logging information about the generation and download process.

## License 📜
----------

Bing API is licensed under the MIT License. See the [LICENSE](https://domain.apac.ai/LICENSE) file for more details.

## Todo

- [ ] Add Automatic cookie finding seamlessly
- [ ] Automatically upgrade browser versions
- [ ] Add automatic browser detection, cross-browser support
- [ ] Simplify endpoints for ease of use
- [ ] Integrate GPT-4 vision API using a similar approach
- [ ] Establish Idea2Image Documentation
- [ ] Create tests for Idea2Image
- [ ] Implement human feedback loop for Idea2Image
- [ ] Support different output types (svg, jpg)
- [ ] Integrate BingChat API
- [ ] Integrate ChatGPT Dalle API
- [ ] Develop ChatGPT V API

This documentation provides a comprehensive guide on how to interact with the Bing API, leveraging both ChatGPT-4 and DALL-E 3 capabilities for text and image completions.
