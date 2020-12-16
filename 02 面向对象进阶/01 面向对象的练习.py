# -*- coding: utf-8 -*-
# @Time    : 2020/12/11 14:45
# @Author  : sunzhen
# @File    : 01 面向对象的练习.py
# @Software: PyCharm

# 房子(House) 有 户型、总面积 、剩余面积(等于总面积的60%) 和 家具名称列表 属性
# 新房子没有任何的家具
# 将 家具的名称 追加到 家具名称列表 中
# 判断 家具的面积 是否 超过剩余面积，如果超过，提示不能添加这件家具
class House(object):
	# 缺省参数
	def __init__(self, house_type, total_area, free_area, fru_list=None):
		if fru_list is None:  # 如果这个值是None
			fru_list = []  # 将fru_list 设置为None
		
		self.house_type = house_type
		self.total_area = total_area
		self.free_area = total_area * 0.6
		self.fru_list = fru_list
	
	def add_fru(self, x):  # x = bed
		if self.free_area < x.area:
			print('剩余面积不足，放不进去了')
		else:
			self.fru_list.append(x.name)
			self.free_area -= x.area
	
	def __str__(self):
		return '户型={}，总面积={}, 剩余面积={}, 家具名称列表={}'.format(
			self.house_type, self.total_area, self.free_area,self.fru_list
		)


house1 = House('两室一厅', 55, 40)


# 家具(Furniture) 有 名字 和 占地面积属性，其中
# 席梦思(bed) 占地 4 平米
# 衣柜(chest) 占地 2 平米
# 餐桌(table) 占地 1.5 平米
# 将以上三件 家具 添加 到 房子 中
# 打印房子时，要求输出：户型、总面积、剩余面积、家具名称列表

class Furniture(object):
	def __init__(self, name, area):
		self.name = name
		self.area = area


bed = Furniture('席梦思', 4)
chest = Furniture('衣柜', 2)
table = Furniture('餐桌', 1.5)

# 将家具添加到房间里(面向对象关注点:让谁做)
house1.add_fru(bed)
house1.add_fru(chest)
house1.add_fru(table)

print(house1)
