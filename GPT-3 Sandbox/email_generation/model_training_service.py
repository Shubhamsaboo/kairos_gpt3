from training_data import defaultPrompt
from const import API_KEY
import openai


def set_openai_key(key):
    """Sets OpenAI key."""
    openai.api_key = key


class Code:
    def __init__(self):
        print("Model Intilization--->")
        #set_openai_key(API_KEY)

    def query(self, prompt, myKwargs={}):
        """
        wrapper for the API to save the prompt and the result
        """

        # arguments to send the API
        kwargs = {
            "engine": "davinci",
            "temperature": 0.50,
            "max_tokens": 70,
            "best_of": 2,
            "stop": ["Input:"]
        }

        for kwarg in myKwargs:
            kwargs[kwarg] = myKwargs[kwarg]

        r = openai.Completion.create(prompt=prompt, **kwargs)["choices"][0]["text"].strip()
        return r

    def model_prediction(self, input, api_key):
        """
        wrapper for the API to save the prompt and the result
        """
        # Setting the OpenAI API key got from the OpenAI dashboard
        set_openai_key(api_key)
        output = self.query(defaultPrompt.format(input))
        return output
