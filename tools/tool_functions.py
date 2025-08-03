def check_blacklist(user_id: str) -> str:
    if user_id.startswith("black"):
        return f"用户 {user_id} 在黑名单中"
    return f"用户 {user_id} 不在黑名单"

def get_user_profile(user_id: str) -> str:
    return f"用户画像：{user_id}，风险等级中等，近期交易频繁"