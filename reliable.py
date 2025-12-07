import numpy as np
import pandas as pd

mean = 4
std = 1
size = (1000, 1000)
samples = np.random.normal(mean, std, size)

results = []
count = 0
for sample in samples:
    sample_mean = sum(sample)/len(sample)
    sample_mean = float(sample_mean)
    sample_std = (sum([(x - sample_mean)**2 for x in sample])/(len(sample)-1))**(1/2)
    sample_std = float(sample_std)
    lowlimit = sample_mean - 1.96 * sample_std / (len(sample))**(1/2)
    highlimit = sample_mean + 1.96 * sample_std / (len(sample))**(1/2)
    if mean > lowlimit and mean < highlimit:
        reliable = True
        count+=1
    else:
        reliable = False
    
    results.append([len(sample), round(sample_mean,3), round(sample_std,3), round(lowlimit,3), round(highlimit,3), reliable])

print("모의 실험 | 표본의 크기 | 점추정값 | 표본표준편차 | 하한   | 상한   | 포함 여부")
for x in range(len(results)):
    result = results[x]
    print(f"실험 {x+1:<4} | {result[0]:<11} | {result[1]:<8.4} | {result[2]:<12.4} | {result[3]:<6.4} | {result[4]:<6.4} | {result[5]}")
print(f"count : {count}")