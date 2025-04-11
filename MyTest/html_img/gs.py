# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET

# 创建根元素
root = ET.Element("data")

# 创建子元素
modify = ET.SubElement(root, "modify")
r = ET.SubElement(modify, "r")

# 添加数据
data = [
    {"name": "fileName", "value": "wszmkj_sbf.raq"},
    {"name": "srcType", "value": "file"},
    {"name": "cachedId", "value": "A_1520"},
    {"name": "pageUrl", "value": "/public/xxcx/sbf_wszmkj_jg.jsp?sqq=2024-12-01&amp;sqz=2025-01-31&amp;reportParamsId=101517"},
    {"name": "backAndRefresh", "value": "/public/xxcx/sbf_wszmkj_jgdy.jsp?bxh=30033880"},
    {"name": "promptAfterSave", "value": "no"},
    {"name": "saveDataByListener", "value": "no"},
    {"name": "inputExceptionPage", "value": "/myErrorPage.jsp"},
    {"name": "keyRepeatError", "value": "no"},
    {"name": "data", "value": None},
    {"name": "params", "value": "sqz=2025-01-31;djxh=10112301000033756847;bxh=30033880;sqq=2024-12-01"}
]
for item in data:
    value = item["value"] if item["value"] is not None else ""
    c = ET.SubElement(r, "c", attrib={"name": item["name"], "value": value})
xml_str = ET.tostring(root, encoding='utf-8', method='xml', xml_declaration=True).decode('utf-8')
print(xml_str)
# 生成 XML 树
# tree = ET.ElementTree(root)

# 输出或保存 XML 文件
# tree.write("output.xml", encoding="utf-8", xml_declaration=True)
