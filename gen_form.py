#!/usr/bin/env python3
"""Generate a filled expert registration form as docx using only stdlib"""

import zipfile
import os
from datetime import datetime

def create_docx():
    output = '/Users/aaa/.openclaw/media/filled_form.docx'
    
    # Simple docx XML content
    document_xml = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
<w:body>
<w:p><w:pPr><w:jc w:val="center"/><w:rPr><w:b/><w:sz w:val="28"/></w:rPr></w:pPr><w:r><w:rPr><w:b/><w:sz w:val="28"/></w:rPr><w:t>附件一：专家申请入库登记表</w:t></w:r></w:p>

<w:p><w:pPr><w:rPr><w:b/><w:sz w:val="24"/></w:rPr></w:pPr><w:r><w:rPr><w:b/><w:sz w:val="24"/></w:rPr><w:t>专家基本信息</w:t></w:r></w:p>

<w:tbl>
<w:tblPr><w:tblStyle w:val="TableGrid"/><w:tblW w:w="9000" w:type="dxa"/></w:tblPr>
<w:tblGrid><w:gridCol w:w="3000"/><w:gridCol w:w="6000"/></w:tblGrid>

''' + '\n'.join([
f'''<w:tr><w:tc><w:p><w:r><w:t>{label}</w:t></w:r></w:p></w:tc><w:tc><w:p><w:r><w:t>{value}</w:t></w:r></w:p></w:tc></w:tr>'''
    for label, value in [
        ('姓名', '[待填写]'),
        ('性别', '[待填写]'),
        ('出生年月', '[待填写]'),
        ('身份证号码', '[待填写]'),
        ('工作单位', '[待填写]'),
        ('工作年限', '[待填写]'),
        ('职务', '[待填写]'),
        ('学历', '[待填写]'),
        ('职称', '[待填写]'),
        ('手 机', '[待填写]'),
        ('E-mail', '[待填写]'),
        ('评审专业', '[待填写]'),
    ]
]) + '''

</w:tbl>

<w:p><w:r><w:t> </w:t></w:r></w:p>
<w:p><w:pPr><w:rPr><w:b/></w:rPr></w:pPr><w:r><w:rPr><w:b/></w:rPr><w:t>专家入库申请声明</w:t></w:r></w:p>
<w:p><w:r><w:t>本人自愿申请加入中教集团专家库，接受中教集团对本人入库资格的评审，承诺以上所填信息均真实有效。本人如能通过评审并进入中教集团专家库，将自觉遵守以下工作守则：</w:t></w:r></w:p>
<w:p><w:r><w:t>1、认真学习并执行《中教集团招标类采购管理 3.0》、《后勤部广东分部-采购管理办法》；</w:t></w:r></w:p>
<w:p><w:r><w:t>2、履行职责，遵守纪律，严守秘密，廉洁自律，不自行与投标人进行可能影响评审结果的接触；</w:t></w:r></w:p>
<w:p><w:r><w:t>3、不弄虚作假，不谋取私利，不泄露与评审活动有关的情况和资料；</w:t></w:r></w:p>
<w:p><w:r><w:t>4、不收除审核评审工作劳务报酬以外的任何现金、有价证券和礼物，不收有关利害关系人的任何财物和好处；</w:t></w:r></w:p>
<w:p><w:r><w:t>5、客观、公正、公平地参与评审工作，维护国家利益，维护招标、投标双方的合法权益；</w:t></w:r></w:p>
<w:p><w:r><w:t>6、认真明确提出个人意见并对所提意见承担责任；</w:t></w:r></w:p>
<w:p><w:r><w:t>7、如本人存在国家法律、法规或规章规定应该回避的情形时，将主动申请回避。</w:t></w:r></w:p>
<w:p><w:r><w:t> </w:t></w:r></w:p>
<w:p><w:r><w:t>专家本人签字：_____________</w:t></w:r></w:p>
<w:p><w:r><w:t>日    期：''' + datetime.now().strftime('%Y年%m月%d日') + '''</w:t></w:r></w:p>
<w:p><w:r><w:t> </w:t></w:r></w:p>
<w:p><w:r><w:t>【审批栏位 - 由审批人填写】</w:t></w:r></w:p>
<w:p><w:r><w:t>招标采购中心负责人审批：_____________</w:t></w:r></w:p>
<w:p><w:r><w:t>后勤部广东分部负责人审批：_____________</w:t></w:r></w:p>
<w:p><w:r><w:t> </w:t></w:r></w:p>
<w:p><w:r><w:t>说明：1.请随此申请登记表附专家本人身份证、学历证（如有）、职称证书（如有）复印件。</w:t></w:r></w:p>
<w:p><w:r><w:t>2.专家本人信息变更时应及时通知我中教集团招标采购中心。</w:t></w:r></w:p>

