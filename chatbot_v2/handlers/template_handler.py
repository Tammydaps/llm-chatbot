from typing import Dict
from chatbot_v2.templates.templates import (
    clean_template,
)
from chatbot_v2.handlers.base_handler import (
    BaseHandler,
    section_templates
)


class TemplateHandler(BaseHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def section(self):
        return self.__section_template

    @section.setter
    def section(self, section_type: str):
        if section_type not in section_templates.keys():
            raise ValueError(
                f"This section type: {section_type} is not supported"
            )
        self.__section_template = section_templates.get(section_type)

    def get_templates(self):
        templates = []
        for template_info in self.__section_template[0].items():
            clean_template_info = clean_template(template_info)
            template = clean_template_info[1][1]
            templates.append(template)
        return templates

    def get_summaries(self):
        summaries = []
        for template_info in self.__section_template[0].items():
            clean_template_info = clean_template(template_info)
            summary = clean_template_info[1][0]
            summaries.append(summary)
        return summaries

    def get_template_data(self):
        pass
