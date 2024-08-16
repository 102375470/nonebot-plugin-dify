from typing import List, Literal, Optional, Union, Set

from nonebot import get_plugin_config
from pydantic import BaseModel


class Config(BaseModel):
    dify_api_base: str = "https://api.dify.ai/v1"
    dify_api_key: str = "app-xxx"
    dify_app_type: str = "chatbot"
    """dify助手类型 chatbot(对应聊天助手)/agent(对应Agent)/workflow(对应工作流)，默认为chatbot"""
    
    dify_convsersation_max_messages: int = 20
    """dify目前不支持设置历史消息长度，暂时使用超过最大消息数清空会话的策略，缺点是没有滑动窗口，会突然丢失历史消息"""

    dify_ignore_prefix: Set[str] = ["/", "."]
    """忽略词，指令以本 Set 中的元素开头不会触发词库回复"""

    dify_expires_in_seconds: int = 3600

    dify_image_upload_enable: bool = False

    dify_image_cache_dir: str = "tmp"


config = get_plugin_config(Config)