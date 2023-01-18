"""A Steamship package for prompt-based text generation.

This package provides a simple template for building prompt-based applications.

To run it:
1. Get a Steamship API Key (Visit: https://steamship.com/account/api). If you do not
   already have a Steamship account, you will need to create one.
2. Copy this key to a Replit Secret named STEAMSHIP_API_KEY.
3. Click the green `Run` button at the top of the window (or open a Shell and type `python3 api.py`).

To change the behavior:
1. Edit the prompt template to match your use case (found in PROMPT_TEMPLATE).
2. Add any variables you need to `generate` and in the call to `PROMPT_TEMPLATE.format` 

To deploy it for others to use on the web:
1. Set a unique 'handle' in your steamship.json file (defaults to `my-prompt-package`).
2. Close any Replit Shells that were opened before you created the STEAMSHIP_API_KEY secret.
3. Open a **new** Replit Shell.
4. Run `ship deploy` in the Shell.
5. Visit the package page for your app to see a running demo version (displayed as output from `ship deploy`).
   It should look like: http://steamship.com/packages/<your-package-name>

More information about this template is provided in README.md.
"""

import uuid
import os

from steamship import File, Block, Steamship
from steamship.data import TagKind, TagValue
from steamship.invocable import post, PackageService


class PromptPackage(PackageService):
  """Example Steamship Prompt package.

    To use this package, invoke the `generate` method with the parameters
    that will be used to fill in the PROMPT_TEMPLATE for generation. Each
    invocation will return a response with a length controlled by the MAX_WORDS
    setting.

    More advanced configuration of Steamship packages are possible. To learn more,
    read our docs at: https://docs.steamship.com/packages/using.html.
    """

  # This is the heart of your prompt app. This can be as simple or as involved
  # as you would like. Have fun playing around with it to tailor exactly to
  # your tastes.
  #
  # Edit this, using {} where you'd like to insert parameters.
  #
  # In this example, the prompt template takes two parameters:
  #  1. the name of the person being greeted
  #  2. the trait that you'd like to compliment them on
  PROMPT_TEMPLATE = "Say an unusual greeting to {}. Compliment them on their {}."

  # (Optional) Adjust the randomness; 0 = no variety, 1 = lots of variety
  PROMPT_TEMPERATURE = 0.8

  # (Optional) What's the longest response you want back?
  MAX_WORDS = 30

  # When this package is deployed, this annotation tells Steamship to expose an endpoint that
  # accepts HTTP POST requests for the `/generate` request path.
  @post("generate")
  def generate(self, name: str, trait: str) -> str:
    """Generate text from prompt parameters."""

    # Update this to match any changes you make to PROMPT_TEMPLATE
    # (and the method signature of `generate()`.).
    prompt_text = self.PROMPT_TEMPLATE.format(name, trait)

    # Get an instance of the default text generation plugin, configured
    # with your settings for content length (MAX_WORDS) and
    # randomness (PROMPT_TEMPERATURE).
    generator = self.client.use_plugin("prompt-generation-default",
                                       config={
                                         "max_words": self.MAX_WORDS,
                                         "temperature": self.PROMPT_TEMPERATURE
                                       })

    # Each prompt will be stored in Steamship as a File. The generated text will be
    # associated with the prompt File via Steamship tags. This enables later retrieval
    # of prompts and their results (which may be used in subsequent operations, etc.).
    #
    # To learn about the Steamship data model, please consult our the docs:
    # https://docs.steamship.com/workspaces/data_model/index.html
    file = File.create(self.client,
                       blocks=[Block.CreateRequest(text=prompt_text)])

    # This requests generation from the parameterized prompt. Tagging with our prompt generator
    # plugin will result in a new tag that contains the generated output.
    # We `wait()` because generation of text is done asynchronously and may take a few moments
    # (somewhat depending on the complexity of your prompt).
    file.tag(plugin_instance=generator.handle).wait()

    # Retrieve the stored generated content and return it in the body of the response.
    # Refreshing the file ensures that we get the latest content for the file.
    return self._generated_text(file.refresh())

  def _generated_text(self, prompt_file: File) -> str:
    """Get the generated text for a prompt file."""

    # Here, we iterate through the content blocks associated with a file
    # as well as any tags on that content to find the generated text.
    #
    # The Steamship data model provides flexible content organization,
    # storage, and lookup. Read more about the data model via:
    # https://docs.steamship.com/workspaces/data_model/index.html
    for text_block in prompt_file.blocks:
      for block_tag in text_block.tags:
        if block_tag.kind == TagKind.GENERATION:
          return self._sanitize(block_tag.value[TagValue.STRING_VALUE])

    return ""

  def _sanitize(self, text: str):
    """Remove any leading/trailing whitespace and partial sentences.

      This assumes that your generated output will include consistent punctuation. You may
      want to alter this method to better fit the format of your generated text.
      """
    last_punc = -1
    for i, c in enumerate(reversed(text)):
      if c in ".!?\"":
        last_punc = len(text) - i
        break
    if last_punc != -1:
      result = text[:last_punc + 1]
    else:
      result = text
    return result.strip()


# Try it out locally by running this file!
if __name__ == "__main__":
  api_key = os.environ.get('STEAMSHIP_API_KEY')
  if api_key is None or api_key == "" or api_key == "REPLACE-ME":
    print(
      """You must add your Steamship API key as a Replit secret to run this replit. 
More info on how to add a Replit Secret can be found here: https://shorturl.at/bceow
    
Get a Steamship API key here: https://steamship.com/account/api""")
    api_key = input("Paste your API key here: ")

  # This will build a Steamship client using the API Key retrieved from the environment.
  # You must create a Replit Secret of STEAMSHIP_API_KEY with your Steamship API Key.
  # Steamship API Keys can be retrieved via: https://steamship.com/account/api
  client = Steamship(api_key=api_key)

  # This will give you a new random workspace instance for testing and
  # development. Once you are ready to deploy to production, you may want a
  # consistent workspace (to save your work in single place, etc.). For that,
  # replace the generated UUID with the name you want to use consistently.
  client.switch_workspace(str(uuid.uuid4()))

  # Create an instance of your package for testing
  # Here we will generate 5 examples with the same inputs.
  package = PromptPackage(client)
  print("Completing your prompt 5 times with the given inputs:")

  for i in range(5):
    print(
      f"Run {i+1}\n--\n{package.generate(name='Dave', trait='prompt creation')}\n---"
    )

    # Try more examples here!

    # Clean up testing workspace
  client.get_workspace().delete()
