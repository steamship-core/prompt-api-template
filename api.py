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
from termcolor import colored

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
  print(colored("Generate Compliments with GPT-3\n", attrs=['bold']))

  # This helper provides runtime API key prompting, etc.
  check_environment(RuntimeEnvironments.REPLIT)

  with Steamship.temporary_workspace() as client:
    prompt = PromptPackage(client)

    example_name = "Han Solo"
    example_trait = "heroism in the face of adversity"
    print(colored("First, let's run through an example...", 'green'))
    print(colored("Name:", 'grey'), f"{example_name}")
    print(colored("Trait:", 'grey'), f"{example_trait}")
    print(colored("Generating...", 'grey'))
    print(colored("Compliment:", 'grey'),
          f"{prompt.generate(name=example_name, trait=example_trait)}\n")

    print(colored("Now, try with your own inputs...", 'green'))

    try_again = True
    while try_again:
      kwargs = {}
      for parameter in inspect.signature(prompt.generate).parameters:
        kwargs[parameter] = input(
          colored(f'{parameter.capitalize()}: ', 'grey'))

      print(colored("Generating...", 'grey'))

      # This is the prompt-based generation call
      print(colored("Compliment:", 'grey'), f'{prompt.generate(**kwargs)}\n')

      try_again = input(colored("Generate another (y/n)? ",
                                'green')).lower().strip() == 'y'
      print()

    print("Ready to share with your friends (and the world)?")
    print("Run ", colored("$ ship deploy ", color='green',
                          on_color='on_black'),
          "to get a production-ready API endpoint and web-based demo app.")
