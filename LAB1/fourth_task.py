from lxml import etree
from helpers.config import third_task_output_file, fourth_task_xsl_template_file, fourth_task_output_file


goods = etree.parse(third_task_output_file)
xsl_template = etree.parse(fourth_task_xsl_template_file)

transform = etree.XSLT(xsl_template)
goods_html = transform(goods)

goods_html.write(fourth_task_output_file, pretty_print=True, encoding="utf-8")
