from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
from data.plugins.astrbot_plugin_beautiful_giri.api_collection import video

@register("美女集合", "黄四郎", "美女集合", "1.0.0")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    @filter.command("jk")
    async def mp41(self, event: AstrMessageEvent):
        result = await video.mp4("jk")
        await event.send(result)

    @filter.command("欲梦")
    async def mp42(self, event: AstrMessageEvent):
        result = await video.mp4("YuMeng")
        await event.send(result)


    @filter.command("女大")
    async def mp43(self, event: AstrMessageEvent):
        result = await video.mp4("NvDa")
        await event.send(result)

    @filter.command("女高")
    async def mp44(self, event: AstrMessageEvent):
        result = await video.mp4("NvGao")
        await event.send(result)


    @filter.command("热舞")
    async def mp45(self, event: AstrMessageEvent):
        result = await video.mp4("ReWu")
        await event.send(result)


    @filter.command("清纯")
    async def mp46(self, event: AstrMessageEvent):
        result = await video.mp4("QingCun")
        await event.send(result)


    @filter.command("玉足")
    async def mp47(self, event: AstrMessageEvent):
        result = await video.mp4("YuZu")
        await event.send(result)


    @filter.command("蛇姐")
    async def mp48(self, event: AstrMessageEvent):
        result = await video.mp4("SheJie")
        await event.send(result)


    @filter.command("穿搭")
    async def mp49(self, event: AstrMessageEvent):
        result = await video.mp4("ChuanDa")
        await event.send(result)


    @filter.command("小姐姐")
    async def mp410(self, event: AstrMessageEvent):
        result = await video.mp4("GaoZhiLiangXiaoJieJie")
        await event.send(result)


    @filter.command("汉服")
    async def mp411(self, event: AstrMessageEvent):
        result = await video.mp4("HanFu")
        await event.send(result)


    @filter.command("黑丝")
    async def mp412(self, event: AstrMessageEvent):
        result = await video.mp4("HeiSi")
        await event.send(result)


    @filter.command("变装")
    async def mp413(self, event: AstrMessageEvent):
        result = await video.mp4("BianZhuang")
        await event.send(result)


    @filter.command("萝莉")
    async def mp414(self, event: AstrMessageEvent):
        result = await video.mp4("LuoLi")
        await event.send(result)



    @filter.command("甜妹")
    async def mp415(self, event: AstrMessageEvent):
        result = await video.mp4("TianMei")
        await event.send(result)


    @filter.command("白丝")
    async def mp416(self, event: AstrMessageEvent):
        result = await video.mp4("BaiSi")
        await event.send(result)



    async def terminate(self):
        '''可选择实现 terminate 函数，当插件被卸载/停用时会调用。'''
