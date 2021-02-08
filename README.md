# hk-reporter  通用订阅推送插件

## 简介
一款自动爬取各种站点，社交平台更新动态，并将信息推送到QQ的机器人。基于 [`NoneBot2`](https://github.com/nonebot/nonebot2 ) 开发（诞生于明日方舟的蹲饼活动）

支持的平台：
* 微博
    * 图片
    * 文字
    * 不支持视频
    * 不支持转发的内容
* bilibili
    * 图片
    * 专栏
    * 文字
    * 视频链接
    * 不支持转发的内容
* rss
    * 从description中提取图片
    * 文字

## 使用方法

### 使用以及部署
本项目可作为单独插件使用（绝对simple和stupid），也可直接克隆项目进行使用  
作为插件使用请安装`nonebot-hk-reporter`包，并在`bot.py`中加载`nonebot_hk_reporter`插件；或直接克隆本项目进行使用  
配置与安装请参考[nonebot2文档](https://v2.nonebot.dev/)

### 配置变量
* `HK_REPORTER_CONFIG_PATH` 配置文件保存目录，如果不设置，则为当前目录下的`data`文件夹
* `HK_REPORTER_USE_PIC` 以图片形式发送文字（推荐在帐号被风控时使用）
* `HK_REPORTER_USE_LOCAL` 使用本地chromium（文字转图片时需要），否则第一次启动会下载chromium

### 命令
所有命令都需要@bot触发
* 添加订阅（仅管理员和群主）：`添加订阅 [平台代码] uid`
* 查询订阅：`查询订阅`
* 删除订阅（仅管理员和群主）：`删除订阅 [平台代码] uid`

平台代码包含：weibo，bilibili，rss
### 文字转图片
因为可能要发送长文本，所以bot很可能被风控，如有需要请开启以图片形式发送文字，本项目使用的图片转文字方法是chromium（经典杀鸡用牛刀）。

如果确定要开启推荐自行安装chromium，设置使用本地chromium，并且保证服务器有比较大的内存。
## 功能
* 定时爬取制定网站
* 通过图片发送文本，防止风控
* 使用队列限制发送频率

## 鸣谢
* [`go-cqhttp`](https://github.com/Mrs4s/go-cqhttp)：简单又完善的 cqhttp 实现
* [`NoneBot2`](https://github.com/nonebot/nonebot2)：超好用的开发框架
* [`HarukaBot`](https://github.com/SK-415/HarukaBot/): 借鉴了大体的实现思路

## License
MIT
