# nonebot-plugin-dify


## 📖 介绍

基于 [NoneBot2](https://github.com/nonebot/nonebot2)，该插件用于对接LLMOps平台[Dify](https://github.com/langgenius/dify)。

## 💿 安装

### 使用 nb-cli 安装

在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-dify



### 使用包管理器安装

在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令


如pip

    pip install nonebot-plugin-dify

然后打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

    plugins = ["nonebot_plugin_dify"]



## ⚙️ 配置

在 nonebot2 项目的`.env`文件中添加下表中的配置

| 配置项 | 必填 | 默认值 | 说明 |
|:-----:|:----:|:----:|:----:|
| DIFY_API_BASE | 否 | https://api.dify.ai/v1 | DIFY API地址 |
| DIFY_API_KEY | 是 | 无 | DIFY API KEY |
| DIFY_APP_TYPE | 否 | chatbot | DIFY APP 类型 |
| DIFY_IMAGE_UPLOAD_ENABLE | 否 | False | 是否开启上传图片 |
| DIFY_EXPIRES_IN_SECONDS | 否 | 3600 | 会话过期时间 |

## 🎉 使用
### 对接不同的Bot

.env

```
# 对接ONEBOT
ONEBOT_ACCESS_TOKEN=xxxxxx

# 对接TELEGRAM
TELEGRAM_BOTS=[{"token": "1111:xxxx"}]

# 对接DISCORD
DISCORD_BOTS=[{"token": "xxxxxxxxxxxxx"}]
```

### 效果图
