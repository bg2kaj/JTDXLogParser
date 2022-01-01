# JTDXLogParser
A easy script reading JTDX all.txt and give summary report

如果您是一位WSJT-X或JTDX的重度用户，您一定会好奇如何借用FT8模式进行对自己天馈系统的分析，一方面，通过GridTracker等软件和HamSpot等网站可以对您当前的天馈系统的发射性能进行分析，但在接收方面，天馈系统和环境噪音、传播条件、时间和季节等特征一起作用，很难通过单一的指标进行分析。传统的弱信号分析工具如WSPR等在这方面具有一定的优势，然而在FT8大行其道的今天，为何不直接采用FT8的收听信息进行分析呢？
在WSJT-X以及JTDX软件的运行目录下，随着软件的运行会产生诸如202108_ALL.txt的文件，这一文件是我们在正常运行软件时左面解码窗口的内容的复制，因此通过这一文件，可以分析某一月份的所有收听到的信号的情况，从而对于传播，天馈和信号的来源有一个大概的了解。对于像我一样24x7保持软件开启，一直接收信号的人来说，这样的日志文件可以涵盖大部分时间和常用的波段，对于大型竞赛台来说，在空闲时间内准备几台电脑一直对频率进行分析也是对认识传播情况的一个较好补充。
JLP（JTDX Log Parser）就是为了这个目的而写的一个小脚本，它本身运行于python环境下，但为了更多的爱好者使用，我把她打包成exe可执行文件供有兴趣的朋友使用。当前它可以对任意一个日志文件进行分析，按照每一天、每小时进行分类，并对每一小时内的信号来源（暂时精确到大洲）进行分析。在这个软件的输出中，你可以看到每一小时来自各大洲的信号多少，每一日内每个小时接收到的信号多少，以及每月内每一天所接收到的信号多少，以后随着不断地改进，还会增加更多能够分析的项目以及更多种输出的文件格式。

其中，数据文件（cty.dat）来自于https://www.country-files.com/category/big-cty/ 如有需要请自行更新下载。202108_Part是一个范例文件，取自我自己的日志。

接下来是软件的使用说明，该软件不需安装，第一次下载时请注意软件包内的cty文件日期。如对分析要求不高，可使用软件自带的cty文件。如需要更新，请使用最新下载的cty.dat文件替换掉原有的文件，并执行datparse.exe。

datparse.py
===========
Starting BigCty Database conversion...
Please make sure the BigCty file (cty.dat) is up to date.
Download latest file at https://www.country-files.com/category/big-cty/
This is a part of JTDXLogParser, Make sure run this program first if no cty.json file is present.
Based on cytparser by classabbyamp, 0x5c. Distribute with MIT licence.

Generating cty.json files, Stand by.
cty.json file created. Program now will exit.

当程序如上述输出一样，提示JSON文件建立完成后，可进行下一步操作。

将您电脑中的JTDX日志文件复制至软件目录下，如我的目录为C:\Users\Administrator\AppData\Local\JTDX ，在这个文件夹中有许多以年份和月份命名的文件，如202108_ALL.txt。复制此文件至JLP软件目录中，并打开命令提示行，执行下述指令：
D:\JTDXLogParser>JLP.exe 202108_ALL.txt
执行后，如无其他问题，软件会开始分析并生成报告。当前处理一个100MB的日志文件约需要500+秒，期间软件会在命令行中输出处理过程，结束后，软件会提示并自动退出。此时软件文件夹中会出现一个名为“summary_of_202108_ALL.txt”的文件，此文件即为分析报告。下面即是一个部分日志的报告结果。

JTDX Log Parser Summary File
Result for file:202108_Part.txt
Task starts at :Sat Jan  1 22:42:44 2022.

Day 2021-8-1 Hour 0 detailed report:
AF: 0 AS: 138 EU: 1 NA: 0 SA: 0 OC: 6 
160m: 0 80m: 0 60m: 0 40m: 0 30m: 0 20m: 149 17m: 0 15m: 0 12m: 0 10m: 0 6m: 0 
Day 2021-8-1 Daily detailed report:
[149, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

Day 2021 8 10 Hour 9 detailed report:
AF:0 AS:898 EU:46 NA:25 SA:0 OC:307 
160m: 0 80m: 0 60m: 0 40m: 0 30m: 0 20m: 1300 17m: 0 15m: 0 12m: 0 10m: 0 6m: 0 
Day 2021 8 10 Hour detailed report:
[0, 0, 0, 0, 0, 0, 0, 0, 0, 1300, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

Month 8 Total report:
[149, 0, 0, 0, 0, 0, 0, 0, 0, 1300, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Process took 4 seconds to complete.
In total 1450 lines of record were imported.

在这份报告中，我们可以看到8月1日和8月10日中的两个小时的报告，最下方还有8月份的按日期排序的报告。至于这些数据如何使用，未来还会有怎样的分析结果，将会在以后的软件版本中不断更新。
本软件是开源软件，由于一开始仅为个人使用，并没有过于考虑到很多问题，因此肯定还有很多的缺点、不足和漏洞，由于精力有限，在使用中如果有什么问题请您见谅并自行尝试解决，本人不负责解决使用该软件过程中出现的问题。是否使用请您自行定夺。最后祝愿您在数据通信中获得快乐。
DE BG2KAJ
