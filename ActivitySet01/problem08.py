[2:48 pm, 16/05/2022] Veg Muzan: text= "X-DSPAM-Confidence:    0.8475"
a=text.find("0")
text=text[a:]
print(float(text))
[2:48 pm, 16/05/2022] Veg Muzan: fname = input("Enter file name: ")
fh = open(fname)
count=0
total=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count=count+1
    l=line.find("0")
    number=float(line[l:])
    total=total+number
avg=total/count
print("Average spam confidence:",avg)