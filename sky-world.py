import turtle
import streamlit as st
from PIL import Image
import random
import time

#python -m streamlit run

lk = st.empty()
l = st.empty()
k = st.empty()




page = ''
po = lk.title('家庭互联网')
p = l.text_input('输入账户名：')
o = k.text_input('输入密码：', type='password')




if p == 'zcr130423' and o == '130423':
    page = st.sidebar.selectbox('选择', ['首页', '我的图片处理工具', '我的智能词典', '我的留言区', '软件下载'])
    with st.sidebar:
        paage = st.success('登录成功')
    l.empty()
    k.empty()
    lk.empty()




def page1():
    st.title('首页(*^▽^*)')
    #with open('M500004J8dYm0RZCA3.mp3')
    ac = st.radio(label = '今天心情怎么样啊(❁´◡`❁)', options = ('好','一般','差！','不告诉你'))
    if (ac == '好'):
        st.write('HAPPY！')
    elif (ac == '一般') :
        st.write('开心一点qwq')
    elif (ac == '差！') :
        st.write('别生气了嘛o(≧▽≦)o')
    else :
        st.write('§(*￣▽￣*)§')
    ae = st.selectbox(label = '想看什么啊(❁´◡`❁)', options = ('音乐推荐','炸机视频'))
    ase1 = '68214280-1-208.mp4'
    ase2 = '500001660406903-1-192.mp4'
    fr = ase1
    if (ae == '炸机视频'):
        if st.button('换一个'):
            fr = ase2
        st.video(fr,format='video/mp4')
    else :
        st.write(':green[sw音乐推荐----------------------------------------------------------------------------------------------------------------------------]')
        st.write(':red[1.Counting stars - OneRepublic]')
        audio_file = open('M500004J8dYm0RZCA3.mp3', 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/mp3')
        st.write(':orange[2.Everywhere We Go - cooperate]')
        audio_filesss = open('3339297160.mp3', 'rb')
        audio_bytesss = audio_filesss.read()
        st.audio(audio_bytesss, format='audio/mp3')
        st.write(':blue[3.Letting Go - 蔡健雅]')
        audio_file1 = open('123.mp3', 'rb')
        audio_bytes1 = audio_file1.read()
        st.audio(audio_bytes1, format='audio/mp3')

def page2():
    st.title(":sunglasses:图片处理小程序:sunglasses:")
    uploaded_file = st.file_uploader("上传图片", type=['png', 'jpeg', 'jpg'])
    if uploaded_file:
        # 获取图片文件的名称、类型和大小
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        # 显示图片处理界面
        col1, col2, col3 = st.columns([4, 1, 1])
        with col1:
            st.image(img)
        with col2:
            ch = st.toggle('反色滤镜')
            co = st.toggle('增强对比度')
            bw = st.toggle('黑白滤镜')
        with col3:
            st.write('对图片进行反色处理')
            st.write('让图片颜色更加鲜艳')
            st.write('将图片变为灰度图')
        # 点击按钮处理图片
        st.success(':white_check_mark:成功加载图片:white_check_mark:')
        b = st.button('开始处理')
        t = st.text_input('请输入文件名：', max_chars=50, help='输入下载的图片文件名')
        t = t + '.png'
        if b:
            sdf = st.progress(0,text='处理中……0%')
            if ch:
                sdf.progress(50,text='处理中……50%')
                img = img_change_ch(img)
            if co:
                sdf.progress(50,text='处理中……50%')
                img = img_change_co(img)
            if bw:
                sdf.progress(50,text='处理中……50%')
                img = img_change_bw(img)
            st.image(img)
            sdf.progress(100,text=':white_check_mark:处理成功-100%:white_check_mark:')
            st.success(':white_check_mark:处理成功:white_check_mark:')
            a = random.randint(1,999999)
            a = str(a)
            s = a + '.png'
            r = './config/' + s
            img.save(r, format='png')
            with open('./config/' + s, 'rb') as asdasd:
                st.download_button(label='下载图片', data=asdasd, file_name=t, mime='photo/png')
            




def page3():
    st.title('智能小词典')
    with open('words_space.txt', 'r', encoding='utf-8') as f:
        words_list = f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]

    with open('check_out_times.txt', 'r', encoding='utf-8') as f:
        time_list = f.read().split('\n')

    for i in range(len(time_list)):
        time_list[i] = time_list[i].split('#')
    times_dict = {}
    for i in time_list:
        times_dict[int(i[0])] = int(i[1])
    word = st.text_input('请输入要查询的单词：')
    defsf = st.button('查询')

    if defsf:
        if word in words_dict:
            st.write(words_dict[word])
            n = words_dict[word][0]
            if n in times_dict:
                times_dict[n] += 1
            else:
                times_dict[n] = 1
            with open('check_out_times.txt', 'w', encoding='utf-8') as f:
                message = ''
                for k, v in times_dict.items():
                    message += str(k) + '#' + str(v) + '\n'
                message = message[:-1]
                f.write(message)
            st.write('查询次数：', times_dict[n])
            if word == 'SB':
                st.error('尼玛撒比，nmsb，nmsb，nmsb')
            if word == 'ikun':
                st.balloons()
            if word == 'python':
                st.snow()
        else:
            st.error('无法识别')


