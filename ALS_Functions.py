import pymysql
from datetime import datetime, timedelta
from tkinter import *
from tkinter import messagebox
from tkmacosx import *

# Connecting to Database
mypass = "" # Change Password Here
mydatabase="LibraryManager"
con = pymysql.connect( host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

# Some stored members
current_membership_ID = None

# Functions
def movetosomewhere(togo, toremove):
    def function():
        toremove.forget()
        togo.pack()
    return function

def movetosomewhereandstore(togo, toremove, tostore):
    def function():
        global current_membership_ID
        current_membership_ID = tostore.get()
        findId = "select * from Member where id = '"+current_membership_ID+"'"
        findMember = cur.execute(findId)
        if findMember == 0:
            messagebox.showinfo("Error"," Member do not exist")
        else:
            movetosomewhere(togo, toremove)()
    
    return function

def makeMember(*inputs):
    def innerFunc():
        information = []
        for i in inputs:
            information.append(i.get())
            
        insertMember = "insert into"+ " Member values " + f'("{information[0]}", "{information[1]}", "{information[2]}", "{information[3]}", "{information[4]}")'
        try:
            cur.execute(insertMember)
            con.commit()
            messagebox.showinfo('Success',"Success! \n ALS Membership created")
        except:
            messagebox.showinfo("Error","Error! \n \n Member already exist; Missing or Incomplete fields.")
        
    return innerFunc

def deleteMember(returnto, *inputs):
    def innerFunc():
        membershipID = inputs[0].get()
        deleteSql = "delete from Member where id = '"+membershipID+"'"
        findId = "select * from Member where id = '"+membershipID+"'"
        memberInfo = []
        present = True
        try:
            cur.execute(findId)
            con.commit()
            for i in cur:
                memberInfo.append(i[0])
                memberInfo.append(i[1])
                memberInfo.append(i[2])
                memberInfo.append(i[3])
                memberInfo.append(i[4])
            name = memberInfo[1]
            faculty = memberInfo[2]
            phoneNumber = memberInfo[3]
            email = memberInfo[4]
            titleMessage = "Please Confirm Details to Be Correct \n \n"
            member = "Member ID: " + membershipID + " \n"
            name = "Name: " + name + " \n"
            faculty = "Faculty: " + faculty + " \n"
            phoneNumber = "Phone Number: " + phoneNumber + " \n"
            email = "Email: " + email + " \n"
            fullMessage = titleMessage + member + name + faculty + phoneNumber + email
            
            print(name)
            print(faculty)
            print(phoneNumber)
            print(email)
        except:
            messagebox.showinfo("Error","Member ID not present")
            present = False
        
        try:
            confirmation = messagebox.askyesno(message = fullMessage)
            if confirmation:
                cur.execute(deleteSql)
                con.commit()
                messagebox.showinfo(title = "Succes", message = "Success! \n ALS Membership Deleted")
        except:
            if present == True:
                messagebox.showinfo("Error", "Member has oustanding loans, reservations and fines")
            returnto.forget()
            returnto.pack()
    return innerFunc

def updateMember(returnto, *inputs):
    def innerFunc():
        information = [current_membership_ID]
        for i in inputs:
            information.append(i.get())
        indicator = True
        findId = "select * from Member where id = '"+current_membership_ID+"'"
        findMember = cur.execute(findId)
        if findMember == 0:
            indicator = False
            messagebox.showinfo("Error"," Member do not exist")
        updateMember = "update Member set " + f'name="{information[1]}", faculty="{information[2]}", phoneNum="{information[3]}", email="{information[4]}" where id="{information[0]}"'
        name = information[1]
        faculty = information[2]
        phoneNumber = information[3]
        email = information[4]
        titleMessage = "Please Confirm Details to Be Correct \n \n"
        member = "Member ID: " + current_membership_ID + " \n"
        name = "Name: " + name + " \n"
        faculty = "Faculty: " + faculty + " \n"
        phoneNumber = "Phone Number: " + phoneNumber + " \n"
        email = "Email: " + email + " \n"
        fullMessage = titleMessage + member + name + faculty + phoneNumber + email
        if indicator:
            try:
                confirmation = messagebox.askyesno(message = fullMessage)
                if confirmation:
                    cur.execute(updateMember)
                    con.commit()
                    messagebox.showinfo(title = "Succes", message = "Success! \n ALS Membership updated")
            except:
                messagebox.showinfo("Error"," Missing or Incomplete fields.")
                returnto.forget()
                returnto.pack()
    return innerFunc

def addBook(*inputs):
    def innerFunc():
        information=[]
        for i in inputs:
            information.append(i.get())
        insertBook = "insert into"+ " Book values " + f'("{information[0]}", "{information[1]}", "{information[2]}", "{information[3]}", "{information[4]}", {information[5]})'
        try:
            cur.execute(insertBook)
            con.commit()
            messagebox.showinfo('Success',"Success! New Book added in Library")
        except:
            messagebox.showinfo("Error","Book already added; Duplicate, Missing or Incomplete fields.")
        print(information)
    return innerFunc

def withdrawBook(returnto, *inputs):
    def innerFunc():
        accession_number = inputs[0].get()
        findBook = "select * from Book where accessionNo = '"+accession_number+"'"
        deleteBook = "delete from Book where accessionNo = '"+accession_number+"'"
        findReservation = "select accessionNo, COUNT(*) as Total FROM Reservation where accessionNo = '"+accession_number+"'"
        findLoan = "select accessionNo, COUNT(*) as Total FROM Loan where accessionNo = '"+accession_number+"'"
        bookInfo = []
        present = True
        Indicator = False
        cur.execute(findReservation)
        existingReservation = cur.fetchall()[0][1]
        if existingReservation:
            messagebox.showwarning(title=" Error", message = "Error! \nBook is currently Reserved.")
            Indicator = True

        cur.execute(findLoan)
        existingLoan = cur.fetchall()[0][1]
        if existingLoan:
            messagebox.showwarning(title=" Error", message = "Error! \nBook is currently on Loan")
            Indicator = True
            
        try:
            cur.execute(findBook)
            con.commit()
            for i in cur:
                bookInfo.append(i[0])
                bookInfo.append(i[1])
                bookInfo.append(i[2])
                bookInfo.append(i[3])
                bookInfo.append(i[4])
                bookInfo.append(i[5])
            name = bookInfo[1]
            book_author = bookInfo[2]
            isbn = bookInfo[3]
            book_publisher = bookInfo[4]
            year_publish = bookInfo[5]
            print(accession_number)
            titleMessage = "Please Confirm Details to Be Correct \n \n"
            accessionnumberstr = "Accession Number: " + accession_number + " \n"
            title = "Title: " + name + " \n"
            author = "Authors: " + book_author + " \n"
            ISBN = "ISBN: " + isbn + " \n"
            publisher = "Publisher: " + book_publisher + "\n"  
            year= "Year: " + str(year_publish) + " \n"
            fullMessage = titleMessage + accessionnumberstr + title + author + ISBN + publisher + year
        except:
            messagebox.showinfo("Error","Book Number not present")
            present = False
        if Indicator == False:
            try:
                confirmation = messagebox.askyesno(message = fullMessage)
                if confirmation:
                    cur.execute(deleteBook)
                    con.commit()
                    messagebox.showinfo(title = "Success", message= "Success!")
            except:
                returnto.forget()
                returnto.pack()
    return innerFunc

def borrowBook(returnto, *inputs):
    def innerFunc():

        AccessionNumber = inputs[0].get()
        MembershipID = inputs[1].get()
        x = datetime.now()
        todayDate = x.date()
        findReservation = "select * from Reservation where accessionNo = '"+AccessionNumber+"'"
        findFine = "select * from Fine where id = '"+MembershipID+"'"
        y = x + timedelta(days = 14)
        dueDate = y.date()
        findId = "select * from Member where id = '"+MembershipID+"'"
        findBook = "select * from Book where accessionNo = '"+AccessionNumber+"'"
        findQuota = "select id, COUNT(*) as Total FROM Loan where id = '"+MembershipID+"'"
        findLoan = "select * from Loan where accessionNo = '"+AccessionNumber+"'"
        MemberPresent = True
        BookPresent = True
        borrowIndicator = True ##
        addLoan = "insert into"+ " Loan values " + "('"+MembershipID+"', '"+AccessionNumber+"', '"+str(todayDate)+"', '"+str(dueDate)+"')"

        cur.execute(findQuota)
        con.commit()
        existingQuota = cur.fetchall()
        print(existingQuota)
        if existingQuota[0][1] >= 2:
            messagebox.showinfo("Error","Member loan quota exceeded")
            borrowIndicator = False

        cur.execute(findReservation)
        con.commit()
        existingReservation = cur.fetchall()
        if existingReservation != () and borrowIndicator:
            for i in existingReservation:
                if i[0] != MembershipID or i[1] != AccessionNumber:
                    messagebox.showinfo("Error", "Book currently reserved")
                    borrowIndicator = False 
                elif i[0] ==MembershipID and i[1] == AccessionNumber:
                    borrowIndicator = True 

        cur.execute(findLoan)
        con.commit()
        existingLoan = cur.fetchall()
        if existingLoan != ():
            message = "Book currently on loan until " + str(existingLoan[0][3])
            messagebox.showinfo("Error", message)
            borrowIndicator = False
                    
        cur.execute(findFine)
        con.commit()
        existingFines = cur.fetchall()
        FineAmount = 0
        if existingFines != ():
            FineAmount += int(existingFines[0][1])
        if FineAmount > 0:
            borrowIndicator = False
            messagebox.showwarning(title=" Error", message = "Error! \n Member has Outstanding Fine of: $" + str(FineAmount))

        if borrowIndicator:
            cur.execute(findId)
            con.commit()
            MemberInfo = cur.fetchall()
            print(MemberInfo)
            if MemberInfo == ():
                messagebox.showinfo("Error","Member ID not present")
                MemberPresent = False
            else:
                name = MemberInfo[0][1]

            cur.execute(findBook)
            con.commit()
            BookInfo = cur.fetchall()
            print(MemberInfo)
            if BookInfo == ():
                messagebox.showinfo("Error","Book not present")
                BookPresent = False
            else:
                book_title = BookInfo[0][1]

        if MemberPresent and BookPresent and borrowIndicator:

            titleMessage = "Please Confirm Loan Details to Be Correct \n \n"
            accession = "Accession Number: " + AccessionNumber+"\n"
            title = "Book Title: " + book_title+"\n"
            borrow = "Borrow Date: " + str(todayDate)+"\n"
            membership = "Membership ID: " +MembershipID+ "\n"
            member = "Member Name: " +name+ "\n"
            due = "Due Date: " + str(dueDate)+"\n"
            fullMessage = accession + title + borrow + membership + member + due
            confirmation = messagebox.askyesno(title = titleMessage, message = fullMessage)
            deleteReservation = "delete from Reservation where accessionNo = '"+AccessionNumber+"' and id = '"+MembershipID+"'"

            if confirmation:
                cur.execute(addLoan)
                con.commit()
                cur.execute(deleteReservation)
                con.commit()
                messagebox.showinfo("Succes", "Book Borrowed")

    return innerFunc

def returnBook(returnto, *inputs):
    def innerFunc():

        AccessionNumber = inputs[0].get()
        ReturnDate = inputs[1].get() + " 00:00:00"
        ReturnDate = datetime.strptime(ReturnDate,'%Y-%m-%d %H:%M:%S')
        ReturnDate = ReturnDate.date()
        print(ReturnDate)
        LoanDetails = "select * from Loan where accessionNo = '"+AccessionNumber+"'"
        deleteLoan = "delete from Loan where accessionNo = '"+AccessionNumber+"'"
        present = True
        haveFine = False

        cur.execute(LoanDetails)
        existingLoan = cur.fetchall()
        if existingLoan == ():
            messagebox.showinfo("Error","Book Currently Not On Loan")
            present = False
        else:
            memberID = existingLoan[0][0]
            accessionNo = existingLoan[0][1]
            dueDate = existingLoan[0][3]
        
        diff = ReturnDate - dueDate
        if diff.days > 0:
            fineAmount = diff.days * 1
            haveFine = True
        else:
            fineAmount = 0
        titleMessage = "Please Confirm Details to Be Correct \n \n"
        member = "Member ID: " + memberID + " \n"
        accessionNo = "Accession Number: " + accessionNo + " \n"
        returnDate = "Return Date: " + str(ReturnDate) + " \n"
        FineAmount = "Fine: " + str(fineAmount) + " \n"
        fullMessage = titleMessage + member + accessionNo + returnDate + FineAmount

        addFine = "insert into Fine values ('" +memberID+ "', " + str(fineAmount) + ", '" + inputs[1].get() + "')"
        findFine = "select * from Fine where id = '"+memberID+"'"

        if haveFine and present:
            cur.execute(findFine)
            existingFine = cur.fetchall()
            if existingFine == ():
                cur.execute(addFine)
                con.commit()
            else:
                totalAmount = existingFine[0][1] + fineAmount
                updateFine = "update Fine set amountDue = " +str(totalAmount)+" where id = '"+memberID+"'"
                cur.execute(updateFine)
                con.commit()
        if present:
            confirmation = messagebox.askyesno(message = fullMessage)
            if confirmation:
                cur.execute(deleteLoan)
                con.commit()
            if haveFine:
                messagebox.showinfo(title = "Error", message= "Book returned successfully but has fines")
            else:
                messagebox.showinfo(title = "Success", message= "Success!")
        
    return innerFunc

def reserveBook(returnto, *inputs):
    def innerFunc():
        accession_num = inputs[0].get()
        memberID = inputs[1].get()
        reservationDate = inputs[2].get()
        findId = "select * from Member where id = '"+memberID+"'"
        MemberInfo = []
        findBook = "select * from Book where accessionNo = '"+accession_num+"'"
        BookInfo = []
        addReservation = "insert into"+ " Reservation values ('" + memberID + "', '" + accession_num + "', '" + reservationDate + "')"
        findReservation = "select id, COUNT(*) as Total FROM Reservation where id = '"+memberID+"'"
        findFine = "select * from Fine where id = '"+memberID+"'"
        findBookAvailable = "select accessionNo, COUNT(*) as Total FROM Reservation where accessionNo = '"+accession_num+"'"
        FineIndicator = False
        ReservationIndicator = False
        NumOfReservation = 0
        cur.execute(findReservation)
        reservationQuota = cur.fetchall()[0][1]
        if reservationQuota == 2:
            ReservationIndicator = True
            messagebox.showwarning(title=" Error", message = "Error! \n Member currently has 2 Books on Reservation.")

        cur.execute(findFine)
        existingFines = cur.fetchall()
        FineAmount = 0
        if existingFines != ():
            FineAmount += int(existingFines[0][1])
        if FineAmount > 0:
            FineIndicator = True
            messagebox.showwarning(title=" Error", message = "Error! \n Member has Outstanding Fine of: $" + str(FineAmount))

        cur.execute(findBookAvailable)
        existingReservation = cur.fetchall()[0][1]
        if existingReservation == 1:
            ReservationIndicator = True
            messagebox.showwarning(title=" Error", message = "Error! \n Book is reserved.")
        

        if FineIndicator == False and ReservationIndicator == False:
            try:
                cur.execute(findId)
                con.commit()
                for i in cur:
                    MemberInfo.append(i[1])
                name = MemberInfo[0]
            except:
                messagebox.showinfo("Error","Member ID not present")
            try:
                cur.execute(findBook)
                con.commit()
                for i in cur:
                    BookInfo.append(i[1])
                title = BookInfo[0]
            except:
                messagebox.showinfo("Error","Book Number not present")
            titleMessage = "Confirm Reservation Details To Be Correct \n \n"
            accessionnumberstr = "Accession Number: " +accession_num+" \n"
            title = "Title: " + title+" \n"
            memberIDstr = "Membership ID: " +memberID +" \n"
            memberName = "Member Name " +name+" \n"  
            reserveDatestr = "Reserve Date " +reservationDate+" \n"
            fullMessage = titleMessage + accessionnumberstr + title + memberIDstr + memberName + reserveDatestr
            try:
                confirmation = messagebox.askyesno(message = fullMessage)
                if confirmation:
                    cur.execute(addReservation)
                    con.commit()
                    messagebox.showinfo(title = "Success", message= "Success!")
            except:
                messagebox.showinfo("Error")
                returnto.forget()
                returnto.pack()

    return innerFunc

def cancelBook(returnto, *inputs):
    def innerFunc():
        accessionnum = inputs[0].get()
        memberID = inputs[1].get()
        cancellationDate = inputs[2].get()
        deleteReservation = "delete from Reservation where accessionNo = '"+accessionnum+"' and id = '"+memberID+"'"
        findId = "select * from Reservation where id = '"+memberID+"' and accessionNo = '"+accessionnum+"'"
        addCancellation = "insert into"+ " Cancellation values ('" + memberID + "', '" + accessionnum + "')"
        findId = "select * from Member where id = '"+memberID+"'"
        MemberInfo = []
        findBook = "select * from Book where accessionNo = '"+accessionnum+"'"
        BookInfo = []
        Indicator = True

        verificationQuery = "select count(*) from Reservation where id = '"+memberID+"' and accessionNo = '"+accessionnum+"'"
        try:
            cur.execute(findId)
            con.commit()
            for i in cur:
                MemberInfo.append(i[1])
            name = MemberInfo[0]
        except:
            messagebox.showinfo("Error","Member ID not present")
            Indicator = False
        try:
            cur.execute(findBook)
            con.commit()
            for i in cur:
                BookInfo.append(i[1])
            title = BookInfo[0]
        except:
            messagebox.showinfo("Error","Book Number not present")
            Indicator = False

        cur.execute(verificationQuery)
        count = cur.fetchall()
        con.commit()

        if int(count[0][0]) == 0:
            messagebox.showinfo(message = "Member Does Not Have Such Reservation")

        else:
            if Indicator:
                titleMessage = "Confirm Reservation Details To Be Correct \n \n"
                accessionnumberstr = "Accession Number: " +accessionnum+" \n"
                title = "Title: " + title+" \n"
                memberIDstr = "Membership ID: " +memberID +" \n"
                memberName = "Member Name: " +name+" \n"  
                cancelDatestr = "Cancel Date: " +cancellationDate+" \n"
                fullMessage = titleMessage + accessionnumberstr + title + memberIDstr + memberName + cancelDatestr
                try:
                    confirmation = messagebox.askyesno(message = fullMessage)
                    if confirmation:
                        cur.execute(deleteReservation)
                        con.commit()
                        messagebox.showinfo(title = "Success", message= "Success!")
                        cur.execute(addCancellation)
                        con.commit()
                except:
                    messagebox.showinfo("Error", "\nMember has no such reservation.")

    return innerFunc

def payFine(returnto, *inputs):
    def innerFunc():
        
        memberID = inputs[0].get()
        paymentDate = inputs[1].get()
        paymentAmount = int(inputs[2].get())
        findFine = "select * from Fine where id = '"+memberID+"'"
        rightAmount = True
        amountDue = 0
        updateFinePayment = "insert FinePayment values ('" +memberID+ "', '" + paymentDate +"', '" + str(paymentAmount) + "')"
        deleteFine = "delete from Fine where id = '"+memberID+"'"
        Fines = []
        cur.execute(findFine)
        existingFines = cur.fetchall()
        if existingFines == ():
            messagebox.showwarning(title= "Error", message = "Error! \nMember has no fine")
            rightAmount = False
            
        elif existingFines[0][1] != paymentAmount:
            messagebox.showwarning(title= "Error", message = "Error! \n\nIncorrect fine payment amount")
            rightAmount = False

        if rightAmount:
            titleMessage = "Please Confirm Details To Be Correct \n \n"
            memberIDstr = "Membership ID: " + memberID + " \n"
            paymentDatestr = "Payment Date: " + paymentDate + "paymentDate\n"  
            paymentAmountstr = "Payment Due: " + str(paymentAmount)+" \n \nExact Fee Only"
       
            fullMessage = titleMessage + memberIDstr + paymentDatestr + paymentAmountstr 

            confirmation = messagebox.askyesno(message = fullMessage)
            if confirmation:
                cur.execute(deleteFine)
                con.commit()
                cur.execute(updateFinePayment)
                con.commit()
                messagebox.showinfo(title = "Success", message= "Success!")

    return innerFunc

def createTableOnSearch(root, *inputs):
    
    title = ["Accesesion Number", "Title", "Authors", "ISBN", "Publisher", "Year"]
    columns = ["title", "authors", "isbn", "publisher", "yearPublish"]

    def innerfunc():

        # Data Validation

        search = ""
        for i in range(len(inputs)):
            string = inputs[i].get()
            if string != "":
                reference = i
            search += string + " "

        lst = search.split()
        length = len(lst)

        if length != 1:
            messagebox.showwarning(title= "Error", message = "Error! More than 1 or No word \n inputted for search result")
        else:

            key = lst[0]
            query = "select * from Book where " + columns[reference] + " REGEXP " +  "'\\\\b%s\\\\b'"%(key)

            cur.execute(query)
            result = cur.fetchall()
            con.commit()
            records = []
            for i in result:
                records.append(i)

            table1 = Toplevel(root)
            table1.geometry("1200x750")
            table1.title("Search Results Page 1")
            button1 = Button(table1, text = "Close Window", command = table1.destroy, padx = 20, font = ("Helvetica", 16))

            for i in range(len(title)):
                e = Label(table1, width = 20, text = title[i], bg = "white", relief = "raised", fg = "black", font = ("Helvetica", 16, "bold"))
                e.grid(row = 0, column = i)

            i = 2
            k = 2
            for record in records:
                if i == 30:
                    break

                for j in range(len(record)):
                    e = Label(table1, width = 20, text = record[j], bg = "white", relief = "raised", fg = "black", font = ("Helvetica", 16, "bold")) 
                    e.grid(row = i, column = j) 

                i += 1

            button1.grid(row = i + 1, column = 0)

            if i < len(records): 

                table2 = Toplevel(root)
                table2.geometry("1200x750") 
                table2.title("Search Results Page 2")
                button2 = Button(table2, text = "Close Window", command = table2.destroy, padx = 20, font = ("Helvetica", 16))

                for p in range(len(title)):
                    e = Label(table2, width = 20, text = title[p], bg = "white", relief = "raised", fg = "black", font = ("Helvetica", 16, "bold"))
                    e.grid(row = 0, column = p)

                for record in records[i:]:
                    for j in range(len(record)):
                        e = Label(table2, width = 20, text = record[j], bg = "white", relief = "raised", fg = "black", font = ("Helvetica", 16, "bold")) 
                        e.grid(row = k, column = j) 

                    k += 1

                button2.grid(row = k + 1, column = 0)

    return innerfunc

def createTableBooksOnLoan(root):

    title = ["Accession Number", "Title", "Authors", "ISBN", "Publisher", "Year"]

    def innerfunc():

        loanRecords = "select Loan.accessionNo, Book.title, Book.authors, Book.isbn, Book.publisher, Book.yearPublish from Loan INNER JOIN Book ON Loan.accessionNo = Book.accessionNo"
        cur.execute(loanRecords)
        result = cur.fetchall()
        con.commit()
        records = []
        for i in result:
            records.append(i)

        table1 = Toplevel(root)
        table1.geometry("1200x750")
        table1.title("Search Results Page 1")
        button1 = Button(table1, text = "Close Window", command = table1.destroy, padx = 20, font = ("Helvetica", 16))

        for i in range(len(title)):
            e = Label(table1, width = 20, text = title[i], bg = "white", relief = "raised", fg = "black", font = ("Helvetica", 16, "bold"))
            e.grid(row = 0, column = i)

        i = 2
        k = 2
        for record in records:
            if i == 30:
                break

            for j in range(len(record)):
                e = Label(table1, width = 20, text = record[j], bg = "white", relief = "raised", fg = "black", font = ("Helvetica", 16, "bold")) 
                e.grid(row = i, column = j) 

            i += 1

        button1.grid(row = i + 1, column = 0)

        if i < len(records): 

            table2 = Toplevel(root)
            table2.geometry("1200x750") 
            table2.title("Search Results Page 2")
            button2 = Button(table2, text = "Close Window", command = table2.destroy, padx = 20, font = ("Helvetica", 16))

            for p in range(len(title)):
                e = Label(table2, width = 20, text = title[p], bg = "white", relief = "raised", fg = "black", font = ("Helvetica", 16, "bold"))
                e.grid(row = 0, column = p)

            for record in records[i:]:
                for j in range(len(record)):
                    e = Label(table2, width = 20, text = record[j], bg = "white", relief = "raised", fg = "black", font = ("Helvetica", 16, "bold")) 
                    e.grid(row = k, column = j) 

                k += 1

            button2.grid(row = k + 1, column = 0)

    return innerfunc

def createTableOnReservationSearch(root):

    title = ["Accession Number", "Title", "Membership ID", "Name"]

    def innerfunc():

        records = []
        reservationRecords = "SELECT b.accessionNo, m.id, m.name, b.title FROM member AS m INNER JOIN Reservation AS r on m.id = r.id inner join Book as b on b.accessionNo = r.accessionNo"
        cur.execute(reservationRecords)
        result = cur.fetchall()
        con.commit()
        for i in result:
            records.append(i)

        table1 = Toplevel(root)
        table1.geometry("1200x750")
        table1.title("Search Results Page 1")
        button1 = Button(table1, text = "Close Window", command = table1.destroy, padx = 20, font = ("Helvetica", 16))

        for i in range(len(title)):
            e = Label(table1, width = 20, text = title[i], bg = "white", relief = "raised", fg = "black", font = ("Helvetica", 16, "bold"))
            e.grid(row = 0, column = i)

        i = 2
        k = 2
        for record in records:
            if i == 30:
                break

            for j in range(len(record)):
                e = Label(table1, width = 20, text = record[j], bg = "white", relief = "raised", fg = "black", font = ("Helvetica", 16, "bold")) 
                e.grid(row = i, column = j) 

            i += 1

        button1.grid(row = i + 1, column = 0)

        if i < len(records): 

            table2 = Toplevel(root)
            table2.geometry("1200x750") 
            table2.title("Search Results Page 2")
            button2 = Button(table2, text = "Close Window", command = table2.destroy, padx = 20, font = ("Helvetica", 16))

            for p in range(len(title)):
                e = Label(table2, width = 20, text = title[p], bg = "white", relief = "raised", fg = "black", font = ("Helvetica", 16, "bold"))
                e.grid(row = 0, column = p)

            for record in records[i:]:
                for j in range(len(record)):
                    e = Label(table2, width = 20, text = record[j], bg = "white", relief = "raised", fg = "black", font = ("Helvetica", 16, "bold")) 
                    e.grid(row = k, column = j) 

                    k += 1

            button2.grid(row = k + 1, column = 0)

    return innerfunc

def createTableOnFineSearch(root):

    title = ["Membership ID", "Name", "Faculty", "Phone Number", "Email Address"]

    def innerfunc():
        fineRecords = "select Fine.id, Member.name, Member.faculty, Member.phoneNum, Member.email from Fine INNER JOIN Member ON Fine.id = Member.id"
        cur.execute(fineRecords)
        result = cur.fetchall()
        records = []
        for i in result:
            records.append(i)

        table1 = Toplevel(root)
        table1.geometry("1200x750")
        table1.title("Search Results Page 1")
        button1 = Button(table1, text = "Close Window", command = table1.destroy, padx = 20, font = ("Helvetica", 16))

        for i in range(len(title)):
            e = Label(table1, width = 20, text = title[i], bg = "white", relief = "raised", fg = "black", font = ("Helvetica", 16, "bold"))
            e.grid(row = 0, column = i)

        i = 2
        k = 2
        for record in records:
            if i == 30:
                break

            for j in range(len(record)):
                e = Label(table1, width = 20, text = record[j], bg = "white", relief = "raised", fg = "black", font = ("Helvetica", 16, "bold")) 
                e.grid(row = i, column = j) 

            i += 1

        button1.grid(row = i + 1, column = 0)

        if i < len(records): 

            table2 = Toplevel(root)
            table2.geometry("1200x750") 
            table2.title("Search Results Page 2")
            button2 = Button(table2, text = "Close Window", command = table2.destroy, padx = 20, font = ("Helvetica", 16))

            for p in range(len(title)):
                e = Label(table2, width = 20, text = title[p], bg = "white", relief = "raised", fg = "black", font = ("Helvetica", 16, "bold"))
                e.grid(row = 0, column = p)

            for record in records[i:]:
                for j in range(len(record)):
                    e = Label(table2, width = 20, text = record[j], bg = "white", relief = "raised", fg = "black", font = ("Helvetica", 16, "bold")) 
                    e.grid(row = k, column = j) 

                k += 1

            button2.grid(row = k + 1, column = 0)

    return innerfunc

def createTableOnMemberSearch(root, input):

    title = ["Accession Number", "Title", "Authors", "ISBN", "Publisher", "Year"]

    def innerfunc():

        memberID = input.get()
        findId = "select * from Member where id = '"+memberID+"'"

        cur.execute(findId)
        con.commit()
        MemberInfo = cur.fetchall()
        print(MemberInfo)
        if MemberInfo == ():
            messagebox.showinfo("Error","Member ID not present")

        else:
            query = "select b.accessionNo, b.title, b.authors, b.isbn, b.publisher, b.yearPublish FROM book as b INNER JOIN Loan as l ON b.accessionNo = l.accessionNo WHERE l.id = '" + memberID + "'"

            cur.execute(query)
            result = cur.fetchall()
            records = []
            for i in result:
                records.append(i)

            table1 = Toplevel(root)
            table1.geometry("1200x750")
            table1.title("Search Results Page 1")
            button1 = Button(table1, text = "Close Window", command = table1.destroy, padx = 20, font = ("Helvetica", 16))
    
            for i in range(len(title)):
                e = Label(table1, width = 20, text = title[i], bg = "white", relief = "raised", fg = "black", font = ("Helvetica", 16, "bold"))
                e.grid(row = 0, column = i)

            i = 2
            k = 2
            for record in records:
                if i == 30:
                    break

                for j in range(len(record)):
                    e = Label(table1, width = 20, text = record[j], bg = "white", relief = "raised", fg = "black", font = ("Helvetica", 16, "bold")) 
                    e.grid(row = i, column = j) 

                i += 1

            button1.grid(row = i + 1, column = 0)

            if i < len(records): 

                table2 = Toplevel(root)
                table2.geometry("1200x750") 
                table2.title("Search Results Page 2")
                button2 = Button(table2, text = "Close Window", command = table2.destroy, padx = 20, font = ("Helvetica", 16))

                for p in range(len(title)):
                    e = Label(table2, width = 20, text = title[p], bg = "white", relief = "raised", fg = "black", font = ("Helvetica", 16, "bold"))
                    e.grid(row = 0, column = p)

                for record in records[i:]:
                    for j in range(len(record)):
                        e = Label(table2, width = 20, text = record[j], bg = "white", relief = "raised", fg = "black", font = ("Helvetica", 16, "bold")) 
                        e.grid(row = k, column = j) 

                        k += 1

                button2.grid(row = k + 1, column = 0)

    return innerfunc









    
