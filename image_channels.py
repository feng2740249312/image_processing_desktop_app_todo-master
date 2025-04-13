import numpy as np
import image_io
from image_utils import logging


def split_image_channels(image):
    '''
    该函数用于分割图像的颜色通道
    :param image: 输入图像，numpy数组
    :return: 图像的颜色通道列表
    '''
    try:
        logging.info("开始分割图像颜色通道")
        
        # TODO: 1. 检测多通道图像 image 是否真多通道的，如果是，显示错误信息并返回
        # 提示: 使用 raise 抛出异常信息：图像通道数必须大于等于2
        
        
        # TODO: 2. 使用numpy的split函数，沿着通道维度分割图像
        
        
        # TODO: 3. 把分割后的通道图像添加到一个列表 channel_list 中，注意要去掉多余的维度
        channel_list = 
        
        logging.info(f"成功分割图像颜色通道")
        return channel_list
    except Exception as e:
        # print(f"在分割图像颜色通道时发生错误: {e}")
        raise ValueError(f"在分割图像颜色通道时发生错误: {e}")

def merge_image_channels(file_paths):
    '''
    该函数用于合并多个单通道图像，创建一个多通道图像
    :param file_paths: 包含单通道图像文件路径的列表
    :return: 合并后的多通道图像
    '''
    try:
        logging.info("开始合并图像通道")
        
        # TODO: 想办法加载每个图像文件，然后将它们合并成一个多通道图像 merged_image
        # 注意: 检查每个图像是否是单通道的，如果不是，raise 一个异常信息: 要合并子图像必须是单通道图像，不能是多通道图像
        
        merged_image = 
        
        logging.info("成功合并图像通道")
        return merged_image
    except Exception as e:
        raise ValueError(f"在合并图像通道时发生错误: {e}")