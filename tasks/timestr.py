__all__ = (
    'seconds_to_str',
)
def seconds_to_str(seconds: int) -> str:
    """
    Функция должна вернуть текстовое представление времени
    20 -> 20s
    60 -> 01m00s
    65 -> 01m05s
    3700 -> 01h01m40s
    93600 -> 01d02h00m00s
    """
    #raise NotImplementedError
    bagseconds=seconds
    time=''
    time=time_quant(time, bagseconds, 86400, 'd')
    bagseconds=bagseconds%86400
    time=time_quant(time, bagseconds, 3600, 'h')
    bagseconds=bagseconds%3600
    time=time_quant(time, bagseconds, 60, 'm')
    if bagseconds==0:
      time=time+'00s'
    else:
      bagseconds=bagseconds%60
      time=time+f'{bagseconds:02}s'
    return time

def time_quant(qtime: str, remain: int, quant: int, stringadd: str) -> str :
    if (qtime !='' or remain//quant > 0):
        qtime=qtime+f'{remain//quant:02}{stringadd}'
    return qtime