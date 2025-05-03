import openai

class OpenAIAPI:
    """
    Integration with the OpenAI API for conversational AI and natural language processing.
    """

    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_response(self, prompt, max_tokens=150):
        """
        Generates a response using the OpenAI API.
        
        Args:
          prompt (str): The input prompt for the AI.
          max_tokens (int): The maximum number of tokens to generate.

        Returns:
          str: The AI-generated response.
        """
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=max_tokens
            )
            return response.choices[0].text.strip()
        except Exception as e:
            return f"Error: {str(e)}"