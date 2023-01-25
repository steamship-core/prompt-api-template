"""A Steamship package for prompt-based text generation.

This package provides a simple template for building prompt-based applications.

To run it:
1. Get a Steamship API Key (Visit: https://steamship.com/account/api). If you do not
   already have a Steamship account, you will need to create one.
2. Copy this key to a Replit Secret named STEAMSHIP_API_KEY.
3. Click the green `Run` button at the top of the window (or open a Shell and type `python3 api.py`).

More information about this template is provided in README.md.

To learn more about more advanced uses of Steamship, read our docs at: https://docs.steamship.com/packages/using.html.
"""
import os

from steamship import Steamship
from steamship.invocable import post, PackageService


class PromptPackage(PackageService):
    # Modify this to customize behavior to match your needs.
    PROMPT = "Say an unusual greeting to {name}. Compliment them on their {trait}."

    # When this package is deployed, this annotation tells Steamship to expose an endpoint that
    # accepts HTTP POST requests for the `/generate` request path.
    # See README.md for more information about deployment.
    @post("generate")
    def generate(self, **prompt_args) -> str:
        """Generate text from prompt parameters."""
        llm_config = {
            "max_words": 30,    # Controls length of generated output.
            # Controls randomness of output (range: 0.0-1.0).
            "temperature": 0.8
        }
        llm = self.client.use_plugin("gpt3", config=llm_config)
        return llm.generate(self.PROMPT, prompt_args)


# Try it out locally by running this file!
# You'll need to set the STEAMSHIP_API_KEY environment variable
if __name__ == "__main__":
    with Steamship.temporary_workspace() as client:
        package = PromptPackage(client)
        print("Generating compliments:")

        inputs = [
            ('Dave', 'prompt creation'),
            ('Ted', 'leadership skills'),
            ('Enias', 'marketing prowess'),
            ('Doug', 'love of doughnuts'),
        ]

        for input in inputs:
            name, trait = input
            print(f'[{name}, {trait}: {package.generate(name=name, trait=trait)}\n')
