from machine import Pin
from tools import connect,reconnect
import time
import urequests

red_led = Pin(15,mode=Pin.OUT)
btn = Pin(14,mode=Pin.PULL_DOWN)
is_press = False
#connect()

def getCurrentTime():
    times_tuple = time.localtime()
    currentTime = f'{times_tuple[0]}-{times_tuple[1]}-{times_tuple[2]} {times_tuple[3]}:{times_tuple[4]}:{times_tuple[5]}'
    return currentTime

def getTemperature():
    sensor_temp = machine.ADC(4)
    conversion_factor = 3.3 / (65535)
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721
    return temperature

while True:
    if btn.value():
        #解決按下彈跳
        time.sleep_ms(50)
        if btn.value():
            is_press = True
            red_led.value(1)
    else:
        #解決放開彈跳
        time.sleep_ms(50)
        if btn.value() == False:
            if is_press == True:     
                print('release')                
                print(getCurrentTime())
                print(getTemperature())
                is_press = False
                '''
                url_str = 'https://openapi-test-oshv.onrender.com/pico_w/2024-01-22 16:02:10?address=chicken_KFC&celsius=15.386'
                try:
                    response = urequests.get(url_str)
                    pass
                except:
                    print("ap出現問題")            
                    reconnect()
                else:
                    if response.status_code == 200:            
                        print("傳送訊息成功")
                    else:
                        print("傳送失敗(server出現錯誤)")
                    response.close()
                '''
            
        
            red_led.value(0)
        