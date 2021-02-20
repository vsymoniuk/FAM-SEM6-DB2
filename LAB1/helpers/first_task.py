def get_links_to_parse(page: any, base_url: str, links_amount: int):
    page_links = page.xpath('//a/@href')
    valid_links = list(filter(lambda link: 'osvita.ua' in link, page_links))
    return valid_links[:links_amount]


def get_page_text_nodes(page: any):
    filtered_text_nodes = []
    text_nodes = page.xpath('body//*[not(self::script or self::style or self::img)]/text()')
    for text_node in text_nodes:
        text = text_node.strip('\n\t\r ')
        if len(text):
            filtered_text_nodes.append(text)
    return filtered_text_nodes


def get_page_images(page: any):
    return page.xpath('body//img/@src')
