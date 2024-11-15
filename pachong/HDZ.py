# --coding:utf-8--
import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract_table_from_page(url):
    # 发送HTTP请求获取网页内容
    response = requests.get(url, verify=False)
    soup = BeautifulSoup(response.content, 'html.parser')

    # 提取表格数据
    tables = soup.find_all('table')
    if tables:
        # 如果找到表格，则保存为CSV文件
        df = pd.read_html(str(tables[0]))[0]
        df.to_csv(f'{url.split("/")[-1]}.csv', index=False)
    else:
        print(f"No table found on page: {url}")

    # 寻找下一个链接
    links = soup.find_all('a', href=True)
    for link in links:
        next_url = link['href']
        if next_url.startswith('http'):  # 确保链接是绝对链接
            extract_table_from_page(next_url)

# 替换为你要开始搜索的网址
start_url = 'https://www.gem.wiki/Category:Nuclear_power_plants'
extract_table_from_page(start_url)
