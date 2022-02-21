import warnings

import nonebot
from pydantic import BaseSettings


class PlugConfig(BaseSettings):

    bison_config_path: str = ""
    bison_use_pic: bool = False
    bison_use_local: bool = False
    bison_use_forward_pic = True#当图片超过1张时改为合并消息发送
    #bison_browser: str = "local:C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    bison_browser: str = ""
    bison_init_filter: bool = True
    bison_use_queue: bool = True
    bison_outer_url: str = "http://localhost:15556/bison/"
    bison_filter_log: bool = False
    bison_to_me: bool = True

    class Config:
        extra = "ignore"


global_config = nonebot.get_driver().config
plugin_config = PlugConfig(**global_config.dict())
if plugin_config.bison_use_local:
    warnings.warn("BISON_USE_LOCAL is deprecated, please use BISON_BROWSER")
