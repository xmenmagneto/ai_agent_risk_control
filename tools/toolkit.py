from langchain.tools import Tool
from tools.tool_functions import check_blacklist, get_user_profile
from schemas.tool_schemas import BlacklistCheckInput, UserProfileInput

tools = [
    Tool.from_function(
        func=check_blacklist,
        name="check_blacklist",
        description="检查用户是否在黑名单中",
        args_schema=BlacklistCheckInput
    ),
    Tool.from_function(
        func=get_user_profile,
        name="get_user_profile",
        description="获取用户画像信息",
        args_schema=UserProfileInput
    )
]