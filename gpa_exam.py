print("what is your grade for your first SL class")
SL_1=int(input())
print("what is your grade for your second SL class")
SL_2=int(input())
print("what is your grade for your third SL class")
SL_3=int(input())
print('what is your grade for your first HL class')
HL_1=int(input())
print('what is your grade for your second HL class')
HL_2=int(input())
print('what is your grade for your third HL class')
HL_3=int(input())
array_SL=[SL_1, SL_2, SL_3]
array_HL=[HL_1, HL_2, HL_3]
array_letter_SL=[]
for grade in array_SL:
    if array_SL[0] >= 95:
        array_letter_SL.append('A+')
    if 95 > array_SL[0] >= 92.5:
        array_letter_SL.append("A")
    if 92.5> array_SL[0] >= 90:
        array_letter_SL.append("A-")
    if 90> array_SL[0] >= 88.75:
        array_letter_SL.append('B+')
    if 88.75> array_SL[0] >= 85:
        array_letter_SL.append('B')
    if 85 > array_SL[0] >= 81.25:
        array_letter_SL.append('B-')
    if 81.25 > array_SL[0] >= 78.75:
        array_letter_SL.append('C+')
    if 78.75 > array_SL[0] >= 75:
        array_letter_SL.append('C')
    if 75 > array_SL[0] >= 71.25:
        array_letter_SL.append('C-')
    if 71.25 > array_SL[0] >= 68.75:
        array_letter_SL.append('D+')
    if 68.75 > array_SL[0]:
        array_letter_SL.append('D')
    if array_SL[1] >= 95:
        array_letter_SL.append('A+')
    if 95 > array_SL[1] >= 92.5:
        array_letter_SL.append("A")
    if 92.5> array_SL[1] >= 90:
        array_letter_SL.append("A-")
    if 90> array_SL[1] >= 88.75:
        array_letter_SL.append('B+')
    if 88.75> array_SL[1] >= 85:
        array_letter_SL.append('B')
    if 85 > array_SL[1] >= 81.25:
        array_letter_SL.append('B-')
    if 81.25 > array_SL[1] >= 78.75:
        array_letter_SL.append('C+')
    if 78.75 > array_SL[1] >= 75:
        array_letter_SL.append('C')
    if 75 > array_SL[1] >= 71.25:
        array_letter_SL.append('C-')
    if 71.25 > array_SL[1] >= 68.75:
        array_letter_SL.append('D+')
    if 68.75 > array_SL[1]:
        array_letter_SL.append('D')
    if array_SL[2] >= 95:
        array_letter_SL.append('A+')
    if 95 > array_SL[2] >= 92.5:
        array_letter_SL.append("A")
    if 92.5> array_SL[2] >= 90:
        array_letter_SL.append("A-")
    if 90> array_SL[2] >= 88.75:
        array_letter_SL.append('B+')
    if 88.75> array_SL[2] >= 85:
        array_letter_SL.append('B')
    if 85 > array_SL[2] >= 81.25:
        array_letter_SL.append('B-')
    if 81.25 > array_SL[2] >= 78.75:
        array_letter_SL.append('C+')
    if 78.75 > array_SL[2] >= 75:
        array_letter_SL.append('C')
    if 75 > array_SL[2] >= 71.25:
        array_letter_SL.append('C-')
    if 71.25 > array_SL[2] >= 68.75:
        array_letter_SL.append('D+')
    if 68.75 > array_SL[2]:
        array_letter_SL.append('D')
array_letter_HL=[]
for grade in array_HL:
    if array_HL[0] >= 95:
        array_letter_HL.append('A+')
    if 95 > array_HL[0] >= 92.5:
        array_letter_HL.append("A")
    if 92.5> array_HL[0] >= 90:
        array_letter_HL.append("A-")
    if 90> array_HL[0] >= 88.75:
        array_letter_HL.append('B+')
    if 88.75> array_HL[0] >= 85:
        array_letter_HL.append('B')
    if 85 > array_HL[0] >= 81.25:
        array_letter_HL.append('B-')
    if 81.25 > array_HL[0] >= 78.75:
        array_letter_HL.append('C+')
    if 78.75 > array_HL[0] >= 75:
        array_letter_HL.append('C')
    if 75 > array_HL[0] >= 71.25:
        array_letter_HL.append('C-')
    if 71.25 > array_HL[0] >= 68.75:
        array_letter_HL.append('D+')
    if 68.75 > array_HL[0]:
        array_letter_HL.append('D')
    if array_HL[1] >= 95:
        array_letter_HL.append('A+')
    if 95 > array_HL[1] >= 92.5:
        array_letter_HL.append("A")
    if 92.5> array_HL[1] >= 90:
        array_letter_HL.append("A-")
    if 90> array_HL[1] >= 88.75:
        array_letter_HL.append('B+')
    if 88.75> array_HL[1] >= 85:
        array_letter_HL.append('B')
    if 85 > array_HL[1] >= 81.25:
        array_letter_HL.append('B-')
    if 81.25 > array_HL[1] >= 78.75:
        array_letter_HL.append('C+')
    if 78.75 > array_HL[1] >= 75:
        array_letter_HL.append('C')
    if 75 > array_HL[1] >= 71.25:
        array_letter_HL.append('C-')
    if 71.25 > array_HL[0] >= 68.75:
        array_letter_HL.append('D+')
    if 68.75 > array_HL[1]:
        array_letter_HL.append('D')
    if array_HL[2] >= 95:
        array_letter_HL.append('A+')
    if 95 >= array_HL[2] >= 92.5:
        array_letter_HL.append("A")
    if 92.5> array_HL[2] >= 90:
        array_letter_HL.append("A-")
    if 90> array_HL[2] >= 88.75:
        array_letter_HL.append('B+')
    if 88.75> array_HL[2] >= 85:
        array_letter_HL.append('B')
    if 85 > array_HL[2] >= 81.25:
        array_letter_HL.append('B-')
    if 81.25 > array_HL[2] >= 78.75:
        array_letter_HL.append('C+')
    if 78.75 > array_HL[2] >= 75:
        array_letter_HL.append('C')
    if 75 > array_HL[2] >= 71.25:
        array_letter_HL.append('C-')
    if 71.25 > array_HL[2] >= 68.75:
        array_letter_HL.append('D+')
    if 68.75 > array_HL[2]:
        array_letter_HL.append('D')
print('SL letter scores are:')
print(array_letter_SL[0],array_letter_SL[1],array_letter_SL[2])
print('HL letter scores are:')
print(array_letter_HL[0],array_letter_HL[1],array_letter_HL[2])

score_map = {
    'A+': 4,
    'A': 3.7,
    'A-': 3.3,
    'B+': 3,
    'B': 2.7,
    'B-': 2.3,
    'C+': 2,
    'C': 1.7,
    'C-': 1.3,
    'D+': 1,
    'D': 0.7,
}
total = 0
for letter in array_letter_SL:
    total += float(score_map[letter])


total_1 = 0
for letter in array_letter_HL:
    total_1 += float(score_map[letter])


GPA=(((total_1)/3)+((total)/3))/6

GPA_FINAL=round(GPA+0.5,3)
print('GPA equals:')
print(GPA_FINAL)
