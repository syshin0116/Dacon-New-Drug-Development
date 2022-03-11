import sys
import argparse
from tkinter import messagebox

import requests #알트+엔터(cmd+1)
from collections import Counter

#kakao연결 + 신청해놨던 키.
API_url = 'https://dapi.kakao.com/v2/vision/multitag/generate'
MYAPP_KEY = 'df5989bfdeb66e539382f8c9a0275d74'

def multi_tag(image_url):
    header = {'Authorization':'KakaoAK {}'.format(MYAPP_KEY)}
    img_data = {'image_url': image_url}
    response = requests.post(API_url, headers=header, data=img_data)
    print(response)
    json_result = response.json()
    print(json_result)
    result = json_result['result']
    print(result)
    label_kr = result['label_kr']
    print(label_kr)
    return label_kr


if __name__ == '__main__':
    img_list = ['https://img.imbc.com/template/2021/11/program_ddef4556-bde9-42ee-b5d0-f9700326c252.jpg',
                'https://img2.sbs.co.kr/img/sbs_cms/WE/2021/07/12/3DL1626054692449.jpg',
                'https://w.namu.la/s/1c0e615586d75cb6814b6c39e86f19b0e21917c8a3d62af2264667a34aae228cfae185c2365ab46369a4e6c9b0744ccd204da6868e51cd84e9f7176432595ade1484e5464963a16d2a79d8b25622901a',
                'https://images.chosun.com/resizer/taI1PaMAxWVDBw3j1n0ZUoj0eB8=/616x0/smart/cloudfront-ap-northeast-1.images.arcpublishing.com/chosun/DTPZSPJJJRAWXLDE66PUOIVAF4.jpg',
                'https://posri.re.kr/images/old_files/board/Iron100-2.jpg',
                'https://pds.joongang.co.kr/news/component/htmlphoto_mmdata/202110/14/2cff8a58-552f-49c2-b566-5ba73d343c96.jpg',
                'https://upload.wikimedia.org/wikipedia/commons/4/47/New_york_times_square-terabass.jpg',
                'https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Causeway_Bay_sit-in.JPG/250px-Causeway_Bay_sit-in.JPG'
                ]
    result_list = []
    for img in img_list:
        result_list += multi_tag(img)

    print("----", result_list)
    count_result = Counter(result_list)
    print(count_result)
    print(count_result.get('사람'))

    print(count_result.most_common(5))#[('사람', 3), ('여러사람', 3), ('남성', 2), ('안경', 1)]

    order_5 = count_result.most_common(5)
    print(order_5[0]) #('사람', 3)
    order_1 = order_5[0]
    print('제일 반도수가 높은 단어는', order_1[0], '빈도수는', order_1[1]) # 제일 반도수가 높은 단어는 사람 빈도수는 3

    tour = ''
    if order_1[0] == '사람':
        tour = '제주도'
    elif order_1[0] == '남성':
        tour = '등산'
    else:
        tour = '놀이공원'
    messagebox.showinfo('추천', '당신에게 ' + tour + '를 추천합니다.')