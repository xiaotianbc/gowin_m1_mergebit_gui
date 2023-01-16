import winsound
import PySimpleGUI as sg
import os.path
# encoding=utf-8
import os
import fnmatch
import shutil
import pyperclip
import configparser  # 报错参数

sg.theme('SystemDefault')

current_path = os.getcwd()  # 获取当前工作目录路径

# 可执行程序的位置，默认从环境变量里读取，比较灵活
main_makeloc = r'make_loc.exe'  # makeloc exe文件
main_merge_bit = r'merge_bit.exe'  # merge_bit exe文件

# button image

toggle_btn_off = b'iVBORw0KGgoAAAANSUhEUgAAAGQAAAAoCAYAAAAIeF9DAAAPpElEQVRoge1b63MUVRY//Zo3eQHyMBEU5LVYpbxdKosQIbAqoFBraclatZ922Q9bW5b/gvpBa10+6K6WftFyxSpfaAmCEUIEFRTRAkQFFQkkJJghmcm8uqd763e6b+dOZyYJktoiskeb9OP2ne7zu+d3Hve2smvXLhqpKIpCmqaRruu1hmGsCoVCdxiGMc8wjNmapiUURalGm2tQeh3HSTuO802xWDxhmmaraZotpmkmC4UCWZZFxWKRHMcZVjMjAkQAEQqFmiORyJ+j0ei6UCgUNgyDz6uqym3Edi0KlC0227YBQN40zV2FQuHZbDa7O5fLOQBnOGCGBQTKNgzj9lgs9s9EIrE4EomQAOJaVf5IBYoHAKZpHs7lcn9rbm7+OAjGCy+8UHKsD9W3ruuRSCTyVCKR+Es8HlfC4bAPRF9fHx0/fpx+/PFH6unp4WOYJkbHtWApwhowYHVdp6qqKqqrq6Pp06fTvHnzqLq6mnWAa5qmLTYM48DevXuf7e/vf+Suu+7KVep3kIWsXbuW/7a0tDREo9Ed1dXVt8bjcbYK/MB3331HbW1t1N7eTgAIFoMfxSZTF3lU92sUMcplisJgxJbL5Sifz1N9fT01NjbSzTffXAKiaZpH+/v7169Zs+Yszr344oslFFbWQlpaWubGYrH3a2pqGmKxGCv74sWL9Pbbb1NnZyclEgmaNGmST13kUVsJ0h4wOB8EaixLkHIEKKAmAQx8BRhj+/btNHnyZNqwYQNNnDiR398wjFsTicSBDz74oPnOO+/8Gro1TbOyhWiaVh+Pxz+ura3FXwbj8OHDtHv3bgI448aNYyCg5Ouvv55mzJjBf2traykajXIf2WyWaQxWdOrUKTp//rww3V+N75GtRBaA4lkCA5NKpSiTydDq1atpyZIlfkvLstr7+/tvTyaT+MuAUhAQVVUjsVgMYABFVvzOnTvp888/Z34EIDgHjly6dCmfc3vBk4leFPd/jBwo3nHo559/pgMfHaATX59ApFZCb2NJKkVH5cARwAAUKBwDdOHChbRu3Tq/DegrnU4DlBxAwz3aQw895KpRUaCsp6urq9fDQUHxsIojR47QhAkTCNYCAO677z5acNttFI3FyCGHilaRUqk0myi2/nSaRwRMV9c1UhWFYrEozZo9mx3eyW9OMscGqexq3IJS7hlJOk+S3xTnvLyNB+L333/P4MycOVMYwGRN02pt234PwHFAJCxE1/Vl48aNO1hXV6fAEj777DPCteuuu44d9w033EDr16/3aQlKv3TpEv8tHS6exXiCvmpqaigWj5NCDqXT/bT9tdfoYnc39yWs5WqXcr6j0rHwK/I+KAy66u7upubmZlq8eLG47mQymeU9PT0fg95UD00lFAptSyQSHNrCgcM6xo8fz2DceOONtHnTJt4v2kXq7LxAHR0d7CvYccujRlNIwchX3WO06ejopM6ODrKsIgP0xy1bGGhhSRgZV7sELaNcRBnclzcwDt4dLAPdAhih+3A4/A8wEKyIAdE0bU0kEuGkDyaGaAo3YwMod999NyvZtCx20JlMf8lDkaK6ICgq8X/sRrxj1QUMwJw/D1BMvu8P99/PYTPCRAHI1Uxf5aLESvQ1FChQPPQKHQvRNG1pNBpdDf2rHl2hHMI3nD592g9tcdy8ppl03eCR3N3VxT5D5n9331U6/2XLUEv2Fe9vsWjRha5uKloWhUMGbdiwnjkVPkVEGWPNUoLnKJB/BdvACqBb6Bg5nbhmGMZWpnBVVWpDodDvw+EQO+H9+/fzDbhx9uzZTC2OU6Te3l5Wms/3AV9R8tCOe9FRSps4pJBdtCh56RKHyfX1DTRnzhx2dgAf/mQ0Iy9ky0jMFi1aVHL+k08+YWWAs4WibrnlFlq+fPmQ/bW2ttJPP/1EW7ZsGbLdiRMn2P/KdT74EfFbYAboGAn2rFlu4qjrGjCoVVVVawqFQiHDCHG0hNwBSKGjhYsWckf5XJ5yHBkJK3AtwPcVgq48y1A0lVRN8Y5Vv72GB1I1DgXzuRw5tsPZLHwJnJ5cdrnSbdq0afTAAw8MAgOybNkyVuqUKVN8yxxJJRa0i204wful0+lBVEwD1sA6hq77+lI8eBVFBQZNqqZpvxMZ97Fjxxg9HONhq6uq2IlnsjkXaU/xLlVppLHCNRck35m759FO0zyHrwpwNB8kvJjt2DS+bjxn/fAloMWRKGY4gWXI8X4luffee5kJ8LsjEQyakVArgEBbYRWyyNQFXUPnQoCFrmnafFwEICgUohEU1tDQQLbtlQXsImmqihyPFMWjI4bbIdUBFam8r5CbCJLi0pU79AjunRzVvU/1ruPFsOHhkO0fOnRoIFu9QtpasGCBv//DDz/Qu+++S2fOnOF3RMSIeh1yIggS3D179pQMhMcee4yTWVEWEgI9wfKEwDHv27dvUPUBx3DecjgvrguQ0Aa6xvMJqgQWuqqqMwXP4SHA4xCMWlGbwYh3exXde0onDwQSICnAhc+riuIn74yh15oR5HMqjyIEDPUN9cynIgS+0rxEKBuOc9u2bczXSG5h+QgiXn31VXrwwQc5t4KffOutt0pCb7QTpaCgUhEJyccoJUH5QfBEqUi0C1q+qBIjg5f6m6Fjlk84H/AekjgcV1VXk+Ol/6Cjih5ciOfkub2iuqA4A5Yi4GMsaaCtYxdpwvgJPh1cKWWBrjCSIaADhJg4J49YKB/hOwCBgnFdBuTRRx8d1O/JkyfZksSAhSBRxiYLAoXnn3/eD1AqvY+okCeTSd96VFWtASBVgtegFNFJyNDdhwTlqKXoO/6oH8BpiKDLvY5+yjSwHcdNOD0KG80kEX5KTBHIIxj7YAMhSNaG+12E5hiwsJyhBP0gIsXAFgOjkgidCwEWuhzNyOk+/Af8BUdRnqpLaojSUen5YSTQGC8gttFw6HIfsI5KRUxQspCuri6aOnXqkP1isCB6Gu4ZOSq9zLxKfj7dcZw+x3Gq0BG4U/wgRhfMXCR//s3Sv25hl52GDw1T0zAIKS5zMSUWbZsLkqMlGJ1QCCwD1dUDBw6UHf1w7hBEdwBEVsrjjz8+yKmDXuCL5HZw6shNhFMXDhu+J+hTyonQuRBgoXsrJqpwDlVesUIC3BaJRlh7hqaxB/B8OXk+2hvtiqi4+2gzpqoHkIi6PJ5TvAQRlFfwKOpCV9eoluORaM6dO5dp4+GHH+aKNWpvUBIsA5EVSkLkRWHBAieOca/s1EVkFHTyACno1L11CEM+o5hhRFAgRWCXdNu2TxWLxQaghYdEZIJ9/J00eTKRbZIaCZPDilcGrMJz0H6465kEY6EKvDwa5PkRhfy4S3HbF7MWJ4ciJA2+8C8RvBzmbwAIBGGqHKoGZceOHX6oLysa5wTlyRIsi4iioezsg/Mj5WhORLCYUZTuO606jnNMOFPkAzB37KNE4BRdSsEmlKX5SR6SQdU77yaFqtfGTQA1r6blZvAaZ/AaX1M4D7FdJ+7Y9O2335aMUnlJzS/ZEOm8+eabw8KJFR9ggmB4e7kSLL3L7yCfl6/h3aHrm266yffhtm0fV23b3i8mR+bPn8+NgBx4NZnsYZ7PZtxMHQBwJq55ZRKpNKJ5inYVrvrZO498v42bteNcNpsjx7G5DI0QFCNytOZG8Bznzp2j5557jvbu3TvoOsrfTzzxBE8vI+TFCB8pXVZSMlUAo9IcPJeP8nmuoQmxbbsVlNViWVbBsqwQHg4ZOhwjlHPkiy9oxR13kJ3P880iKWKK4mxcJHkeiSkDeYbrLRQ/ifTDAcWhXD5Hhby7EqZ1XyuHh6JaUO4lfomgLzwz1gOgYArnLSIfXMO7iOQPx0ePHuUAALOeGBTwIeWeBZNyTz75pF9shd8dDozgOYS6CJqga+l3gEELoiwsd3wvn89vxMOtXLmSXn75ZR6xKKXM6ezkim9vX68/Hy78uVISbXl+Y8C1uDgEEhVMUvVe6iWbHDrXfo6OHT/GeYBY8zVagJBUwkDfcp1M8dZLydVlgCCmIMjL1is9B/oT+YjwfZXAKAeMyGk2btzotykWi8Agyfxgmua/gBiQmzVrFq8iwTFuRljHcTXTWDfPaah+kVHMhahSAdGt6mr+vIjq+ReVR1R3dxf3hQryG2+84U+EyRYyWiJCdvSN3wA4YoKIZ+ekyE6uwoqp5XI0JqItWJhYxXk5YIhKMPIelG1owGqegc4ZENu2d+fz+cNi9m7Tpk0MiEASnGuaFs/2dXRcoGwmw5EUNkVUc0maPfRnEL3pTkXhEjumcTHraBaLXE/CbyBslOP2K3Xo/4tNVra8lQNA3jDgUUuDLjZv3iw780PZbHYP9K0hTvc6OKYoyp9CoZDCixJiMfrqq694FKATOF6Ej7AAHMMpozDII01xfUq5OQwoHY4bnIsySSFf4AVkyAvgs8DBQ43Iq0VGa5EDEk5MiUvW4eTz+ft7e3vP4roMSLvjOBN1XV8CM4TyoUxM6YIzAQJm2VA1TcQTbDHpVIp9S8Es8LFYHIb7+nr7qKu7i3r7+tgqIOfOtdMrr/yHHaMMxtW6eC44+iu1Ce4PBQYWyzU1NfnXsTo+lUr9G8EE1xI//PBDv0NVVaPxePwgFsqJFYrvvPMOT3lCeeBcOEdUSRcvXkS1NdJCOZIrjAOFeeyjxNzW9hFXTGF5oClBVWNlGRCNwkI5VAjuuecevw0WyqVSqd8mk8ks2vCMqQwIuWUDfykplAaFARAAA/qCtXhL7KmurpamT5tOU6ZiKalbagAUuWyOkj1JOtt+1l80IRxr0ImPFTCCUinPKLeUFMoGTWHqWAiWknqrFnkpqZi1HATIqlWrMFk0Nx6P82Jrsb4XieLrr7/O88CinO0MfP8wqGKrDHzk409Xim2sLiWly1hsDdoW0RSCJFFdRlvLss729/c3NzY2fo3gRi7Bl139joZtbW3LHcfZYds2f46AXGTr1q1MO8h+kaNAsZVWi/gZvLeUUvGmbRFJ4IHHsgR9RPBzBGzwwcgzsKpGBq9QKOBzhI0rVqw4Q16RUZaKH+w0Njae3b9//+22bT9lWZb/wQ6iA/wIoqYvv/ySK6siivLXp5aJtsYqNVUSAYao7MLHYmEIyvooQckTWZ4F4ZO2Z9Pp9CNNTU05+ZosZSkrKAcPHsQnbU/H4/ElYgX8/z9pG14kSj+UyWT+vnLlyoNBAF566aWS4xEBIuTTTz/Fcse/RqPRteFwOCy+ExHglFtuea2IHCJ7/qRgmubOfD7/jPfRpz+TOFQYPQiQoUQ4asMw8Fk0FtitCIVCv9F1nT+LVlW16hoFJOU4Tsq2bXwWfdyyrNZCodBSKBSScNgjXsBBRP8FGptkKVwR+ZoAAAAASUVORK5CYII='
toggle_btn_on = b'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'


