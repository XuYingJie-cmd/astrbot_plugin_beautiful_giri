from astrbot.api.all import *
import requests
import aiohttp
import logging
import re
from astrbot.api.message_components import Video

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def mp4(id_value):

    api_url = f"http://api.mmp.cc/api/ksvideo?type=mp4&id={id_value}"
    result = MessageChain()
    result.chain = []
    try:
        logger.info("开始下载")
        async with aiohttp.ClientSession() as session:
            async with session.get(api_url) as response:
                # 记录响应状态码
                logger.info(f"返回结果，状态码: {response}")
                response_str = str(response)
                # 定义正则表达式来提取视频链接
                pattern = r'<ClientResponse\((https?://[^\)]+)\)'
                match = re.search(pattern, response_str)
                if match:
                    video_url = match.group(1)
                    result.chain = [Video.fromURL(video_url)]
                    logger.info(f"视频链接: {video_url}")
                    return result
                else:
                    # 尝试获取原始文本响应
                    text = await response.text()
                    result.chain = [
                        Plain("未从响应中找到视频链接"),
                        Plain(f"原始响应内容: {text}")
                    ]
                    return result
    except aiohttp.ClientError as e:
        result.chain = [Plain(f"请求异常: {e}")]
    return result