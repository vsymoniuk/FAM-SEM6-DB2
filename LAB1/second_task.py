from lxml import etree
from helpers.config import first_task_output_file


xml = etree.parse(first_task_output_file)
image_fragments = xml.xpath("//page/fragment[@type='image']")
min_value = int(min(list(map(lambda fragment: fragment.xpath('count(./image)'), image_fragments))))
print(f'Мінімальна кількість графічних фрагментів - {min_value}')