# 给删除文件创建一个函数，保证这个操作是安全的
def safe_delete_file(file_path):
    if os.path.exists(file_path):
        # python踩坑之一，如果使用os.remove删除只读文件，会删不掉。。。先运行一下这个就好
        # -r : -代表去除 +代表加上 r代表只读属性
        os.system(f"attrib -r {file_path}")
        os.remove(file_path)  # 如果程序调用此函数不止一次，需要先删除，否则会报错


# 找到高云项目目录下对应后缀的文件
def gowin_find_file_by_suffix(project_dir, file_suffix):
    gowin_file_dir_path = os.path.join(project_dir, 'impl', 'pnr')
    if not os.path.exists(gowin_file_dir_path):
        return -1
    filted_list = fnmatch.filter(os.listdir(gowin_file_dir_path), f'*.{file_suffix}')
    if len(filted_list) == 0:
        return -1
    return os.path.join(gowin_file_dir_path, filted_list[0])  # 返回找到的第一个文件


# 调用make_loc生成 itcm.loc文件
def func_make_loc(posp_file, itcm_size, isDebugEnable):
    if (not isinstance(posp_file, str)) or (len(posp_file) == 0):  # 对传入的参数做一个检查，需要是字符串并且长度大于0
        return -1

    arg_str = main_makeloc + ' -i ' + posp_file + ' -s ' + itcm_size + ' -d –t gowin_syn'
    print(arg_str)
    # 如果要传入多个参数，就继续定义，然后在os.system里加起来就行
    r_v = os.system(arg_str)
    return r_v


