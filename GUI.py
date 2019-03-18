from time import *
from threading import *
from tkinter import *
from tkinter.messagebox import *
import tkinter.filedialog
import tkinter.ttk as ttk
from PIL import Image, ImageTk


class my_GUI(object):
    def __init__(self):
        #关键变量
        self.filename = 'car.jpg'
        # 定义参数字典
        # dict_COM没有设置必要，本来就需要用字符串赋值
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


        #先定义frame，避免覆盖
        self.label01 = LabelFrame(self.tk,height=60,width=420,text="Main Switch",labelanchor='n',bg="whitesmoke")
        self.id01=self.canvas.create_window(225,30,window=self.label01)#坐标是正中
        self.label00 = LabelFrame(self.tk,height=60,width=420,text="Parameter Setting",labelanchor='n',bg="whitesmoke")
        self.id00=self.canvas.create_window(225,90,window=self.label00)#坐标是正中


        #信息选择框
        self.City=StringVar()
        self.city = ttk.Combobox(self.tk, width=7,textvariable=self.City,state='readonly')
        self.city['value']=('beijing','chengdu','guiyang','lanzhou','hanghzhou','tianjin','nanchang','haerbin','chongqing','changchun')
        self.city.current(0)

        self.Day = StringVar()#用来盛放从下拉栏中选择的字符串值
        self.day = ttk.Combobox(self.tk, width=7, textvariable=self.Day,state='readonly')
        self.day['values'] = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")#下拉栏的显示内容
        self.day.current(0)

        self.id11=self.canvas.create_window(165, 95,window=self.city)
        self.id12=self.canvas.create_window(370,95,window=self.day)

        #标签
        #要先定义，不然会覆盖，也可以用子配件、父配件来解决label10 = LabelFrame(tk,height=150,width=130,text="串口设置",labelanchor='n',bg="whitesmoke")#labelanchor属性解决定位问题（n:北，nw:西北，center:正中，其余类推）
        self.label11=Label(self.tk,text="Select the City",bg="whitesmoke")
        self.label12=Label(self.tk,text="Select the Day",bg="whitesmoke")

        self.id21=self.canvas.create_window(80,95,window=self.label11)#一个字符大概20*20，标签自动把中点定位到指定的那个坐标
        self.id22=self.canvas.create_window(285,95,window=self.label12)#由于一个标签也有高度，所以不能让标签们靠得太近，否则新加的会覆盖之前的（只要二者有一点点重合）

        #违法驾驶分析开关
        self.Switch_ill = StringVar()
        self.Switch_ill.set("Illegality Analysis")
        self.button41 = Button(self.tk, textvariable=self.Switch_ill, width=25,
                               command=self.Start_illegalityAnalysis())  # button启动的函数不能接受参数，此时使用lambda，先计算函数结果，然后把结果强制重组为一个匿名简单函数
        self.id41 = self.canvas.create_window(325, 35, window=self.button41)

        #车牌号分析开关
        self.Switch_lic = StringVar()
        self.Switch_lic.set('License Number Analysis')
        self.button61 = Button(self.tk, textvariable=self.Switch_lic, width=25,
                               command=self.Start_licenseNumberAnalysis())  # button启动的函数不能接受参数，此时使用lambda，先计算函数结果，然后把结果强制重组为一个匿名简单函数
        self.id61 = self.canvas.create_window(120, 35, window=self.button61)

        # 图片栏
        self.label81 = LabelFrame(self.tk, height=290, width=420, text="Image Window", labelanchor='n', bg="whitesmoke")
        self.id81 = self.canvas.create_window(225, 265, window=self.label81)  # 坐标是正中

        #选择图片开关
        self.Switch_sel = StringVar()
        self.Switch_sel.set("Select an Image")
        self.button91 = Button(self.tk, textvariable=self.Switch_sel, width=25,
                               command=self.Start_selectingImage)  # button启动的函数不能接受参数，此时使用lambda，先计算函数结果，然后把结果强制重组为一个匿名简单函数
        self.id91 = self.canvas.create_window(120, 160, window=self.button91)

        #消除图片开关
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



    '''def Start_serial_launcher():
        th=Thread(target=Start_serial,args=())
        th.setDaemon(TRUE)
        th.start()
    '''
    def Start_illegalityAnalysis(self):
        try:
            pass
        except:
            showwarning("错误！", "检查串口设置并重置总开关")


    def Start_licenseNumberAnalysis(self):
        pass



    #插图显示
    def resize(self, w_box, h_box, pil_image): #参数是：要适应的窗口宽、高、Image.open后的图片
        w, h = pil_image.size #获取图像的原始大小
        f1 = 1.0*w_box/w
        f2 = 1.0*h_box/h
        factor = min([f1, f2])
        width = int(w*factor)
        height = int(h*factor)
        return pil_image.resize((width, height), Image.ANTIALIAS)


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
        except:
            pass



    def Start_removingImage(self):
        try:
            self.label111 = Label(self.tk, width=50, height=13, bg="whitesmoke")
            self.canvas.create_window(225, 290, window=self.label111)
        except:
            pass

if __name__=='__main__':
    my_gui=my_GUI()
    my_gui.tk.mainloop()

