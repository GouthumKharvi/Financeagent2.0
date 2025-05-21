
import openai

class LanguageAgent:
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_narrative(self, prompt, max_tokens=250, temperature=0.7):
        """
        Generate a narrative or answer using the OpenAI GPT API.

        Args:
            prompt (str): The input text prompt or context.
            max_tokens (int): The maximum number of tokens to generate.
            temperature (float): Controls creativity of responses.

        Returns:
            str: The generated narrative or answer.
        """
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=max_tokens,
                temperature=temperature,
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"Error during LLM call: {str(e)}"
