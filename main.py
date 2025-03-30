import streamlit as st
st.title("🎈 My First Streamlit App")
from marker.converters.pdf import PdfConverter
from marker.models import create_model_dict
from marker.output import text_from_rendered
from marker.config.parser import ConfigParser
config = {
    "output_format": "markdown",
    "disable_image_extraction": True
}

config_parser = ConfigParser(config)

converter = PdfConverter(
    config=config_parser.generate_config_dict(),
    artifact_dict=create_model_dict(),
    processor_list=config_parser.get_processors(),
    renderer=config_parser.get_renderer(),
    llm_service=config_parser.get_llm_service()
)
import time
tic = time.time()
rendered = converter("resume.pdf")
text, _, images = text_from_rendered(rendered)
toc = time.time()
st.write(text)
st.write(images)
st.write(toc - tic)