def page4():
    st.title('我的留言区')
    with open('leave_messages.txt', 'r', encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        if i[1] == '阿短':
            with st.chat_message('🙂'):
                st.write(i[1],':',i[2])
        elif i[1] == '编程猫':
            with st.chat_message('😍'):
                st.write(i[1],':',i[2])
        elif i[1] == '妈妈':
            with st.chat_message('😁'):
                st.write(i[1],':',i[2])
        elif i[1] == 'ikun':
            with st.chat_message('🐔'):
                st.write(i[1],':',i[2])
    name = st.selectbox('我是……', ['阿短', '编程猫', '妈妈', 'ikun'])
    new_message = st.text_input('我来说：')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
        with open('leave_messages.txt', 'w', encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)

def page5():
    st.title(':blue[软件下载~]')
    tyt = st.selectbox('选择软件种类', ['生活类', '飞行器类', '模拟飞行类', '媒体类'])
    if tyt == '生活类':
        c1,c2,c3 = st.columns([1, 1, 1])
        with c1:
            st.link_button('淘宝（暂时不支持下载~）', url='https://uland.taobao.com/sem/tbsearch?clk1=51e76d9e513f7733c16c0af0bc0fc92c&keyword=%E7%B2%AE%E6%B2%B9%E7%B1%B3%E9%9D%A2&localImgKey=&msclkid=d97899d676a712d64c4afe7fd50550f5&page=1&q=&refpid=mm_2898300158_3078300397_115665800437&tab=all&upsId=51e76d9e513f7733c16c0af0bc0fc92c')
        with c2:
            st.link_button('Edge', url='https://go.microsoft.com/fwlink/?linkid=2109047&Channel=Stable&language=zh-cn&brand=M100')
        with c3:
            st.link_button('Bandizip(解压缩软件)', url='https://www.bandisoft.com/bandizip/dl.php?web')
    if tyt == '飞行器类':
        q1, q2, q3 = st.columns([1, 1, 1])
        with q1:
            st.link_button('DJI FLY APP(大疆飞行软件)', url='https://www.dji.com/cn/downloads/djiapp/dji-fly')
        with q2:
            st.link_button('飞常准', url='http://www.variflight.com/lite?AE71649A58c77')
        with q3:
            st.link_button('大疆商城', url='https://www.dji.com/cn/downloads/djiapp/dji-store')
    if tyt == '模拟飞行类':
        e1, e2, e3 = st.columns([1, 1, 1])
        with e1:
            st.link_button('X-Plane11', url='https://www.bilibili.com/opus/440272416000452020')
        with e2:
            st.link_button('大疆虚拟飞行', url='https://www.dji.com/cn/downloads/djiapp/dji-virtual-flight-cn')
        with e3:
            st.link_button('liftoff', url='https://www.liftoff-game.com/')
    if tyt == '媒体类':
        w1, w2, w3 = st.columns([1, 1, 1])
        with w1:
            st.link_button('哔哩哔哩', url='https://app.bilibili.com/?spm_id_from=333.1007.0.0')
        with w2:
            st.write('     ')
        with w3:
            st.link_button('网易云音乐', url='https://music.163.com/#/download')
    st.title(':sunglasses:晨晨软件园:sunglasses:')
        
    
    
def img_change_ch(img):
    '''图片反色滤镜'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            # 获取RGB值，反色处理
            r = 255 - img_array[x, y][0]
            g = 255 - img_array[x, y][1]
            b = 255 - img_array[x, y][2]
            img_array[x, y] = (r, g, b)
    return img

def img_change_co(img):
    '''增强对比度滤镜'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            # 获取RGB值
            r = img_array[x, y][0]
            g = img_array[x, y][1]
            b = img_array[x, y][2]
            # RGB值中，哪个更大，就再大一些
            if r == max(r, g, b):
                if r >= 200:
                    r = 255
                else:
                    r += 55
            elif g == max(r, g, b):
                if g >= 200:
                    g = 255
                else:
                    g += 55
            else:
                if b >= 200:
                    b = 255
                else:
                    b += 55
            img_array[x, y] = (r, g, b)
    return img

def img_change_bw(img):
    '''图片黑白滤镜'''
    img = img.convert('L') # 转换为灰度图
    return img




#转换为灰度图


if (page == '首页'):
    page1()

if (page == '我的图片处理工具'):
    page2()

if (page == '我的智能词典'):
    page3()

if (page == '我的留言区'):
    page4()

if (page == '软件下载'):
    page5()