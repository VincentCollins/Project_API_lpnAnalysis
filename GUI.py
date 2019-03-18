from time import *
from threading import *
from tkinter import *
from tkinter.messagebox import *
import tkinter.filedialog
import tkinter.ttk as ttk
from PIL import Image, ImageTk

#定义参数字典
#dict_COM没有设置必要，本来就需要用字符串赋值
dict_Day={"Monday":1, "Tuesday":2, "Wednesday":3, "Thursday":4, "Friday":5, "Saturday":6, "Sunday":7}

#GUI初始化
tk=Tk()
tk.title("License Plate Number & Illegal Driving Analysis")
tk.maxsize(450,580)#（宽度，高度）
tk.minsize(450,580)
tk.resizable(width = False, height = False)
tk.iconbitmap("./wheel.ico")
canvas=Canvas(tk,width=450,height=580,bg='whitesmoke')
canvas.pack()


#先定义frame，避免覆盖
label01 = LabelFrame(tk,height=60,width=420,text="Main Switch",labelanchor='n',bg="whitesmoke")
id01=canvas.create_window(225,30,window=label01)#坐标是正中
label00 = LabelFrame(tk,height=60,width=420,text="Parameter Setting",labelanchor='n',bg="whitesmoke")
id00=canvas.create_window(225,90,window=label00)#坐标是正中


#信息选择框
City=StringVar()
city = ttk.Combobox(tk, width=7,textvariable=City,state='readonly')
city['value']=('beijing','chengdu','guiyang','lanzhou','hanghzhou','tianjin','nanchang','haerbin','chongqing','changchun')
city.current(0)

Day = StringVar()#用来盛放从下拉栏中选择的字符串值
day = ttk.Combobox(tk, width=7, textvariable=Day,state='readonly')
day['values'] = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")#下拉栏的显示内容
day.current(0)

id11=canvas.create_window(165, 95,window=city)
id12=canvas.create_window(370,95,window=day)

#标签
#要先定义，不然会覆盖，也可以用子配件、父配件来解决label10 = LabelFrame(tk,height=150,width=130,text="串口设置",labelanchor='n',bg="whitesmoke")#labelanchor属性解决定位问题（n:北，nw:西北，center:正中，其余类推）
label11=Label(tk,text="Select the City",bg="whitesmoke")
label12=Label(tk,text="Select the Day",bg="whitesmoke")

id21=canvas.create_window(80,95,window=label11)#一个字符大概20*20，标签自动把中点定位到指定的那个坐标
id22=canvas.create_window(285,95,window=label12)#由于一个标签也有高度，所以不能让标签们靠得太近，否则新加的会覆盖之前的（只要二者有一点点重合）

#总开关
Switch_ill = StringVar()
Switch_ill.set("Illegality Analysis")

'''def Start_serial_launcher():
    th=Thread(target=Start_serial,args=())
    th.setDaemon(TRUE)
    th.start()
'''
def Start_illegalityAnalysis():
    try:
        pass
    except:
        showwarning("错误！", "检查串口设置并重置总开关")


button41 = Button(tk, textvariable=Switch_ill, width=25,command=Start_illegalityAnalysis())#button启动的函数不能接受参数，此时使用lambda，先计算函数结果，然后把结果强制重组为一个匿名简单函数
id41 = canvas.create_window(325, 35, window=button41)

#搜索串口
Switch_lic=StringVar()
Switch_lic.set('License Number Analysis')
def Start_licenseNumberAnalysis():
    pass


button61 = Button(tk, textvariable=Switch_lic, width=25,command=Start_licenseNumberAnalysis())#button启动的函数不能接受参数，此时使用lambda，先计算函数结果，然后把结果强制重组为一个匿名简单函数
id61 = canvas.create_window(120, 35, window=button61)



#插图按钮
label81 = LabelFrame(tk,height=290,width=420,text="Image Window",labelanchor='n',bg="whitesmoke")
id81=canvas.create_window(225,265,window=label81)#坐标是正中
Switch_sel = StringVar()
Switch_sel.set("Select an Image")

def Start_selectingImage():
    try:
        filename=tkinter.filedialog.askopenfilename()
    except:
        pass

button91 = Button(tk, textvariable=Switch_sel, width=25,command=Start_selectingImage)#button启动的函数不能接受参数，此时使用lambda，先计算函数结果，然后把结果强制重组为一个匿名简单函数
id91 = canvas.create_window(120, 160, window=button91)

Switch_rem=StringVar()
Switch_rem.set('Remove the image')
def Start_removingImage():
    pass
button101 = Button(tk, textvariable=Switch_rem, width=25,command=Start_removingImage)#button启动的函数不能接受参数，此时使用lambda，先计算函数结果，然后把结果强制重组为一个匿名简单函数
id101 = canvas.create_window(325, 160, window=button101)

#插图显示
def resize( w_box, h_box, pil_image): #参数是：要适应的窗口宽、高、Image.open后的图片
  w, h = pil_image.size #获取图像的原始大小
  f1 = 1.0*w_box/w
  f2 = 1.0*h_box/h
  factor = min([f1, f2])
  width = int(w*factor)
  height = int(h*factor)
  return pil_image.resize((width, height), Image.ANTIALIAS)

#用canvas.create_iamge显示图片的话好像会被放到底层去
img_open = Image.open('car.jpg')
img_open=resize(300,300,img_open)
img_jpg = ImageTk.PhotoImage(img_open)
label_img = Label(tk, image = img_jpg)
canvas.create_window(225,290,window=label_img)

label111=Label(tk,width=50,height=13,bg="whitesmoke")
canvas.create_window(225,290,window=label111)

label_img = Label(tk, image = img_jpg)
canvas.create_window(225,290,window=label_img)

#反馈
label121 = LabelFrame(tk,height=150,width=420,text="Log",labelanchor='n',bg="whitesmoke")
id121=canvas.create_window(225,490,window=label121)#坐标是正中

logText=Text(tk,width=55,height=8)
canvas.create_window(225,495,window=logText)

tk.mainloop()
