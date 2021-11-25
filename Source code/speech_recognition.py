#_*_ coding:UTF-8 _*_
# @author: jacky
# 百度云语音识别Demo，实现对本地语音文件的识别。
# 需安装好python-SDK，录音文件不不超过60s，文件类型为wav格式。
# 音频参数需设置为 单通道 采样频率为16K PCM格式 可以先采用官方音频进行测试

# 导入AipSpeech  AipSpeech是语音识别的Python SDK客户端
from aip import AipSpeech
import os
import importlib,sys

importlib.reload(sys)
#sys.setdefaultencoding('utf8')

''' 你的APPID AK SK  参数在申请的百度云语音服务的控制台查看'''
APP_ID = '23476240'
API_KEY = 'XXH3nkO18oDqrerZTuvlMvc3'
SECRET_KEY = 'PMf0mbamURxetU1aoxH5uXttvzi36uj7'

# 新建一个AipSpeech
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


# 读取文件
def get_file_content(filePath):   #filePath  待读取文件名
    with open(filePath, 'rb') as fp:
        return fp.read()

        
def stt(filename, lan="中文"):         # 语音识别
    # 识别本地文件
    piddict = {"中文":1537, "英文":1737, "英语":1737}
    print('语言码是', piddict[lan])
    result = client.asr(get_file_content(filename),
                        'wav',
                        16000,
                        {'dev_pid': piddict[lan],}      # dev_pid参数表示识别的语言类型 1536表示普通话
                        )
    # print (result)

    # 解析返回值，打印语音识别的结果
    if result['err_msg']=='success.':
        word = result['result'][0].encode('utf-8')       # utf-8编码
        if word!='':
            if word[len(word)-3:len(word)]=='，':
                #print (word[0:len(word)-3])
                with open('demo.txt','w') as f:
                    f.write(word[0:len(word)-3])
                f.close()
                return word[0:len(word)-3]
            else:
                #print(bytes.decode(word))
                with open('demo.txt','w') as f:
                    f.write(bytes.decode(word))
                f.close()
                return bytes.decode(word)
        else:
            print ("音频文件不存在或格式错误")
    else:
        print ("错误")
    return None

# main函数 识别本地录音文件yahboom.wav
if __name__ == '__main__':
    stt('test.wav')
    