def func_merge_bit(bin_file, itcm_loc, fs_file):
    if not os.path.exists(itcm_loc):
        sg.popup('请生成ITCM 布局位置信息 itcm.loc 文件！！！')
        return -1
    if not (os.path.exists(fs_file) and os.path.exists(bin_file)):
        return -1
    temp_fs_path = os.path.join(current_path, 'temp.fs')
    safe_delete_file(temp_fs_path)
    shutil.copy(fs_file, temp_fs_path)  # 先把fs文件复制到当前目录，这个是高云工具缺陷的workaround

    arg_str = main_merge_bit + ' ' + bin_file + ' ' + itcm_loc + ' temp.fs'
    print(arg_str)
    # 如果要传入多个参数，就继续定义，然后在os.system里加起来就行
    r_v = os.system(arg_str)
    safe_delete_file(temp_fs_path)
    return r_v


def gowin_exflash_program(fs_file_path):
    arg_s = 'programmer_cli.exe --device  GW2A-18C --cable-index 1 --spiaddr 0x000000 --run 36 --fsFile ' + fs_file_path
    print(arg_s)
    r_v = os.system(arg_s)
    return r_v


make_itcm_loc_column = [
    [
        sg.Text("确认 make_loc 和merge_bit 已经加入环境变量"),
        sg.Button(button_text='load', button_color=('black', 'white'), size=(5, 1), key='-BLOAD-'),
    ],
    [sg.Text("选择硬件设计项目 gprj 所在文件夹")],
    [sg.Text("MUST!! Project -> Place&Route -> Generate Post-Place File: True")],
    [
        sg.In(size=(40, 1), enable_events=True, key="-FPROJECTDIR-"),
        sg.FolderBrowse()
    ],
    [
        sg.Text("ITCM-Size"),
        sg.In(size=(5, 1), enable_events=True, key="-SITCMSIZE-", default_text="32"),
        sg.Text("Enable-Debug"),
        sg.Button('', image_data=toggle_btn_on, key='-TOGGLE-GRAPHIC-',
                  button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0)
    ],
    [
        sg.Text("itcm.loc文件"),
        sg.In(size=(20, 1), enable_events=True, key="-FITCMLOC-"),
        sg.FileBrowse(file_types=(("fs-file", "*.fs"),)),
    ],
    [
        sg.Text("硬件设计码流文件"),
        sg.In(size=(20, 1), enable_events=True, key="-FFSFILE-"),
        sg.FileBrowse(file_types=(("fs-file", "*.fs"),)),
    ]
]

