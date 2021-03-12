
"""
Given the input format, compute:

Output format:
{
    "name/en-us": Product name,
    "name/fr-ca": Product name,
    "vendor_code": Unique identifier of the product used by vendor,
    "species/en-us": Wood type,
    "species/fr-ca": Wood type,
    "link/en-us": English link,
    "link/fr-ca": French link, obtained by adding "/fr" after .com - ie https://www.example.com/fr/<path>,
    "size_name": <width inches>" <width inches fraction> (<width millimeters> mm),
	"tile_width": Plank width in meters,
    "tile_layout": "random_length", "herringbone" or "repeat",
				All “herringbone” have the word "herring" in their english series (series_en). 
				“random_length” products do not contain "herring".
    "tile_length": Plank length in meters. Use "0.5" for Herringbone and "2.0" for other planks 
				- Ensure that random_length or repeat products have “2.0” as their value,
	"vendor_source": Path to image, relative to the "userdata" directory.
				- When "image_name" is defined in the input, you should:
					- call the "download_img(image_url, local_path)" function and 
					- you should make the image URL using "https://assets.example.com/images/<image_name>.jpg". 
					- local path equal to "/userdata/example/assets/floors/<image_name>.jpg".
					- Afterward, set "vendor_source" to the local path relative to the userdata directory.
				- When "image_name" is not defined
					* Use the pre-existing "/userdata/example/image_not_found.jpg" file for "vendor_source"
					* Set "tile_layout" to "repeat"
					* Set "is_hidden" to 1
}


"""

#!/bin/python3

import re

inputs = {
  "sku": "09-20T8-000-332",
  "master_title_fr": "Érable Merveilleux",
  "master_title_en": "Marvelous Maple",
  "series_en": "regular",
  "series_fr": "ordinaire",
  "specie_en": "Maple",
  "specie_fr": "Érable",
  "grade_value": "9",
  "grade_en": "Pro",
  "grade_fr": "Pro",
  "width_value": "G",
  "width_inch": "4",
  "width_inch_fraction": "7/16",
  "width_milimeter": "112",
  "color_value": "00",
  "color_en": "Natural",
  "color_fr": "Naturel",
  "texture_value": "0",
  "texture_en": "Normal",
  "texture_fr": "Normale",
  "qty_per_box": "29",
  "qty_per_box_en": "29 sq.ft./Box",
  "qty_per_box_fr": "29 pi.ca./Bte",
  "is_new": "1",
  "last_changed": "1551830705",
  "thickness_milimeter": "12.70",
  "thickness_inch": '½ "',
  "group_color_value": "5",
  "group_color_en": "Naturals",
  "group_color_fr": "Naturels",
  "group_width_value": "3",
  "group_width_desc": 'Entre 4" et 5"',
  "destid1": "66902",
  "url": "https://www.example.com/SKU/09-20T8-000-332",
  "image_name": "09-20T8-000-XXX",
  "herringbone_variant": "",
  # SKU of herringbone installment
  }

def convert(inputs):
  output = {}
  output["name/en-us"] = inputs["master_title_en"]
  output["name/fr-ca"] = inputs["master_title_fr"]
  output["vendor_code"] = inputs["sku"]
  output["species/en-us"] = inputs["specie_en"]
  output["species/fr-ca"] = inputs["specie_fr"]
  output["link/en-us"] = inputs["url"]
  output["link/fr-ca"] = inputs["url"].replace('.com', '.com/fr')
  # pattern = re.compile(r"(.*\.com)(.*)")
  # d = pattern.match(inputs["url"])
  # output["link/fr-ca"] = d.group(1) + '/fr' + d.group(2)
  output["size_name"] = f'{inputs["width_inch"]}" {inputs["width_inch_fraction"]} ({inputs["width_milimeter"]}mm)'
  output["tile_width"] = float(inputs["width_milimeter"])/1000
  output["tile_layout"] = "herringbone" if "herring" in inputs["series_en"] else "random_length"
  
  if "image_name" in inputs:
    image_url = f' https://assets.example.com/images/{inputs["image_name"]}.jpg'
    local_path = f'/userdata/example/assets/floors/{inputs["image_name"]}.jpg'
    download_img(image_url, local_path)
    output["vendor_source"] = "/userdata/example/assets/floors/"
  else:
    output["vendor_source"] = "/userdata/example/image_not_found.jpg"
    output["tile_layout"] = "repeat"
    output["hidden"] = 1

  output["tile_length"] = 0.5 if output["tile_layout"] =='herringbone' else 2

  return output


def download_img(image_url, local_path):
  pass


for item in convert(inputs):
  print(f'{item} : {convert(inputs)[item]}')


