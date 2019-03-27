from time import *
from threading import *
from tkinter import *
from tkinter.messagebox import *
import tkinter.filedialog
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from datetime import *
from collections import Iterable
from lpnAnalysis.lpnAnalyze import *
from lpnAnalysis.lpnRestrictionInves import *

#my_GUI类包含了GUI创建所需一切内容
class my_GUI(object):
    def __init__(self):
        self.myday=datetime.now().strftime('%A')#获取时间

        #定义两个API调用类，前一个用来联网识别车牌号，后一个用来联网查询尾号限行信息
        self.api_lpn=API_lpn()
        self.api_ill=API_illegality()

        #关键变量filename，用于存储用户选择的图片的路径
        self.filename = 'car.jpg'

        self.dict_Day = {"Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4, "Friday": 5, "Saturday": 6, "Sunday": 7}

        #GUI初始化
        self.tk=Tk()
        self.tk.title("License Plate Number & Illegal Driving Analysis")
        self.tk.maxsize(450,580)#（宽度，高度）
        self.tk.minsize(450,580)
        self.tk.resizable(width = False, height = False)
        self.tk.iconbitmap("./wheel.ico")
        self.canvas=Canvas(self.tk,width=450,height=580,bg='whitesmoke')
        self.canvas.pack()


        self.label01 = LabelFrame(self.tk,height=60,width=420,text="Main Switch",labelanchor='n',bg="whitesmoke")
        self.id01=self.canvas.create_window(225,30,window=self.label01)#坐标是正中
        self.label00 = LabelFrame(self.tk,height=60,width=420,text="Parameter Setting",labelanchor='n',bg="whitesmoke")
        self.id00=self.canvas.create_window(225,90,window=self.label00)#坐标是正中


        #信息（城市、星期数）选择框
        self.City=StringVar()
        self.city = ttk.Combobox(self.tk, width=7,textvariable=self.City,state='readonly')
        self.city['value']=('beijing','chengdu','guiyang','lanzhou','hanghzhou','tianjin','nanchang','haerbin','chongqing','changchun')
        self.city.current(0)

        self.Day = StringVar()
        self.day = ttk.Combobox(self.tk, width=7, textvariable=self.Day,state='readonly')
        self.day['values'] = ("today", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")#下拉栏的显示内容
        self.day.current(0)

        self.id11=self.canvas.create_window(165, 95,window=self.city)
        self.id12=self.canvas.create_window(370,95,window=self.day)

        #选择框的标签
        self.label11=Label(self.tk,text="Select the City",bg="whitesmoke")
        self.label12=Label(self.tk,text="Select the Day",bg="whitesmoke")

        self.id21=self.canvas.create_window(80,95,window=self.label11)#一个字符大概20*20，标签自动把中点定位到指定的那个坐标
        self.id22=self.canvas.create_window(285,95,window=self.label12)#由于一个标签也有高度，所以不能让标签们靠得太近，否则新加的会覆盖之前的（只要二者有一点点重合）

        #违法驾驶分析功能按钮
        self.Switch_ill = StringVar()
        self.Switch_ill.set("Illegality Analysis")
        self.button41 = Button(self.tk, textvariable=self.Switch_ill, width=25,
                               command=self.Start_illegalityAnalysis)  # button启动的函数不能接受参数，此时使用lambda，先计算函数结果，然后把结果强制重组为一个匿名简单函数
        self.id41 = self.canvas.create_window(325, 35, window=self.button41)

        #车牌号分析功能按钮
        self.Switch_lic = StringVar()
        self.Switch_lic.set('License Number Analysis')
        self.button61 = Button(self.tk, textvariable=self.Switch_lic, width=25,
                               command=self.Start_licenseNumberAnalysis)  # button启动的函数不能接受参数，此时使用lambda，先计算函数结果，然后把结果强制重组为一个匿名简单函数
        self.id61 = self.canvas.create_window(120, 35, window=self.button61)

        # 图片栏
        self.label81 = LabelFrame(self.tk, height=290, width=420, text="Image Window", labelanchor='n', bg="whitesmoke")
        self.id81 = self.canvas.create_window(225, 265, window=self.label81)  # 坐标是正中

        #选择图片功能按钮
        self.Switch_sel = StringVar()
        self.Switch_sel.set("Select an Image")
        self.button91 = Button(self.tk, textvariable=self.Switch_sel, width=25,
                               command=self.Start_selectingImage)  # button启动的函数不能接受参数，此时使用lambda，先计算函数结果，然后把结果强制重组为一个匿名简单函数
        self.id91 = self.canvas.create_window(120, 160, window=self.button91)

        #消除图片功能按钮
        self.Switch_rem = StringVar()
        self.Switch_rem.set('Remove the image')
        self.button101 = Button(self.tk, textvariable=self.Switch_rem, width=25,
                                command=self.Start_removingImage)  # button启动的函数不能接受参数，此时使用lambda，先计算函数结果，然后把结果强制重组为一个匿名简单函数
        self.id101 = self.canvas.create_window(325, 160, window=self.button101)

        #日志显示
        self.label121 = LabelFrame(self.tk, height=150, width=420, text="Log", labelanchor='n', bg="whitesmoke")
        self.id121 = self.canvas.create_window(225, 490, window=self.label121)  # 坐标是正中

        self.logText = Text(self.tk, width=55, height=8)
        self.canvas.create_window(225, 495, window=self.logText)

        '''showinfo("NOTE","It is my honor to have this APP used by you guys!\n"
                    "Select an image file, set the two parameters,\n"
                    "And you can:\n"
                    "1.Analyze the license number in the picture\n"
                    "2.Analyze whether the car is illegally driven\n"
                    "(specifically,with a restricted rear number)")
        '''

    #使用多线程的代码
    '''def Start_serial_launcher():
        th=Thread(target=Start_serial,args=())
        th.setDaemon(TRUE)
        th.start()
    '''

    #日志更新函数:更新日志信息并保持指针在最新行
    def log_print(self,string):
        self.logText.insert(INSERT,string)
        self.logText.see(END)

    #开始进行违规驾驶分析：访问提供限号信息的API
    def Start_illegalityAnalysis(self):
        #提示选择文件
        if not self.filename:
            showwarning("Warning", "Choose an image file first!")
            return
        try:
            #API需要的星期数由1~7表示，同时1表示今天，2表示明天，以此类推，所以需要数字标号的换算
            if self.Day.get()!='today':
                #query()在文件lpnRestrctionInves.py中的API_illegality类中定义
                #query()函数用于直接访问API，一个参数是城市，一个是相对星期数
                self.api_ill.query(self.City.get(), (self.dict_Day[self.Day.get()]+8-self.dict_Day[self.myday])%7)
            else:
                self.api_ill.query(self.City.get(), 1)

            #在日志中显示尾号限行信息
            self.log_print('Rear number restriction inquiry:\n'+"city:"+self.City.get()+"\n")
            if self.Day.get()=='today':
                self.log_print("Day:"+self.myday+'\n')
            else:
                self.log_print("Day:" + self.Day.get()+'\n')
            self.log_print("\nRestricted number: ")

            if self.api_ill.queryResult["isxianxing"]:#如果这一天有限行的话
                for n in self.api_ill.queryResult["xxweihao"]:
                    self.log_print(str(n)+' ')
            else:#这一天无限行
                self.log_print("No restriction in this day")

            #根据API返回的尾号限行数据，判断刚才识别到的车牌号在用户指定的地点、时间是否违规
            self.log_print("\n\nIllegality detection:\n")
            #如果有多个车牌的话，依次显示判断结果
            if self.api_ill.queryResult["isxianxing"]:#如果这一天有限行
                for value in self.api_lpn.queryResult['words_result']:
                    self.log_print("Plate "+value['number']+':')
                    if int(value["number"][-1]) in self.api_ill.queryResult['xxweihao']:
                        self.log_print(" illegal\n")
                    else:
                        self.log_print(" legal\n")
                self.log_print('\n')
            else:
                self.log_print('No car is illegally driven\n')
        except:
            pass

    #车牌号分析函数，访问百度云智能的图片识别API，可以识别图片中的车牌号
    def Start_licenseNumberAnalysis(self):
        try:
            if not self.filename:
                #提示用户选择文件
                showwarning("Warning","Choose an image file first!")
            else:
                self.api_lpn.connect(self.filename)
                self.log_print("license plate number analyzing result:\n")
                #出错处理
                if "error_code" in self.api_lpn.queryResult:
                    self.log_print("No plates detected!\n\n")
                else:
                    #在log显示框中挨个儿打印识别到的车牌号
                    for n in self.api_lpn.queryResult['words_result']:
                        print(n['number'])
                        self.log_print(n['number']+'\n')
                    self.log_print('\n')
        except:
            pass



    #插图显示部分
    #resize用于调整图片大小
    def resize(self, w_box, h_box, pil_image): #参数是：要适应的窗口宽、高、Image.open后的图片
        w, h = pil_image.size #获取图像的原始大小
        f1 = 1.0*w_box/w
        f2 = 1.0*h_box/h
        factor = min([f1, f2])
        width = int(w*factor)
        height = int(h*factor)
        return pil_image.resize((width, height), Image.ANTIALIAS)

    #选择图片并显示
    def Start_selectingImage(self):
        try:
            self.filename=tkinter.filedialog.askopenfilename()
            print(self.filename)
            # 用canvas.create_iamge显示图片的话好像会被放到底层去

            self.img_open = Image.open(self.filename)
            self.img_open = self.resize(300, 200, self.img_open)
            self.img_jpg = ImageTk.PhotoImage(self.img_open)
            self.label_img = Label(self.tk, image=self.img_jpg)
            self.canvas.create_window(225, 290, window=self.label_img)
            self.log_print("You have selected file:" + self.filename + '\n\n')
        except:
            pass


    #清楚显示地图片并取消选择
    def Start_removingImage(self):
        try:
            self.log_print("You have removed the latest image!\n\n")
            self.label111 = Label(self.tk, width=50, height=13, bg="whitesmoke")
            self.canvas.create_window(225, 290, window=self.label111)
            self.filename=''
        except:
            pass

if __name__=='__main__':
    my_gui=my_GUI()
    my_gui.tk.mainloop()

