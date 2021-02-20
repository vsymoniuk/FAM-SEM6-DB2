from lxml import etree
from helpers.shared import get_html_by_url
from helpers.config import first_task_url, page_to_parse_amount, first_task_output_file
from helpers.first_task import get_links_to_parse, get_page_text_nodes, get_page_images

links_to_parse = [first_task_url]
pages_to_parse = []
links_iterator = 0

# getting all pages to parse
while len(pages_to_parse) < page_to_parse_amount:
    try:
        current_page_link = links_to_parse[links_iterator]
        current_page = get_html_by_url(current_page_link)
        required_links_amount = page_to_parse_amount - len(pages_to_parse)
        valid_links = get_links_to_parse(current_page, first_task_url, required_links_amount)
        links_to_parse += valid_links
        for link in valid_links:
            pages_to_parse.append(get_html_by_url(link))
        links_iterator += 1
    except IndexError:
        print("There is no enough links to parse")

# parsing pages to XML
xml = etree.Element('data')

for i in range(page_to_parse_amount):
    page_link = links_to_parse[i]
    page = pages_to_parse[i]

    page_element = etree.SubElement(xml, 'page')
    page_element.set('url', page_link)

    text_fragment = etree.SubElement(page_element, 'fragment')
    text_fragment.set('type', 'text')
    text_nodes = get_page_text_nodes(page)
    for text_node in text_nodes:
        text = etree.SubElement(text_fragment, 'text')
        text.text = text_node

    image_fragment = etree.SubElement(page_element, 'fragment')
    image_fragment.set('type', 'image')
    image_urls = get_page_images(page)
    for url in image_urls:
        image = etree.SubElement(image_fragment, 'image')
        image.text = url

xml_tree = etree.ElementTree(xml)
xml_tree.write(first_task_output_file, pretty_print=True, xml_declaration=True, encoding="utf-8")




