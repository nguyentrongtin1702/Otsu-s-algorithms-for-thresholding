import numpy as np
import math

grayscale_level_1 = 0
grayscale_level_2 = 0
grayscale_level_3 = 0
wb =0
bins = [1,2,3]
size_of_image = 16
intensity_level = [[1,1,1,1],
                   [1,2,2,2],
                   [2,3,3,3],
                   [3,3,3,3]]

for i in range(len(intensity_level)):
    for j in range(len(intensity_level[i])):
        if intensity_level[i][j] == 1:
            grayscale_level_1 = grayscale_level_1+1
        elif intensity_level[i][j] == 2:
            grayscale_level_2 = grayscale_level_2+1
        elif intensity_level[i][j] == 3:
            grayscale_level_3 = grayscale_level_3+1 

sum_of_intensity = [0,grayscale_level_1,grayscale_level_2,grayscale_level_3]
sum = 0
for t in sum_of_intensity:
    sum = sum+t

print(sum)
print("number of value 1",sum_of_intensity[0])
print("number of value 2",sum_of_intensity[1])
print("number of value 3",sum_of_intensity[2])
print("number of value 3",sum_of_intensity[3])


size_of_sum_of_intensity = 3
#caculation foregroud and background

p=[0,0,0,0]

for t in range(3):
    nor = sum_of_intensity[t+1]/size_of_image
    p[t+1]=nor

print("pi",p)

#weight 
wb = [0,0,0]
wf = [1,0,0]
for k in range(size_of_sum_of_intensity-1):
    P1 = p[k+1]+p[k]
    wb[k+1]=P1
    wf[k+1]=1-P1
    
print("weight_back",wb)
print("weigh_fore",wf)

#mean_b
mean_b = [0,0,0]
mean_b_mem = 0
for q in range(size_of_sum_of_intensity-1):
    mean_b_mem = mean_b_mem + ((sum_of_intensity[q+1])/(sum_of_intensity[q+1]+sum_of_intensity[q]))
    mean_b[q+1] = mean_b_mem 

print("meam back",mean_b)

#mean_f
mean_f = [0,0,0]
mean_f_mem = (bins[size_of_sum_of_intensity-1]*sum_of_intensity[size_of_sum_of_intensity])/(sum_of_intensity[size_of_sum_of_intensity])
print(mean_f_mem)
h = range(size_of_sum_of_intensity)
mean_f[2] = mean_f_mem
mean_f[1] = (bins[1]*sum_of_intensity[2]+(bins[2]*sum_of_intensity[3]))/(sum_of_intensity[2]+sum_of_intensity[3])
mean_f[0] = (bins[0]*sum_of_intensity[1]+bins[1]*sum_of_intensity[2]+bins[2]*sum_of_intensity[3])/(size_of_image)
print("mean_fore",mean_f)

#mean global
y = 1
mg= 0
for y in range(4):
    mg = mg + y*p[y-1]

print("mean global",mg)

sigma_b_quare = [0,0,0]
for n in range(size_of_sum_of_intensity):
    #sigma_b_quare[n] = wb[n]*(mean_b[n]-mg)*(mean_b[n]-mg)+wf[n]*(mean_f[n]-mg)*(mean_f[n]-mg)
    sigma_b_quare[n] = wb[n]*wf[n]*math.pow((mean_b[n]-mean_f[n]),2)

print("sigma_b_square",sigma_b_quare)
num = sigma_b_quare[0]
for i in range(size_of_sum_of_intensity):
    if num>sigma_b_quare[i]:
        max = num
    elif num<=sigma_b_quare[i]:
        max = sigma_b_quare[i]
    num = sigma_b_quare[i]

print("Threshold",max)