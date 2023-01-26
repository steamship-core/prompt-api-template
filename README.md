# Overview
This is a basic Replit template for building a [Steamship](https://steamship.com) package for prompt-based text generation.

## Quick Start

To get started, Click `Use Template` from the [template page](https://replit.com/@steamship/Steamship-Prompt-App-Template?v=1) in Replit.

To run it:
1. Get a Steamship API Key (Visit: [https://steamship.com/account/api](https://www.steamship.com/account/api)). If you do not
   already have a Steamship account, you will need to create one.
1. Copy this key to a [Replit Secret](https://docs.replit.com/programming-ide/storing-sensitive-information-environment-variables) named `STEAMSHIP_API_KEY`.
1. Click the green `Run` button at the top of the window (or open a new Shell and type `python3 api.py`).

# Prompt-based Text Generation

This template provides a simple mechanism to generate text based on a supplied prompt. The prompt can ask for any kind of text to be generated, including poems, letters, Twitter responses, LinkedIn posts, jokes, etc. The prompt can be customized based on user input, allowing your users to generate personalized text.

## Running the generator

### Prerequisites

You will need a [Steamship](https://steamship.com) Account and an associated API Key. With an account, an API Key can be obtained
via the website ([https://www.steamship.com/account/api](https://www.steamship.com/account/api)).

You will need to create a Replit Secret for `STEAMSHIP_API_KEY` with your Steamship API key. 

### Local test/development

To run the package locally, use the provided `Run` button in Replit (or open a new Shell and type `python3 api.py`).

### Production deployment

Once you are satisfied with your prompt, you may deploy it to Steamship in order to create running instance(s) and a demo application.

First, ensure that you have descriptive package handle for your package in `steamship.json` (defaults to `my-prompt-package`). This handle will be used by Steamship to refer to your package internally and externally. It must be globally-unique, so you may need to try a few before finding one that is unclaimed.

To deploy it on [Steamship](https://steamship.com), open a **new** Shell and type `ship deploy`. This will push a new version of your Steamship package to Steamship's servers.

Details about the package will be accessible via https://www.steamship.com/packages/<your-package-name\>. A default demo web app will also be deployed and made globally-accessible.

# Package Files

## `api.py`

The main logic for the generator lives entirely in `api.py`. This file contains a `PromptPackage` class with one API method: `generate()`. Inside of `generate()`, the prompt is built with the user-supplied parameters and submitted to the generation plugin.

## `steamship.json`

After you deploy once, you will see a new `steamship.json` file in your repl. This is the manifest Steamship uses to store metadata about your package. This includes a handle for the package, as well as a version (allowing for package updates). This information will be used when you deploy your package to Steamship to present package details to users.

The tag `Prompt API` signals [Steamship](https://steamship.com) to automatically generate a special web interface for your package upon instance creation (post-deployment).

## `requirements.txt`

This file is used by [Steamship](https://steamship.com) in the package deployment process. Any dependencies that are needed by your code should be added here to ensure they are accessible to your package at runtime.

# About Steamship

[Steamship](https://steamship.com) is the fastest way to deploy language AI.

Steamship [packages](https://steamship.com/packages) provide a mechanism for encapsulating and deploying your language AI logic, 
allowing invocation with parameters that supports auto-scaling and persistence via a static HTTP endpoint.

Steamship packages can combine multiple Steamship [plugins](https://steamship.com/plugins) to build complex applications out of various AI building blocks. These plugins cover a broad variety of AI skills, including transcription, summarization, and generation.

To learn more about Steamship packages and plugins, please read our docs: https://docs.steamship.com/.

## Feedback and Support

Have any feedback on this template? Or on [Steamship](https://steamship.com) in general?

We'd love to hear from you. Please reach out to: hello@steamship.com, or join us on our [Discord](https://discord.gg/5Vry5ANVwT).