# Restaurant-system
餐厅点餐系统：

该系统必须允许客户：
• 选择他们的桌号。
• 浏览菜单。
• 将菜单中的物品添加到他们的订单中。
• 请求服务员的帮助。
• 餐食完成后请求账单。然后，客户可以前往前台付款。

该系统必须允许厨房员工：
• 查看已接收的客户订单的按时间排序的列表
• 一旦准备好供应，就标记订单项为已准备

该系统必须允许服务员：
• 当客户请求帮助时接收通知，该通知应包括请求帮助的桌号信息
• 处理完请求后，将请求帮助标记为已完成
• 当订单项准备完毕且准备上菜时，接收通知，该通知应包括已准备订单项的信息以及应将其送达的桌号
• 一旦已将订单项送达客户，就将订单项标记为已完成

该系统还必须允许经理：
• 在菜单中添加新的类别
• 添加带有标题、描述、配料、类别和成本的新菜单项到菜单中
• 从菜单中移除现有的菜单项
• 更新菜单的描述、配料、类别或成本
• 更新在类别内显示菜单项的顺序
• 更新菜单上显示的菜单类别的顺序

## 1. Backend Configuration

(a)Install some required Python libraries:  
`pip install django==3.2`  

`pip install djangorestframework==3.12.0`  

`pip install django-cors-headers`  

`pip install drf-yasg2`  

`pip install drf-writable-nested`  

`pip install django-filter` (installing this step would update django version to 4.0, we need to install django==3.2 again and ignore error)  

so do the following
`pip install django==3.2`  

(b)Update the model:  
`cd backend`

`python manage.py makemigrations` or
`python3 manage.py makemigrations`

(c)Migrate settings:  
`python manage.py migrate` or
`python3 manage.py migrate`

(d)Create superuser
`python manage.py createsuperuser` or
`python3 manage.py createsuperuser`

Then just follow the instruction provided by the command line to create a user.

(e)Run server:  
`python manage.py runserver` or
`python3 manage.py runserver`

read backend doc in Swagger: http://127.0.0.1:8000/doc/

## 2.Fontend Configuration

(a) cd frontend folder:  
`cd frontend`
    
(b) Install npm package:  
`npm install`

(d) Add other libraries (updating):  
`npm install react-router-dom`  

`npm install antd` (2023.06.26)  

(d) Start frontend:  
`npm start`

