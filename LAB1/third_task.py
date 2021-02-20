from lxml import etree
from helpers.shared import get_html_by_url
from helpers.config import third_task_url, goods_to_parse_amount, third_task_output_file
from helpers.third_task import append_good_xml_item

goods_page = get_html_by_url(third_task_url)
goods_container = goods_page.xpath("//div[@class='item']")[:goods_to_parse_amount]

xml = etree.Element('data')

for good in goods_container:
    append_good_xml_item(xml, good)

xml_tree = etree.ElementTree(xml)
xml_tree.write(third_task_output_file, pretty_print=True, xml_declaration=True, encoding="utf-8")
