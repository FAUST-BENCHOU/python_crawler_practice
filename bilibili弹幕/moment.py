import re

# 打开文件用于写入结果
with open('moment.txt', 'w', encoding='utf-8') as output_file:

    with open('danmus.csv', encoding='utf-8') as f:
        danmus = []
        for line in f.readlines()[1:]:
            time = int(float(line.split(',')[0]))
            text = line.split(',')[-1].replace('\n', '')
            danmus.append([time, text])

    danmus.sort(key=lambda x: x[0])
    high_energy_count = 0
    high_energy_times = []

    for item in danmus:
        if re.search('高能', item[1]):
            output_file.write(f'{int(item[0]/60)}m{item[0]%60}s {item[1]}\n')
            high_energy_count += 1
            high_energy_times.append(item[0])
        else:
            pass

    output_file.write(f"高能出现总次数: {high_energy_count}\n")

    # 统计高频出现的时间点
    if high_energy_count > 0:
        high_energy_times.sort()
        high_energy_freq = {}
        for time_point in high_energy_times:
            minute = int(time_point / 60)
            second = time_point % 60
            time_str = f"{minute}m{second}s"
            high_energy_freq[time_str] = high_energy_freq.get(time_str, 0) + 1

        # 找到高频出现的前三个时间点和次数
        top_three = sorted(high_energy_freq.items(), key=lambda x: x[1], reverse=True)[:3]

        # 输出高频出现的前三个时间点和次数到文件
        output_file.write("高频出现的前三个时间点和次数:\n")
        for time_str, freq in top_three:
            output_file.write(f"{time_str}: {freq}次\n")
    else:
        output_file.write("没有找到包含 '高能' 的弹幕。\n")
