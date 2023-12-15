# import matplotlib
# matplotlib.use('TkAgg')
# import matplotlib
# matplotlib.use('Qt5Agg')
# import PyQt5
# import PySide2
# matplotlib.use('Tk') # ValueErrsuor: 'tk' is not a valid value for backend; supported values are ['GTK3Agg', 'GTK3Cairo', 'GTK4Agg', 'GTK4Cairo', 'MacOSX', 'nbAgg', 'QtAgg', 'QtCairo', 'Qt5Agg', 'Qt5Cairo', 'TkAgg', 'TkCairo', 'WebAgg', 'WX', 'WXAgg', 'WXCairo', 'agg', 'cairo', 'pdf', 'pgf', 'ps', 'svg', 'template']
import matplotlib.pyplot as plt
# Q: ImportError: libX11.so.6: cannot open shared object file: No such file or directory
# A: apt install libx11-6 # x11-common?
#    或者直接 apt install python3-tk 上述依赖会带上来

# plt.rcParams['font.sans-serif']=['Microsoft YaHei']
# https://www.fontpalace.com/!pfont-download/simhei/
# plt.rcParams['font.sans-serif']=['SimHei'] # OK
# plt.rcParams['font.sans-serif']=['黑体']
# plt.rcParams['font.sans-serif']=['黑体,SimHei']
# import matplotlib as mpl
# mpl.rcParams['font.sans-serif'] = ['AR PL UKai CN']  # 汉字字体,优先使用楷体，如果找不到楷体，则使用黑体
# mpl.rcParams['font.family'] = 'AR PL UKai CN' # OK
# plt.rcParams['font.sans-serif']=['AR PL UMing CN'] # OK
# plt.rcParams['axes.unicode_minus'] = False

x = [1, 2, 3]
y = [5, -7, 8]
plt.plot(x, y)
plt.xlabel('x - 轴')
plt.ylabel('y - 轴')
plt.title('简单图形')
plt.show()