merge_bit_column = [
    [
        sg.Text("软件设计二进制 BIN 文件"),
        sg.In(size=(20, 1), enable_events=True, key="-FBINFILE-"),
        sg.FileBrowse(file_types=(("BIN FILE", "*.bin"),)),
    ],
    [
        sg.Text("如果没有itcm.loc文件，需要先生成", key='-TextMERGEBITL-'),
        sg.Button(button_text='merge_bit', button_color=('black', 'white'), size=(12, 2), key='-BMERGEBIT-'),
    ],
    [sg.InputText('', key='-OUTPROG-'),
     sg.Button(button_text='copy', button_color=('black', 'white'), size=(5, 1), key='-BCOPY-'),
     ]
]

# ----- Full layout -----
layout = [
    [sg.Column(make_itcm_loc_column)],
    [sg.HorizontalSeparator()],
    [sg.Column(merge_bit_column)]
]

window = sg.Window("Gowin Merge bit Tool", layout)

# 用一个字符串来保存当前硬件设计项目的位置
s_proj_dir = ""


def when_hard_change():
    fs_file_path = gowin_find_file_by_suffix(s_proj_dir, 'fs')
    window['-FFSFILE-'].update(fs_file_path)

    posp_file_path = gowin_find_file_by_suffix(s_proj_dir, 'posp')
    make_loc_result = func_make_loc(posp_file_path, values["-SITCMSIZE-"], True)
    if make_loc_result != 0:
        sg.popup('make_loc failed!')
    if not os.path.exists(current_path + '/itcm.loc'):
        sg.popup('make_loc failed!')
    window['-FITCMLOC-'].update(current_path + '/itcm.loc')


