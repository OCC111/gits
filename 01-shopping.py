import random 
import time 
list1=[]   #大列表，存储下面小列表的数据
while True:
	print('-'*40)
	print('$'*40)
	print('欢迎来到加尔商超管理系统')
	print('1.添加商品\n2.修改商品\n3.删除商品\n4.退出系统\n5.商超娱乐系统\n6.幸运宝箱')
	print('$'*40)
	print('-'*40)
	list2=[]    #此为小列表，存储下面的内容
	list2=['谢谢参与','谢谢参与','Macbook Air','至高之拳-李青','西部牛仔-亚索','神王-德玛西亚之力','神王-诺克萨斯','勇敢的心-德莱厄斯','神王-德玛西亚之力-三天','神王-诺克萨斯-三天','任性学霸-艾克','制胜金靴-李青','制胜金靴-李青-三天','小红帽,安妮-三天','小红帽,安妮'] 
	sys = int(input('请输入要进行的程序:'))
	if sys == 1:   #添加商品
		time.sleep(2)
		user1 = input('请输入要添加的商品:')  
		price = int(input('请输入商品价格:'))

		list2.append(user1)
		list2.append(price)
		list1.append(list2)
		print(list1)
	elif sys == 2:   #修改商品
		user2 = input('请输入要修改的商品:')
		for n in list1:
			if user2 == n[0]:
				print('1.修改名字\n2.修改商品\n3.修改名字和价格')
				user3 = int(input('请选择功能:'))
				if user3 == 1:
					name = input('please insert shop name:')
					n[0] = name
					print(list1)
				elif user3 == 2:
					name1 = int(input('please insert price:'))
					n[1] = name1
					print(list1)
				elif user3 == 3:
					name = input('please insert shop name:')
					name1 = int(input('please insert price:'))
					n[0] = name
					n[1] = name1
					print(list1)
				break 
	elif sys == 3:   #删除商品
		user4 = input('please insert delete shop name:')
		for position,l in enumerate(list1):   #for循环，，，索引，，，l代表一个列表，enumerate函数名下的list1在l中
			if user4 == l[0]:   #如果user4
				list1.pop(position)   #删除列表索引值
		break 
	elif sys == 4:
		print('即将退出系统') 
		time.sleep(3)
		break
	elif sys == 5:
		def game():   #定义一个函数game
			print('加尔娱乐城')
			print('1.猜拳\n2.猜数字')
			game1 = int(input('输入进程号:'))
			if game1 == 1:
				time.sleep(2)
				print('欢迎来到猜拳大世界!')
				pc=random.randint(1,3)
				i = 1
				for i in range(1,4):  #for循环，让猜拳只进行四次，之后退出系统
					user = int(input('1.石2.刀3.布请输入序号:'))
					if (user == 1 and pc == 2)or(user == 2 and pc == 3)or(user == 3 and pc == 1):
						time.sleep(2)
						print('电脑:%d'% pc)
						print('电脑弱爆了!!!')
					elif user == pc:
						time.sleep(2)
						print('电脑:%d'% pc)
						print('心有灵犀,再来一次吧!')
					else:
						time.sleep(2)
						print('玩家弱爆了!')
				i += 1
				print('这个社会不会给你太多机会的!')
			elif game1 == 2:
				time.sleep(2)
				print('欢迎来到猜数字!!!')
				a = 0
				for a in range(1,101):
					pc2=random.randint(1,100)
					users = int(input('输入一个数字:'))
					if users == pc2:
						time.sleep(2)
						print('Wow,居然被你猜到了!')
						continue
					elif users > pc2:
						print('数大了,再来一次吧!')
						print('哈哈,答案竟是:%d'% pc2)
						continue
					elif users < pc2:
						print('数小了,再来一次吧!')
						
						print('哈哈,答案竟是:%d'% pc2)
						continue
					elif pc2 == 77:
						time.sleep(2)
						return a
				a += 1
		game()

	elif sys == 6:
		print('这里有你想要的道具~')
		user4 = input('是否抽奖?(y/n):')
		if user4 == 'y':			
			print('祝您抽到极品道具!!!')
			time.sleep(3)
			print('即将揭晓答案～')
			pc3=random.sample(list2,1)	
			print('%s'% pc3)
			continue	
		elif user4 == 'n':
			break			
					


				
						
				




	
