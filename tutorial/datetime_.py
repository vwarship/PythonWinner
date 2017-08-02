from datetime import datetime, date


"""获得两个日期的间隔天数"""
begin_date = date(2017,7,1)
end_date = date(2017,7,20)
time_delta = end_date - begin_date
days = time_delta.days  # 19
