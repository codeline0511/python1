def convert_time(s):
    h = s // 3600
    s %= 3600

    m = s // 60
    s %= 60
    
    print(h+m+s, "초는", h, "시간", m, "분", s, "초이다.")


def get_integer(n):
    a = int(input(n))
    return a

sec = get_integer("변환하고자 하는 시간(초)?")
convert_time(sec)
