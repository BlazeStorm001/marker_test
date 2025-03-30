from marker.converters.pdf import PdfConverter
from marker.models import create_model_dict
from marker.output import text_from_rendered
from marker.config.parser import ConfigParser
from pdb import set_trace
config = {
    "output_format": "json",
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
print(config_parser.get_processors())
set_trace()
import time
tic = time.time()
rendered = converter("D:\\Desktop\\fastapi_demo\\resumes\\shivam_kumar_f.pdf")
text, _, images = text_from_rendered(rendered)
toc = time.time()
print(text)
print(images)
print(toc - tic)
