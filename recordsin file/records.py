import random
num = 1000
records = [
    "[NEW] tcp      6 120 SYN_SENT src=10.1.2.3 dst={dst1} sport=47800 dport=21 [UNREPLIED] src=203.0.113.47 dst={dst2} sport=21 dport=47800 helper=ftp",
    "[UPDATE] tcp      6 60 SYN_RECV src=10.1.2.3 dst={dst1} sport=47800 dport=21 src=203.0.113.47 dst={dst2} sport=21 dport=47800 helper=ftp",
    "[UPDATE] tcp      6 432000 ESTABLISHED src=10.1.2.3 dst={dst1} sport=47800 dport=21 src=203.0.113.47 dst={dst2} sport=21 dport=47800 [ASSURED] helper=ftp"
]
s_records = []
for _ in range(num):
    random_dst1 = "203.0.113." + str(random.randint(1, 5))
    print(random_dst1)
    random_dst2 = "192.52.100." + str(random.randint(1, 5))
    print(random_dst2)
    for record in records:
        record = record.format(dst1=random_dst1, dst2=random_dst2)
        s_records.append(record)
output_file = "count_recods.txt"
with open(output_file, 'w') as file:
    for record in s_records:
        file.write(record + "\n")

print(f"{num} random records have been generated and saved to {output_file}.")



