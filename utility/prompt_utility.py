import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class PromptCreation:
    @staticmethod
    def generic_prompt(client, openai_model, messages):
        """
        This function create the prompt, request and return the response
        :param client: OpenAI client
        :param openai_model: OpenAI model that used
        :param messages: Question of the user
        :return: Stream that contain the response
        """
        try:
            return client.chat.completions.create(
                model=openai_model,
                messages=[
                    {"role": msg["role"], "content": msg["content"]}
                    for msg in messages
                ], stream=True,)

        except Exception as e:
            logger.info(f"Inside generic_prompt function.\n {e}")
