# wangzhe
目标：利用合适的手段（如爬虫等）从鹅厂著名手游《王者荣耀》的信息页面中获取相关有用信息，以关系型数据库的形式存储所获取的信息，使用合适的 Web 框架制作一个与你所获取的信息直接有关（或经处理后间接有关）的 Web 应用。
利用合适的手段（如爬虫等）从鹅厂著名手游《王者荣耀》的信息页面中获取相关有用信息，以关系型数据库的形式存储所获取的信息，使用合适的 Web 框架制作一个与你所获取的信息直接有关（或经处理后间接有关）的 Web 应用。

WEB框架与数据库：python+flask+pymysql

2018.11.26
已经实现：通过输入英雄名称，物品或召唤师技能得到数据库中的信息（数据库是直接下载的json，以后会改成爬虫吧），并反馈到页面上
可以得到如下内容
通过英雄名称查询：英雄ID，英雄称号，英雄皮肤名称
通过物品名称查询：物品ID，物品价格（单件价格/总价格），物品属性（基本属性/特殊属性）
通过召唤师技能名称查询：解锁等级，简介

PS.界面难看得不忍直视qwq
