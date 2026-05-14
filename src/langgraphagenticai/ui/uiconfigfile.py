from configparser import ConfigParser
from pathlib import Path


class Config:

    def __init__(self):

        config_file = Path(__file__).parent / "uiconfigfile.ini"

        self.config = ConfigParser()
        self.config.read(config_file)

    def get_llm_options(self):

        options = self.config["DEFAULT"].get(
            "LLM_OPTIONS",
            "GROQ"
        )

        return [option.strip() for option in options.split(",")]

    def get_usecase_options(self):

        options = self.config["DEFAULT"].get(
            "USECASE_OPTIONS",
            "Chatbot"
        )

        return [option.strip() for option in options.split(",")]

    def get_groq_model_options(self):

        options = self.config["DEFAULT"].get(
            "GROQ_MODEL_OPTIONS",
            "llama3-8b-8192"
        )

        return [option.strip() for option in options.split(",")]

    def get_page_title(self):

        return self.config["DEFAULT"].get(
            "PAGE_TITLE",
            "LangGraph Agentic AI"
        )