"""A Steamship package for prompt-based text generation.

This package provides a simple template for building prompt-based applications.

To run it:
1. Get a Steamship API Key (Visit: https://steamship.com/account/api). If you do not
   already have a Steamship account, you will need to create one.
2. Copy this key to a Replit Secret named STEAMSHIP_API_KEY.
3. Click the green `Run` button at the top of the window (or open a Shell and type `python3 api.py`).

More information about this template is provided in README.md.

To learn more about advanced uses of Steamship, read our docs at: https://docs.steamship.com/packages/using.html.
"""
import inspect

from steamship import check_environment, RuntimeEnvironments, Steamship
from steamship.invocable import post, PackageService


class PromptPackage(PackageService):
  # Modify this to customize behavior to match your needs.
  PROMPT = "Say an unusual greeting to {name}. Compliment them on their {trait}."

  # When this package is deployed, this annotation tells Steamship
  # to expose an endpoint that accepts HTTP POST requests for the
  # `/generate` request path.
  # See README.md for more information about deployment.
  @post("generate")
  def generate(self, name: str, trait: str) -> str:
    """Generate text from prompt parameters."""
    llm_config = {
      # Controls length of generated output.
      "max_words": 30,
      # Controls randomness of output (range: 0.0-1.0).
      "temperature": 0.8
    }
    prompt_args = {"name": name, "trait": trait}

    llm = self.client.use_plugin("gpt-3", config=llm_config)
    return llm.generate(self.PROMPT, prompt_args)


# Try it out locally by running this file!
if __name__ == "__main__":
  # This helper provides runtime API key prompting, etc.
  check_environment(RuntimeEnvironments.REPLIT)

  with Steamship.temporary_workspace() as client:
    package = PromptPackage(client)
    print("Let's try it out!")

    try_again = True
    while try_again:
      print()
      kwargs = {}
      for parameter in inspect.signature(package.generate).parameters:
        kwargs[parameter] = input(f'{parameter.capitalize()}: ')
      print("Generating...\n")

      # This is the prompt-based generation call
      print(f'{package.generate(**kwargs)}\n')

      try_again = input("Try again (y/n)? ").lower().strip() == 'y'
