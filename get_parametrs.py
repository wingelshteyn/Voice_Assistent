import extract_parametrs


def get_parametrs(func_name, data):
    if func_name == 'random_num':
        return extract_parametrs.random_range_parametrs(data)
    if func_name == 'search_in_youtube':
        return extract_parametrs.youtube_query(data)
    if func_name == 'open_app':
        return extract_parametrs.open_app_query(data)
    if func_name == 'count':
        return extract_parametrs.count_parametrs(data)
    if func_name == 'timer':
        return extract_parametrs.timer_parametr(data)
