# -*- coding: utf-8 -*-
# 此模块继承自stock.picking，安装之后可以在 库存->作业->所有调拨->创建->额外信息 里面查看到此模块的具体变现形式
from odoo import models,fields,api
import urllib

global null
null = ''

class Kuaidi(models.Model):
	_inherit="stock.picking"

	com_name=fields.Selection([
		('yunda',"韵达"),
		('shunfeng',"顺丰"),
		('shengtong',"申通"),
		('zhongtong',"中通"),
		('yuantong',"圆通"),
		('yousukuaidi',"优速"),
		('huitongkuaidi',"百世快递"),
		('debangwuliu',"德邦物流"),
	],string="快递公司",default=null)
	kuaidi_number=fields.Char(string="快递单号")
	kuaidi_info=fields.Text()
	kuaidi_tree_info=fields.Text(string="最新物流信息")
# 获取物流信息的方法
	def get_info(self):
		if self.com_name and self.kuaidi_number:
			url=str('http://www.kuaidi100.com/query?type='+self.com_name+'&postid='+self.kuaidi_number)
			page=urllib.urlopen(url)
			html=page.read()
			data=eval(html)
			# 状态格式转换
			pre_info=''
			temp = ''
			for pre in data:
				status=data['status']
				state=data['state']
				ischeck=data['ischeck']
				message=data['message']
				com=data['com']
				nu=data['nu']
				condition=data['condition']
				pre_info=str(message)
				temp = pre_info + "。请再次核对您的物流单号，并且刷新浏览器重试！"
			swich_info=data['data']
			#物流信息显示 及格式转换
			info = ''
			tree_info = ''
			for test in swich_info:
				ftime = test['ftime']
				context = test['context']
				print context
				print swich_info
				location = test['location']
				info = info + '时间：' + ftime + '  中转信息：' + context + '  更新站点：' + location + '\n\n'
			#状态判断
			if data['message'] == 'ok':
				tree_info=swich_info[0]['ftime'] + '\n' + swich_info[0]['context']
				self.kuaidi_info=info
				self.kuaidi_tree_info=tree_info
			else:
				self.kuaidi_info=temp
				self.kuaidi_tree_info=temp
		else:
			self.kuaidi_info="此订单没有物流信息！"
			self.kuaidi_tree_info="此订单没有物流信息！"

# 在第一次输入物流信息时自动更新物流信息
	@api.onchange('kuaidi_number')
	def auto_update_kuadidi(self):
		self.get_info()
# 在每次查看订单的时候，手动更新最新的物流信息
	@api.one
	def manual_updata_kuaidi(self):
		self.get_info()













