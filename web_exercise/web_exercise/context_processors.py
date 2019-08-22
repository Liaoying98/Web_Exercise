# 全局上下文管理器
def base_date(request):
    current_url = request.path
    return locals()
