#!/usr/bin/env python
# -*- coding: gb2312 -*-
#
#  zhengtai.py
#  
#  Copyright 2017 Administrator <Administrator@WIN-84KOMAOFRMQ>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import matplotlib.pyplot as plt

def make_random_list(m,a,c,s0):
	"""线性同余法生成伪随机序列"""
	s = []
	s.append(s0)
	s_float = []
	s_float.append(s[0]/m)
	i = 0
	while i < m:
		 s.append((s[i]*a+c)%m)
		 s_float.append(s[i+1]/m)
		 i += 1
	return s_float
	
def print_list(sx):
	"""将排好序的数列进行绘制"""
	lenth = len(sx)
	min_value = sx[0]
	max_value = sx[lenth - 1]
	value_range = max_value - min_value
	
	n = 50
	
	jump_range = value_range / n
	
	result_list = []
	
	i = 0
	
	while i < n + 1:
		result_list.append(0)
		i += 1
	
	for s in sx:
		i = int((s - min_value)/jump_range)
		result_list[i] += 1
	print(result_list)
	plt.plot(result_list)
	plt.show()
		

if __name__ == "__main__":
	i = 0
	s_total = []
	k = 2
	s0 = 1
	c = 5
	m = 65536
	while i < 12:
		k = k + 1
		s = make_random_list(m,4*k+1,c,s0+i)
		s_total.append(s)
		i += 1
	sx = []
	i = 0
	while i < m:
		j = 0
		total = 0
		while j < 12:
			total = total + s_total[j][i]
			j += 1
		z = total - 6
		sx.append(2+3*z)
		i += 1
	
	sx.sort()
	print_list(sx)
		
	
