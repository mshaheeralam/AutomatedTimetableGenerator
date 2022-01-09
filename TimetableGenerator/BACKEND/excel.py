from django.core.files import File
import xlsxwriter


def data(myfile):
    temp = myfile.readline().split()
    return temp[1]


def excel(worksheet, workbook):
    cell_format = workbook.add_format()
    cell_format.set_align('center')
    cell_format.set_align('vcenter')
    worksheet.set_column('A:F', 20, cell_format)
    worksheet.write(0, 1, 'Monday')
    worksheet.write(0, 2, 'Tuesday')
    worksheet.write(0, 3, 'Wednesday')
    worksheet.write(0, 4, 'Thursday')
    worksheet.write(0, 5, 'Friday')
    worksheet.write(1, 0, '08:00')
    worksheet.write(2, 0, '09:00')
    worksheet.write(3, 0, '10:00')
    worksheet.write(4, 0, '11:00')
    worksheet.write(5, 0, '12:00')
    worksheet.write(6, 0, '13:00')
    worksheet.write(7, 0, '14:00')
    worksheet.write(8, 0, '15:00')
    worksheet.write(9, 0, '16:00')
    worksheet.write(10, 0, '17:00')


def constraint(val, r, c):
    for i in range(r):
        for j in range(c):
            if val[i][j] != 0 and val[i][j][-3:] != 'LAB':
                for k in range(r):
                    if val[k][j] != 0 and val[k][j][-3:] != 'LAB':
                        if val[i][j].split()[0] == val[k][j].split()[0] and k != i:
                            temp = val[k][j]
                            val[k][j] = 0
                            check = True
                            for p in range(c):
                                for q in range(r):
                                    if val[q][p] == temp:
                                        check = False
                                        break
                                if check:
                                    for s in range(r):
                                        if val[s][p] == 0:
                                            val[s][p] = temp
                                            break
                                    break
    for i in range(r):
        for j in range(c):
            if val[i][j] == 0:
                val[i][j] = ""


def core():
    workbook = xlsxwriter.Workbook(r'C:\\Users\\shahe\\OneDrive\\Desktop\\Timetable.xlsx')
    weekdays = {"Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4, "Friday": 5}

    CS29 = workbook.add_worksheet("CS29")
    EEE29 = workbook.add_worksheet("EEE29")
    EEP29 = workbook.add_worksheet("EEP29")
    ME29A = workbook.add_worksheet("ME29-A")
    ME29B = workbook.add_worksheet("ME29-B")
    ES29 = workbook.add_worksheet("ES29")
    excel(EEE29, workbook)
    excel(EEP29, workbook)
    excel(CS29, workbook)
    excel(ES29, workbook)
    excel(ME29B, workbook)
    excel(ME29A, workbook)
    r = 10
    c = 5
    EE29 = [0] * r
    for x in range(r):
        EE29[x] = [0] * c
    EP29 = [0] * r
    for x in range(r):
        EP29[x] = [0] * c
    C29 = [0] * r
    for x in range(r):
        C29[x] = [0] * c
    E29 = [0] * r
    for x in range(r):
        E29[x] = [0] * c
    MA29 = [0] * r
    for x in range(r):
        MA29[x] = [0] * c
    MB29 = [0] * r
    for x in range(r):
        MB29[x] = [0] * c

    with open('c:\\Users\\shahe\\OneDrive\\Desktop\\sol_text.txt', 'r') as f:
        myfile = File(f)
        Lines = myfile.readlines()
        total_lines = 0
        for line in Lines:
            total_lines = total_lines + 1
        myfile.seek(0)
        for i in range(16):
            myfile.readline()
        count = 17
        while count < total_lines:
            for i in range(2):
                myfile.readline()
                count += 1
            temp = myfile.readline().split(" ", 1)
            teacher = temp[1].strip()
            count += 1
            subject = data(myfile)
            count += 1
            temp = myfile.readline().split(" ", 1)
            group = temp[1].strip()
            count += 1
            myfile.readline()
            count += 1
            duration = data(myfile)
            count += 1
            temp = myfile.readline().split(" ", 1)
            count += 1
            classroom = temp[1].strip()
            temp = myfile.readline().split()
            count += 1
            day = temp[1]
            time = temp[2]
            for groups in group.split(", "):
                if groups == "EEE29":
                    day_integer = weekdays[day]
                    time_integer = int(time) - 7
                    for i in range(int(duration)):
                        EE29[time_integer - 1][day_integer - 1] = subject + "  " + classroom
                        time_integer += 1
                elif groups == "EEP29":
                    day_integer = weekdays[day]
                    time_integer = int(time) - 7
                    for i in range(int(duration)):
                        EP29[time_integer - 1][day_integer - 1] = subject + "  " + classroom
                        time_integer += 1
                elif groups == "CS29":
                    day_integer = weekdays[day]
                    time_integer = int(time) - 7
                    for i in range(int(duration)):
                        CS29.write(time_integer, day_integer, subject + "   " + classroom)
                        time_integer += 1
                elif groups == "ES29":
                    day_integer = weekdays[day]
                    time_integer = int(time) - 7
                    for i in range(int(duration)):
                        E29[time_integer - 1][day_integer - 1] = subject + "  " + classroom
                        time_integer += 1
                elif groups == "ME29-A":
                    day_integer = weekdays[day]
                    time_integer = int(time) - 7
                    for i in range(int(duration)):
                        MA29[time_integer - 1][day_integer - 1] = subject + "  " + classroom
                        time_integer += 1
                elif groups == "ME29-B":
                    day_integer = weekdays[day]
                    time_integer = int(time) - 7
                    for i in range(int(duration)):
                        MB29[time_integer - 1][day_integer - 1] = subject + "  " + classroom
                        time_integer += 1

        myfile.closed
        f.closed
    constraint(EE29, r, c)
    constraint(EP29, r, c)
    # constraint(C29,r,c)
    constraint(E29, r, c)
    constraint(MA29, r, c)
    constraint(MB29, r, c)

    for i in range(r):
        for j in range(c):
            EEE29.write(i + 1, j + 1, EE29[i][j])
            EEP29.write(i + 1, j + 1, EP29[i][j])
            # CS29.write(i+1, j+1, C29[i][j])
            ES29.write(i + 1, j + 1, E29[i][j])
            ME29A.write(i + 1, j + 1, MA29[i][j])
            ME29B.write(i + 1, j + 1, MB29[i][j])
    workbook.close()

