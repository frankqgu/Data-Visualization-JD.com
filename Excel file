
import requests
import json
import time
import random
import xlwt

file = xlwt.Workbook(encoding='utf-8')
sheet = file.add_sheet('data', cell_overwrite_ok=True)
start = time.time()
for i in range(5):    
    try:
        url = 'https://club.jd.com/comment/productPageComments.action?&productId=100008587483&score=3&sortType=5&page=%s&pageSize=10&isShadowSku=0&rid=0&fold=1' % i
        
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.60',
            'referer': 'https://item.jd.com/100008587483.html'
        }
        response = requests.get(url, headers=headers)
        data = json.loads(response.text)  
        page = i * 10   
        if(data['comments']):
            for temp in data['comments']:
                sheet.write(page, 0, page)  
                sheet.write(page, 1, temp['content'])   
                sheet.write(page, 2, temp['score'])
                page = page + 1
            print('第%s页爬取成功' % i)
        else:
            print('.............第%s页爬取失败' %i)
            file.save('comments.xlsx') 

    except Exception as e:
        print('爬取失败，url：%s'%url)
        print('page是%s'%i)
        continue
    time.sleep(random.random() * 5) 
end = time.time()
file.save('comments.xlsx')
