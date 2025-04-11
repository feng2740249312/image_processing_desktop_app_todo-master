from image_utils import logging # 从image_utils.py中导入logging对象


def crop_image(image, crop_region):
    """
    裁剪图像
    :param image: 输入图像，PIL.Image对象
    :param crop_region: 裁剪区域,格式为(上,下,左,右)
    :return: 裁剪后的图像
    """
    try:
        logging.info(f"开始裁剪图像，裁剪区域,{crop_region}")
        
        # TODO: 从crop_region中提取上、下、左、右的坐标
        
        
        # TODO: 直接使用切片操作，裁剪图像 image 生成裁剪后的图像 cropped_image
        cropped_image = 
        
        return cropped_image
    except Exception as e:
        raise ValueError(f"Error occurred while cropping image: {e}")
    