<w:p><w:r><w:br w:type="page"/></w:r></w:p>

<w:p><w:pPr><w:jc w:val="center"/><w:rPr><w:b/><w:sz w:val="28"/></w:rPr></w:pPr><w:r><w:rPr><w:b/><w:sz w:val="28"/></w:rPr><w:t>附件二：项目评标专家费支付申请表</w:t></w:r></w:p>

<w:tbl>
<w:tblPr><w:tblStyle w:val="TableGrid"/><w:tblW w:w="9000" w:type="dxa"/></w:tblPr>
<w:tblGrid><w:gridCol w:w="3000"/><w:gridCol w:w="6000"/></w:tblGrid>
<w:tr><w:tc><w:p><w:r><w:t>学校</w:t></w:r></w:p></w:tc><w:tc><w:p><w:r><w:t>[待填写]</w:t></w:r></w:p></w:tc></w:tr>
<w:tr><w:tc><w:p><w:r><w:t>项目编号</w:t></w:r></w:p></w:tc><w:tc><w:p><w:r><w:t>[待填写]</w:t></w:r></w:p></w:tc></w:tr>
<w:tr><w:tc><w:p><w:r><w:t>项目名称</w:t></w:r></w:p></w:tc><w:tc><w:p><w:r><w:t>[待填写]</w:t></w:r></w:p></w:tc></w:tr>
<w:tr><w:tc><w:p><w:r><w:t>评审日期</w:t></w:r></w:p></w:tc><w:tc><w:p><w:r><w:t>[待填写]</w:t></w:r></w:p></w:tc></w:tr>
<w:tr><w:tc><w:p><w:r><w:t>评审专家</w:t></w:r></w:p></w:tc><w:tc><w:p><w:r><w:t>共 _____ 人</w:t></w:r></w:p></w:tc></w:tr>
<w:tr><w:tc><w:p><w:r><w:t>使用自有车辆</w:t></w:r></w:p></w:tc><w:tc><w:p><w:r><w:t>□ 是  ■ 否（请选择）</w:t></w:r></w:p></w:tc></w:tr>
<w:tr><w:tc><w:p><w:r><w:t>专家车辆登记</w:t></w:r></w:p></w:tc><w:tc><w:p><w:r><w:t>[如有车辆请填写]</w:t></w:r></w:p></w:tc></w:tr>
<w:tr><w:tc><w:p><w:r><w:t>评审费合计</w:t></w:r></w:p></w:tc><w:tc><w:p><w:r><w:t>_____ 元</w:t></w:r></w:p></w:tc></w:tr>
<w:tr><w:tc><w:p><w:r><w:t>车旅费合计</w:t></w:r></w:p></w:tc><w:tc><w:p><w:r><w:t>_____ 元</w:t></w:r></w:p></w:tc></w:tr>
<w:tr><w:tc><w:p><w:r><w:t>共计</w:t></w:r></w:p></w:tc><w:tc><w:p><w:r><w:t>_____ 元</w:t></w:r></w:p></w:tc></w:tr>
</w:tbl>

<w:p><w:r><w:t> </w:t></w:r></w:p>
<w:p><w:r><w:t>【审批栏位 - 由审批人填写】</w:t></w:r></w:p>
<w:p><w:r><w:t>经办人：_____________</w:t></w:r></w:p>
<w:p><w:r><w:t>招标采购中心负责人审批：_____________</w:t></w:r></w:p>
<w:p><w:r><w:t>后勤部广东分部负责人审批：_____________</w:t></w:r></w:p>
<w:p><w:r><w:t> </w:t></w:r></w:p>
<w:p><w:r><w:t>注：1、提交此表需一同附项目评审专家签到表复印件。</w:t></w:r></w:p>
<w:p><w:r><w:t>2、上述填报项不够填写，可自行加行。</w:t></w:r></w:p>

</w:body>
</w:document>'''

    content_types = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
</Types>'''

    rels = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>'''

    word_rels = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
</Relationships>'''

    with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED) as zf:
        zf.writestr('[Content_Types].xml', content_types)
        zf.writestr('_rels/.rels', rels)
        zf.writestr('word/_rels/document.xml.rels', word_rels)
        zf.writestr('word/document.xml', document_xml)
    
    print(f'Created: {output}')
    return output

create_docx()
