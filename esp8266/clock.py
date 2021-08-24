from machine import RTC;
import ntptime;

def toDoubleStr(n):
    return "0" + str(n) if n < 10 else str(n);

def initMachineTime():
    ntptime.NTP_DELTA = 3155644800   # UTC+8偏移时间（秒），不设置就是UTC0
    ntptime.host = "ntp1.aliyun.com"  # ntp服务器，默认是"pool.ntp.org"
    ntptime.settime();               # 修改设备时间

def getCurrentTime():
    rtc = RTC();
    timeTup = rtc.datetime();
    timeList = list(timeTup);
    Y = str(timeList[0]);
    M = toDoubleStr(timeList[1]);
    D = toDoubleStr(timeList[2]);
    h = toDoubleStr(timeList[4]);
    m = toDoubleStr(timeList[5]);
    s = toDoubleStr(timeList[6]);
    return {
        "date": Y + "/" + M + "/" + D,
        "time": h + ":" + m + ":" +s
    }
