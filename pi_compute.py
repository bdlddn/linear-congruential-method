#!/usr/bin/env python
# -*- coding: gb2312 -*-
#
#  pi_function.py
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
import math

def make_random_list(m,a,c,s0):
	"""线性同余法生成伪随机序列"""
	s = []
	s.append(s0)
	#~ s_float = []
	#~ s_long = []
	#~ s_float.append(s[0]/m)
	#~ s_long.append(s[0])
	i = 0
	while i < m:
		 s.append((s[i]*a+c)%m)
		 #~ s_float.append(s[i+1]/m)
		 #~ s_long.append(s[i+1])
		 i += 1
	#~ return s_float
	return s

def make_pair(sx, sy, m):
	"""将两个数组高低拼接起来提高精度"""
	lenth = len(sx)
	s = []
	i = 0 
	while i < lenth:
		s.append(sx[i]*m + sy[i])
		i += 1
	return s
	
	

def compute_pi(sx,sy,m):
	"""计算pi的值"""
	count = 0
	i = 1
	lenth = 2
	while i < m:
		j = 1
		while j < m:
			if math.sqrt(sx[i]*sx[i] + sy[j]*sy[j]) < m * m:
				count += 1
			j += lenth
		i += lenth
	pi = float(4 * count / (m * m) * lenth * lenth)
	return pi
	
if __name__ == "__main__":
	pi_sum = 0.0
	k_list = [3,5,7,11,13,17,19,23,31,37]
	total_times = 1
	m = 65536
	c = 5
	s0 = 1
	i = 0
	#  多次执行求平均，目前只执行了一次
	while i < total_times:
		k1 = k_list[i]
		k2 = k_list[i+1]
		k3 = k_list[i+2]
		k4 = k_list[i+3]
		j = 0
		while j < 1:
			
			sx = make_random_list(m,4*k1+1,c,s0+1)
			sy = make_random_list(m,4*k2+1,c,s0+500)
			sk = make_random_list(m,4*k3+1,c,s0+1000)
			sz = make_random_list(m,4*k4+1,c,s0+2000)
			ssx = make_pair(sx, sy, m)
			ssy = make_pair(sk, sz, m)
			pi = compute_pi(ssx, ssy, m)
			print(pi)
			j += 1
			
		pi_sum += pi
		i += 1
		
	print(pi_sum/total_times)
