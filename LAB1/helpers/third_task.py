from operator import itemgetter
from lxml import etree


def get_good_meta(good):
    name = good.xpath(".//div[@class='name']/a/text()")[0]
    price = good.xpath(".//div[@class='price']/text()")[0].strip('\n ')
    image_url = good.xpath(".//img/@src")[0]

    return {
        "name": name,
        "price": price,
        "image_url": image_url,
    }


def append_good_xml_item(parent, good):
    good_meta = get_good_meta(good)
    name, price, image_url = itemgetter('name', 'price', 'image_url')(good_meta)

    good_element = etree.SubElement(parent, 'good')

    name_element = etree.SubElement(good_element, 'name')
    name_element.text = name

    price_element = etree.SubElement(good_element, 'price')
    price_element.text = price

    image_element = etree.SubElement(good_element, 'image')
    image_element.text = image_url
