# gowin merge bin GUI

这个是一个用于高云FPGA的嵌入式M1软核的用户软件设计程序合并工具，使用前应当将官方的bin添加到环境变量中。

本程序使用pySimpleGUI开发

打包成单文件exe运行： `python -m nuitka --follow-imports --standalone  mb.py --enable-plugin=tk-inter --onefile`