down = graphic_off = False
# Run the Event Loop
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    elif event == '-TOGGLE-GRAPHIC-':  # if the graphical button that changes images
        graphic_off = not graphic_off
        window['-TOGGLE-GRAPHIC-'].update(image_data=toggle_btn_off if graphic_off else toggle_btn_on)
    elif event == '-BMERGEBIT-':  # 如果是点击了MERGEBIT的按键
        window['-TextMERGEBITL-'].update('make new_temp.fs in progress ...', text_color='black')
        merge_bit_result = func_merge_bit(values["-FBINFILE-"], current_path + '/itcm.loc', values["-FFSFILE-"])
        if merge_bit_result == 0:
            window['-TextMERGEBITL-'].update('make new_temp.fs OK，program to flash->0x0', text_color='green')
            str_fs_path = os.path.join(os.getcwd(), 'new_temp.fs')
            prog_cli_text = fr'programmer_cli.exe --device  GW2A-18C --cable-index 1 --run 36 --spiaddr 0x000000 --fsFile "{str_fs_path}"'
            window['-OUTPROG-'].update(prog_cli_text)
            config = configparser.ConfigParser()  # 创建一个配置文件管理句柄
            config.read("gowin_mb_conf.ini", encoding="utf-8")
            if not config.has_section("def"):  # 检查是否存在section
                config.add_section("def")
            config.set("def", "hard", values["-FPROJECTDIR-"])  # 修改db_port的值为69
            config.set("def", "soft", values["-FBINFILE-"])  # 修改db_port的值为69
            config.write(open("gowin_mb_conf.ini", "w"))
        else:
            window['-TextMERGEBITL-'].update('执行失败！！！请检查输入是否正确', text_color='red')

    elif event == '-FPROJECTDIR-':
        s_proj_dir = values["-FPROJECTDIR-"]
        when_hard_change()

    elif event == '-BCOPY-':
        pyperclip.copy(values['-OUTPROG-'])  # 把文字复制到剪切板


    elif event == '-BLOAD-':
        config = configparser.ConfigParser()  # 创建一个配置文件管理句柄
        config.read("gowin_mb_conf.ini", encoding="utf-8")
        if config.has_section("def") \
                and config.has_option("def", "hard") \
                and config.has_option("def", "soft"):  # 检查是否存在section
            r = config.get("def", "hard")
            s_proj_dir = r
            window["-FPROJECTDIR-"].update(r)
            r = config.get("def", "soft")
            window["-FBINFILE-"].update(r)
            when_hard_change()

window.close()
