#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import os


def download_file(mp3_url, file_folder):
    """下载MP3文件"""
    # 文件夹不存在，则创建文件夹
    folder = os.path.exists(file_folder)
    if not folder:
        os.makedirs(file_folder)
    # 读取远程MP3资源
    res = requests.get(mp3_url)
    res.raise_for_status()
    # 获取文件名
    file_name = os.path.basename(mp3_url)
    file_path = os.path.join(file_folder, file_name)
    print('正在写入资源文件：', file_path)
    # 保存到本地
    # image_file = open(file_path, 'wb')
    # for chunk in res.iter_content(100000):
    #     image_file.write(chunk)
    # image_file.close()
    with open(file_path, 'wb') as f:
        f.write(res.content)
    print('写入文件结束！')


# 程序主入口
if __name__ == "__main__":
    # MP3源地址url
    url = 'https://music.163.com/song/media/outer/url?id=27587486.mp3'
    # MP3保存文件夹
    folder = 'mp3/'
    # 调用下载方法
    download_file(url, folder)
