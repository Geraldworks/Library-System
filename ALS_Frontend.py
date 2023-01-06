from tkinter import *
from tkinter import font
from tkmacosx import *
from ALS_Functions import *

### Set these dimensions as default
ori = Tk()
ori.title("ALS Web Application")
height, width = 1000, 1400
ori.geometry(f"{width}x{height}")

### Create all necessary frames here 

# 6 Panels
mainFrame = Frame(ori, width = width, height = height)

# Back to Main Menu Frame
backToMainMenu = Frame(ori, width = width, height = height)

# Membership Frame
memberFrame = Frame(ori, width = width, height = height)
createMemberFrame = Frame(ori, width = width, height = height)
deleteMemberFrame = Frame(ori, width = width, height = height)
updateMemberFrame = Frame(ori, width = width, height = height)
updateMemberAllDetailsFrame = Frame(ori, width = width, height = height)

# Book Frame
BookFrame = Frame(ori, width = width, height = height)
BookAcquistionFrame = Frame(ori, width = width, height = height)
BookWithdrawalFrame = Frame(ori, width = width, height = height)

# Loan Frame
LoanFrame = Frame(ori, width = width, height = height)
BorrowBookFrame = Frame(ori, width = width, height = height)
ReturnBookFrame = Frame(ori, width = width, height = height)

# Reservation Frame
ReservationFrame = Frame(ori, width = width, height = height)
ReserveBookFrame = Frame(ori, width = width, height = height)
CancelReservationFrame = Frame(ori, width = width, height = height)

# Fine Frame
FineFrame = Frame(ori, width = width, height = height)
PayFineFrame = Frame(ori, width = width, height = height)

# Reports Frame
reportsFrame = Frame(ori, width = width, height = height)
allBookSearchFrame = Frame(ori, width = width, height = height)
booksOnLoanFrame = Frame(ori, width = width, height = height) 

### This will be our default fonts
font3 = font.Font(family = "Helvetica", size = "20", weight = "bold")
font4 = font.Font(family = "Helvetica", size = "20")
font5 = font.Font(family = "Helvetica", size = "16", weight = "bold")

### All Frame Creation

## Main Frame ##

# This is to create the mainFrame
mainHeader = Label(mainFrame, text = "(ALS)", borderwidth = 5, bg = "white", padx = 350, fg = "black", font = ("Helvetica", 46, "bold"), pady = 20)
mainHeader.grid(row = 0, column = 0, pady = 50, columnspan = 3)

goToMembershipButton = Button(mainFrame, text = "Membership", pady = 30, padx = 50, command = movetosomewhere(memberFrame, mainFrame), font = font3)
goToMembershipButton.grid(row = 1, column = 0, pady = 30)

goToBooksButton = Button(mainFrame, text = "Books", pady = 30, padx = 50, command = movetosomewhere(BookFrame, mainFrame), font = font3)
goToBooksButton.grid(row = 1, column = 1, pady = 30)

goToLoansButton = Button(mainFrame, text = "Loans", pady = 30, padx = 50, command = movetosomewhere(LoanFrame, mainFrame), font = font3)
goToLoansButton.grid(row = 1, column = 2, pady = 30)

goToReservationsButton = Button(mainFrame, text = "Reservations", pady = 30, padx = 50, command = movetosomewhere(ReservationFrame,mainFrame), font = font3)
goToReservationsButton.grid(row = 2, column = 0, pady = 30)

goToFinesButton = Button(mainFrame, text = "Fines", pady = 30, padx = 50, command = movetosomewhere(FineFrame,mainFrame), font = font3)
goToFinesButton.grid(row = 2, column = 1, pady = 30)

goToReportsButton = Button(mainFrame, text = "Reports", pady = 30, padx = 50, font = font3, command = movetosomewhere(reportsFrame, mainFrame))
goToReportsButton.grid(row = 2, column = 2, pady = 30)

## Membership Frame ##

# This is to create the memberFrame 
memberHeader = Label(memberFrame, text = "Select one of the Options below:", borderwidth = 5, bg = "lightblue", padx = 350, fg = "black", font = font3, pady = 20)
memberHeader.grid(row = 0, column = 0, pady = 50, columnspan = 3)

# members = PhotoImage(file = r"C:\Wei Han\Y1S2\BT2102\Assignment 1\Gerald\ALS_Python_Code\Images\MemberImage.png").subsample(2, 2)
members = PhotoImage(file = "./Images/MemberImage.png").subsample(2, 2)
memberImage = Label(memberFrame, image = members)
memberImage.grid(row=1,column=0,rowspan=3)

creationTextBox = Label(memberFrame, text = "1. Creation", font = font3, bg = "blue", fg = "white", width = 15)
creationTextBox.grid(row = 1, column = 1)
goToMemberCreationButton = Button(memberFrame, text = "Membership creation", pady = 20, command = movetosomewhere(createMemberFrame, memberFrame))
goToMemberCreationButton.grid(row = 1, column = 2, pady = 30)

deletionTextBox = Label(memberFrame, text = "2. Deletion", font = font3, bg = "blue", fg = "white", width = 15)
deletionTextBox.grid(row = 2, column = 1)
goToDeleteMemberButton = Button(memberFrame, text = "Membership deletion", pady = 20, command = movetosomewhere(deleteMemberFrame, memberFrame))
goToDeleteMemberButton.grid(row = 2, column = 2, pady = 30)

updateTextBox = Label(memberFrame, text = "3. Update", font = font3, bg = "blue", fg = "white", width = 15)
updateTextBox.grid(row = 3, column = 1)
goToUpdateMemberButton = Button(memberFrame, text = "Membership update", pady = 20, command = movetosomewhere(updateMemberFrame, memberFrame))
goToUpdateMemberButton.grid(row = 3, column = 2, pady = 30)

returnToMainMenuButton = Button(memberFrame, text = "Back to Main Menu", command = movetosomewhere(mainFrame, memberFrame), pady = 20, padx = 400, bg = "lightblue", font = font3)
returnToMainMenuButton.grid(row = 4, column = 0, pady = 50, columnspan=3)

# This is to create the createMemberFrame
header = Label(createMemberFrame, text = "Enter your details here", borderwidth = 5, bg = "lightblue", padx = 350, fg = "black", relief = "raised", font = font3, pady = 20)
header.grid(row = 0, column = 0, pady = 100, columnspan = 4)

membershipTextBox1 = Label(createMemberFrame, text = "Membership ID", font = font3, bg = "blue", fg = "white", width = 15)
membershipTextBox1.grid(row = 1, column = 2)
membershipInputBox1 = Entry(createMemberFrame, text = "Input1", font = font4, bg = "white", fg = "black", width = 45, insertbackground = 'black')
membershipInputBox1.grid(row = 1, column = 3)
membershipInputBox1.insert(0, "A unique alphanuimeric id that distinguishes every member")

membershipTextBox2 = Label(createMemberFrame, text = "Name", font = font3, bg = "blue", fg = "white", width = 15)
membershipTextBox2.grid(row = 2, column = 2)
membershipInputBox2 = Entry(createMemberFrame, text = "Input2", font = font4, bg = "white", fg = "black", width = 45, insertbackground = 'black')
membershipInputBox2.grid(row = 2, column = 3)
membershipInputBox2.insert(0, "Enter member's name")

membershipTextBox3 = Label(createMemberFrame, text = "Faculty", font = font3, bg = "blue", fg = "white", width = 15)
membershipTextBox3.grid(row = 3, column = 2)
membershipInputBox3 = Entry(createMemberFrame, text = "Input3", font = font4, bg = "white", fg = "black", width = 45, insertbackground = 'black')
membershipInputBox3.grid(row = 3, column = 3)
membershipInputBox3.insert(0, "e.g., Computing, Engineering, Science, etc.")

membershipTextBox4 = Label(createMemberFrame, text = "Phone Number", font = font3, bg = "blue", fg = "white", width = 15)
membershipTextBox4.grid(row = 4, column = 2)
membershipInputBox4 = Entry(createMemberFrame, text = "Input4", font = font4, bg = "white", fg = "black", width = 45, insertbackground = 'black')
membershipInputBox4.grid(row = 4, column = 3)
membershipInputBox4.insert(0, "e.g., 91234567, 96508372")

membershipTextBox5 = Label(createMemberFrame, text = "Email Address", font = font3, bg = "blue", fg = "white", width = 15)
membershipTextBox5.grid(row = 5, column = 2)
membershipInputBox5 = Entry(createMemberFrame, text = "Input5", font = font4, bg = "white", fg = "black", width = 45, insertbackground = 'black')
membershipInputBox5.grid(row = 5, column = 3)
membershipInputBox5.insert(0, "e.g., ALSuser@als.edu")

createMemberButton = Button(createMemberFrame, text = "Create Member", command = makeMember(membershipInputBox1, membershipInputBox2, membershipInputBox3, membershipInputBox4, membershipInputBox5), pady = 20)
createMemberButton.grid(row = 6, column = 2, pady = 100)
returnToMainMenuButton = Button(createMemberFrame, text = "Back to Main Menu", command = movetosomewhere(mainFrame, createMemberFrame), pady = 20, padx = 15)
returnToMainMenuButton.grid(row = 6, column = 3, pady = 100)

# This is to create the deleteMemberFrame 
header = Label(deleteMemberFrame, text = "To Delete Member, Please Enter Membership ID", borderwidth = 5, bg = "lightblue", padx = 200, fg = "black", relief = "raised", font = font3, pady = 20)
header.grid(row = 0, column = 0, pady = 100, columnspan = 4)

deleteMemberTextBox1 = Label(deleteMemberFrame, text = "Membership ID", font = font3, bg = "blue", fg = "white", width = 15)
deleteMemberTextBox1.grid(row = 1, column = 1)
deleteMemberInputBox1 = Entry(deleteMemberFrame, font = font4, bg = "white", fg = "black", width = 45, insertbackground = 'black')
deleteMemberInputBox1.grid(row = 1, column = 2)
deleteMemberInputBox1.insert(0, "A unique alphanuimeric id that distinguishes every member")

deleteMemberButton = Button(deleteMemberFrame, text = "Delete Member", command = deleteMember(deleteMemberFrame, deleteMemberInputBox1), pady = 20, padx = 20)
deleteMemberButton.grid(row = 2, column = 1, pady = 100)
returnToMemberFrame = Button(deleteMemberFrame, text = "Back to Membership Menu", command = movetosomewhere(memberFrame, deleteMemberFrame), pady = 20, padx = 15)
returnToMemberFrame.grid(row = 2, column = 2, pady = 100)

# This is to create the updateMemberFrame
header = Label(updateMemberFrame, text = "To Update a Member, Please Enter Membership ID", borderwidth = 5, bg = "lightblue", padx = 200, fg = "black", relief = "raised", font = font3, pady = 20)
header.grid(row = 0, column = 0, pady = 100, columnspan = 4)

updateMemberTextBox = Label(updateMemberFrame, text = "Membership ID", font = font3, bg = "blue", fg = "white", width = 15)
updateMemberTextBox.grid(row = 1, column = 1)
updateMemberInputBox = Entry(updateMemberFrame, font = font4, bg = "white", fg = "black", width = 45, insertbackground = 'black')
updateMemberInputBox.grid(row = 1, column = 2)
updateMemberInputBox.insert(0, "A unique alphanuimeric id that distinguishes every member")

updateMemberButton = Button(updateMemberFrame, text = "Update Member", pady = 20, padx = 20, command = movetosomewhereandstore(updateMemberAllDetailsFrame, updateMemberFrame, updateMemberInputBox))
updateMemberButton.grid(row = 2, column = 1, pady = 100)
returnToMemberFrame = Button(updateMemberFrame, text = "Back to Membership Menu", command = movetosomewhere(memberFrame, updateMemberFrame), pady = 20, padx = 15)
returnToMemberFrame.grid(row = 2, column = 2, pady = 100)

# This is to create the updateMemberAllDetailsFrame
header = Label(updateMemberAllDetailsFrame, text = "Enter all your details here in all boxes", borderwidth = 5, bg = "lightblue", padx = 250, fg = "black", relief = "raised", font = font3, pady = 20)
header.grid(row = 0, column = 0, pady = 100, columnspan = 4)

updateMemberTextBox1 = Label(updateMemberAllDetailsFrame, text = "Membership ID", font = font3, bg = "blue", fg = "black", width = 15)
updateMemberTextBox1.grid(row = 1, column = 2)
updateMemberInputBox1 = Label(updateMemberAllDetailsFrame, text = "A unique alphanuimeric id that distinguishes every member", font = font4, bg = "white", fg = "grey", width = 45)
updateMemberInputBox1.grid(row = 1, column = 3)

updateMemberTextBox2 = Label(updateMemberAllDetailsFrame, text = "Name", font = font3, bg = "blue", fg = "white", width = 15)
updateMemberTextBox2.grid(row = 2, column = 2)
updateMemberInputBox2 = Entry(updateMemberAllDetailsFrame, font = font4, bg = "white", fg = "black", width = 45, insertbackground = 'black')
updateMemberInputBox2.grid(row = 2, column = 3)
updateMemberInputBox2.insert(0, "Update member's name")

updateMemberTextBox3 = Label(updateMemberAllDetailsFrame, text = "Faculty", font = font3, bg = "blue", fg = "white", width = 15)
updateMemberTextBox3.grid(row = 3, column = 2)
updateMemberInputBox3 = Entry(updateMemberAllDetailsFrame,font = font4, bg = "white", fg = "black", width = 45, insertbackground = 'black')
updateMemberInputBox3.grid(row = 3, column = 3)
updateMemberInputBox3.insert(0, "Update Faculty.. Computing, Engineering, Science, etc.")

updateMemberTextBox4 = Label(updateMemberAllDetailsFrame, text = "Phone Number", font = font3, bg = "blue", fg = "white", width = 15)
updateMemberTextBox4.grid(row = 4, column = 2)
updateMemberInputBox4 = Entry(updateMemberAllDetailsFrame, font = font4, bg = "white", fg = "black", width = 45, insertbackground = 'black')
updateMemberInputBox4.grid(row = 4, column = 3)
updateMemberInputBox4.insert(0, "Update Phone Number")

updateMemberTextBox5 = Label(updateMemberAllDetailsFrame, text = "Email Address", font = font3, bg = "blue", fg = "white", width = 15)
updateMemberTextBox5.grid(row = 5, column = 2)
updateMemberInputBox5 = Entry(updateMemberAllDetailsFrame, font = font4, bg = "white", fg = "black", width = 45, insertbackground = 'black')
updateMemberInputBox5.grid(row = 5, column = 3)
updateMemberInputBox5.insert(0, "Update email address")

updateMemberConfirmButton = Button(updateMemberAllDetailsFrame, text = "Update Member", pady = 20,
                            command = updateMember(updateMemberAllDetailsFrame ,updateMemberInputBox2, updateMemberInputBox3, updateMemberInputBox4, updateMemberInputBox5))
updateMemberConfirmButton.grid(row = 6, column = 2, pady = 100)
returnToMainMenuButton = Button(updateMemberAllDetailsFrame, text = "Back to Membership Menu", command = movetosomewhere(memberFrame, updateMemberAllDetailsFrame), pady = 20, padx = 15)
returnToMainMenuButton.grid(row = 6, column = 3, pady = 100)

## Book Frame ##

# This is to create BookFrame
# Book = PhotoImage(file = r"C:\Wei Han\Y1S2\BT2102\Assignment 1\Gerald\ALS_Python_Code\Images\BookImage.png")
Book = PhotoImage(file = "./Images/BookImage.png")
BookImage = Label(BookFrame, image = Book)
BookImage.grid(row=1,column=0,rowspan=2)

mainheader = Label(BookFrame, text = "Select one of the options below:", borderwidth = 5, bg = "lightblue", padx = 100, fg = "black", relief = "raised", font = font3, pady = 20,width=50)
mainheader.grid(row = 0, column = 0, pady = 25, columnspan = 3)
BackToMainButton = Button(BookFrame, text = "Back to Main Menu", bg = "lightblue", font = font3, padx = 350, command = movetosomewhere(mainFrame, BookFrame)) #link to main menu here?????
BackToMainButton.grid(row = 5, column = 0, pady = 25, columnspan = 3)

Acquisition= Label(BookFrame, text = "4.Acquisition", font = font3, bg = "lightblue", fg = "black", width = 15, height=5)
Acquisition.grid(row=1, column=1)
AcquistionButton = Button(BookFrame, text = "Book Acquisition", font = font4, bg = "white", fg = "black", command = movetosomewhere(BookAcquistionFrame,BookFrame), pady = 20)
AcquistionButton.grid(row=1,column=2)

Withdrawal= Label(BookFrame, text = "5.Withdrawal", font = font3, bg = "lightblue", fg = "black", width = 15,height=5)
Withdrawal.grid(row=2, column=1)
WithdrawalButton = Button(BookFrame,text = "Book Withdrawal", font = font4, bg = "white", fg = "black", command = movetosomewhere(BookWithdrawalFrame,BookFrame), pady = 20)
WithdrawalButton.grid(row=2,column=2)

# This is to create the BookAcquisition frame
header = Label(BookAcquistionFrame, text = "For New Book Acquisition, Please Enter The Required Information Below", borderwidth = 5, bg = "lightblue", padx = 90, fg = "black", relief = "raised", font = font3, pady = 20)
header.grid(row = 0, column = 1, pady = 100, columnspan = 3)

AccessionNumber= Label(BookAcquistionFrame, text = "Accession Number", font = font3, bg = "lightblue", fg = "black", width = 15)
AccessionNumber.grid(row = 1, column = 1)
AccessionInputBox = Entry(BookAcquistionFrame, font = font4, bg = "white", fg = "black", width = 55, insertbackground = 'black')
AccessionInputBox.grid(row = 1, column = 2,columnspan=3)
AccessionInputBox.insert(0, "Used to identify an instance of book")

BookTitleBox = Label(BookAcquistionFrame, text = "Title", font = font3, bg = "lightblue", fg = "black", width = 15)
BookTitleBox.grid(row = 2, column =1)
BookTitleInputBox = Entry(BookAcquistionFrame, font = font4, bg = "white", fg = "black", width = 55, insertbackground = 'black')
BookTitleInputBox.grid(row = 2, column = 2,columnspan=3)
BookTitleInputBox.insert(0, "Book Title")

AuthorBox = Label(BookAcquistionFrame, text = "Authors", font = font3, bg = "lightblue", fg = "black", width = 15)
AuthorBox.grid(row = 3, column = 1)
AuthorInputBox = Entry(BookAcquistionFrame, font = font4, bg = "white", fg = "black", width = 55, insertbackground = 'black')
AuthorInputBox.grid(row = 3, column = 2,columnspan=3)
AuthorInputBox.insert(0, "There can be multiple authors for a book")

ISBNBox = Label(BookAcquistionFrame, text = "ISBN", font = font3, bg = "lightblue", fg = "black", width = 15)
ISBNBox.grid(row = 4, column = 1)
ISBNInputBox = Entry(BookAcquistionFrame, font = font4, bg = "white", fg = "black", width = 55, insertbackground = 'black')
ISBNInputBox.grid(row = 4, column = 2,columnspan=3)
ISBNInputBox.insert(0, "ISBN Number")

PublicationBox = Label(BookAcquistionFrame, text = "Publisher", font = font3, bg = "lightblue", fg = "black", width = 15)
PublicationBox.grid(row = 5, column = 1)
PublisherInputBox = Entry(BookAcquistionFrame, font = font4, bg = "white", fg = "black", width = 55, insertbackground = 'black')
PublisherInputBox.grid(row = 5, column = 2,columnspan=3)
PublisherInputBox.insert(0, "Random House, Penguin, Cengage, Springer, etc.")

PublicationYear = Label(BookAcquistionFrame, text = "Publication Year", font = font3, bg = "lightblue", fg = "black", width = 15)
PublicationYear.grid(row = 6, column = 1)
PublisherYearInputBox = Entry(BookAcquistionFrame, font = font4, bg = "white", fg = "black", width = 55, insertbackground = 'black')
PublisherYearInputBox.grid(row = 6, column = 2,columnspan=3)
PublisherYearInputBox.insert(0, "Edition Year")

addBookButton = Button(BookAcquistionFrame, text = "Add New Book", bg="lightblue", font=font3,command = addBook(AccessionInputBox, BookTitleInputBox, AuthorInputBox, ISBNInputBox, PublisherInputBox, PublisherYearInputBox), pady = 20)
addBookButton.grid(row = 7, column = 1,pady = 100)
returnToMainMenuButton = Button(BookAcquistionFrame, text = "Back to Books Menu", bg="lightblue", font= font3,command = movetosomewhere(BookFrame, BookAcquistionFrame), pady = 20)
returnToMainMenuButton.grid(row = 7, column = 3, pady = 100)

# This is to create Book Withdrawal Frame
header2 = Label(BookWithdrawalFrame, text = "To Remove Outdated Books From System, Please Enter Required Information Below:", borderwidth = 5, bg = "lightblue", padx = 90, fg = "black", relief = "raised", font = font3, pady = 20)
header2.grid(row = 0, column = 1, pady = 100, columnspan = 3)

AccessionNumber = Label(BookWithdrawalFrame,text="Accession Number",font = font3, bg = "lightblue", fg = "black", width = 20,height=5)
AccessionNumber.grid(row=1,column=1,rowspan=3,padx=20)
AccessionInputBox = Entry(BookWithdrawalFrame,font=font4, bg = "white", fg = "black", width = 45, insertbackground = 'black')
AccessionInputBox.grid(row=3, column=2,padx=20,columnspan=3)
AccessionInputBox.insert(0, "Used to identify an instance of Book")

withdrawBookButton = Button(BookWithdrawalFrame, text= "Withdraw Book", font=font3, bg="lightblue" ,command= withdrawBook(BookWithdrawalFrame,AccessionInputBox), pady = 20, padx = 20)
withdrawBookButton.grid(row = 4, column =1,pady=85)

returnToMainMenuButton = Button(BookWithdrawalFrame, text = "Back to Books Menu", bg="lightblue", font= font3,command = movetosomewhere(BookFrame, BookWithdrawalFrame), pady = 20, padx = 20)
returnToMainMenuButton.grid(row = 4, column = 3, pady = 100,padx=90)

## Loan Frame ##

# This is to create LoanFrame
# Loan = PhotoImage(file = r"C:\Users\tanyi\OneDrive\Documents\1. Course Materials\2. BT2102\Assignment 1\BT2102-Assignment-1-main\LoansImage.png")
Loan = PhotoImage(file = "./Images/LoansImage.png")
LoanImage = Label(LoanFrame, image = Loan)
LoanImage.grid(row=1,column=0,rowspan=2)

mainheader = Label(LoanFrame, text = "Select one of the options below:", borderwidth = 5, bg = "lightblue", padx = 70, fg = "black", relief = "raised", font = font3, pady = 20,width=50)
mainheader.grid(row = 0, column = 0, pady = 25, columnspan = 5)
BackToMainButton = Button(LoanFrame, text="Back to Main Menu", bg="lightblue", font =font3,padx=350, command = movetosomewhere(mainFrame, LoanFrame)) 
BackToMainButton.grid(row =5, column = 0,pady=25,columnspan=5)

Borrow = Label(LoanFrame, text = "6.Borrow", font = font3, bg = "lightblue", fg = "black", width = 15, height=5)
Borrow.grid(row=1, column=1)
BorrowButton = Button(LoanFrame, text = "Book Borrowing", font = font4, bg = "white", fg = "black", command = movetosomewhere(BorrowBookFrame,LoanFrame), pady = 20)
BorrowButton.grid(row=1,column=2)

Return= Label(LoanFrame, text = "7.Return", font = font3, bg = "lightblue", fg = "black", width = 15,height=5)
Return.grid(row=2, column=1)
ReturnButton = Button(LoanFrame,text = "Book Return", font = font4, bg = "white", fg = "black", command = movetosomewhere(ReturnBookFrame,LoanFrame), pady = 20)
ReturnButton.grid(row=2,column=2)

# This is to create the BorrowBook frame 
header = Label(BorrowBookFrame, text = "To Borrow a Book, Please Enter Information Below", borderwidth = 5, bg = "lightblue", padx = 120, fg = "black", relief = "raised", font = font3, pady = 20)
header.grid(row = 0, column = 1, pady = 100, columnspan = 4)

AccessionNumber= Label(BorrowBookFrame, text = "Accession Number", font = font3, bg = "lightblue", fg = "black", width=20, height=5)
AccessionNumber.grid(row = 1, column = 1, rowspan=3)
AccessionInputBox = Entry(BorrowBookFrame, font = font4, bg = "white", fg = "black", width = 55, insertbackground = 'black')
AccessionInputBox.grid(row = 3, column = 2,columnspan=3,padx=20,pady=10)
AccessionInputBox.insert(0, "Used to identify an instance of book")

MembershipID= Label(BorrowBookFrame, text = "Membership ID", font = font3, bg = "lightblue", fg = "black", width=20, height=5)
MembershipID.grid(row = 4, column = 1, rowspan=3, pady=10)
MembershipIDBox = Entry(BorrowBookFrame, font = font4, bg = "white", fg = "black", width = 55, insertbackground = 'black')
MembershipIDBox.grid(row = 6, column = 2,columnspan=3,padx=20,pady=10)
MembershipIDBox.insert(0, "A unique alphanumeric id that distinguishes every member")

BorrowBookButton = Button(BorrowBookFrame, text = "Borrow Book", bg="lightblue", font=font3, command = borrowBook(BorrowBookFrame, AccessionInputBox, MembershipIDBox), pady = 20, padx = 20)
BorrowBookButton.grid(row = 7, column = 1,pady = 50)
returnToLoansMenuButton = Button(BorrowBookFrame, text = "Back to Loans Menu", bg="lightblue", font= font3, command = movetosomewhere(LoanFrame, BorrowBookFrame), pady = 20)
returnToLoansMenuButton.grid(row = 7, column = 3, pady = 50)

#This is to create ReturnBook Frame
header2 = Label(ReturnBookFrame, text = "To Return a Book, Please Enter Information Below:", borderwidth = 5, bg = "lightblue", padx = 90, fg = "black", relief = "raised", font = font3, pady = 20)
header2.grid(row = 0, column = 0, pady = 100, columnspan = 4)

AccessionNumber= Label(ReturnBookFrame, text = "Accession Number", font = font3, bg = "lightblue", fg = "black", width=20, height=5)
AccessionNumber.grid(row = 1, column = 1, rowspan=3)
AccessionInputBox = Entry(ReturnBookFrame, font = font4, bg = "white", fg = "black", width = 45, insertbackground = 'black')
AccessionInputBox.grid(row = 3, column = 2,columnspan=3,padx=20,pady=10)
AccessionInputBox.insert(0, "Used to identify an instance of book")

ReturnDate= Label(ReturnBookFrame, text = "Return Date \n (yyyy-mm-dd)", font = font3, bg = "lightblue", fg = "black", width=20, height=5)
ReturnDate.grid(row = 4, column = 1, rowspan=3, pady=10)
ReturnDateBox = Entry(ReturnBookFrame, font = font4, bg = "white", fg = "black", width = 45, insertbackground = 'black')
ReturnDateBox.grid(row = 6, column = 2, columnspan=3,padx=20,pady=10)
ReturnDateBox.insert(0, "Date of book return")

ReturnBookButton = Button(ReturnBookFrame, text = "Return Book", bg = "lightblue", font = font3, pady = 20, command = returnBook(ReturnBookFrame,AccessionInputBox, ReturnDateBox))
ReturnBookButton.grid(row = 7, column =1 ,pady=50)
returnToMainMenuButton = Button(ReturnBookFrame, text = "Back to Loans Menu", bg="lightblue", font= font3, command = movetosomewhere(LoanFrame, ReturnBookFrame), pady = 20)
returnToMainMenuButton.grid(row = 7, column = 3, pady = 50)

## Reservations ##

# This is to create ReservationFrame
# Reservation = PhotoImage(file = r"C:\Wei Han\Y1S2\BT2102\Assignment 1\Gerald\ALS_Python_Code\Images\Reservations.png").subsample(3,3)
Reservation = PhotoImage(file = "./Images/Reservations.png").subsample(3,3)
ReservationImage = Label(ReservationFrame, image = Reservation)
ReservationImage.grid(row=1,column=0,rowspan=2)

mainheader = Label(ReservationFrame, text = "Select one of the options below:", borderwidth = 5, bg = "lightblue", padx = 100, fg = "black", relief = "raised", font = font3, pady = 20,width=50)
mainheader.grid(row = 0, column = 0, pady = 25, columnspan = 3)
BackToMainButton = Button(ReservationFrame, text = "Back to Main Menu", bg = "lightblue", font = font3, padx = 350, command = movetosomewhere(mainFrame, ReservationFrame)) 
BackToMainButton.grid(row = 5, column = 0, pady = 25, columnspan = 3)

Reserve= Label(ReservationFrame, text = "8. Reserve a Book", font = font3, bg = "lightblue", fg = "black", width = 20, height=5)
Reserve.grid(row=1, column=1)
ReserveButton = Button(ReservationFrame, text = "Book Reservation", font = font4, bg = "white", fg = "black", command = movetosomewhere(ReserveBookFrame,ReservationFrame), pady = 20, padx =40)
ReserveButton.grid(row=1,column=2)

CancelReserve= Label(ReservationFrame, text = "9. Cancel Reservation", font = font3, bg = "lightblue", fg = "black", width = 20,height=5)
CancelReserve.grid(row=2, column=1)
CancelReserveButton = Button(ReservationFrame,text = "Reservation Cancellation", font = font4, bg = "white", fg = "black", command = movetosomewhere(CancelReservationFrame,ReservationFrame), pady = 20)
CancelReserveButton.grid(row=2,column=2)

# This is to create ReserveBookFrame

header = Label(ReserveBookFrame, text = "To Reserve a Book, Please Enter Information Below:", borderwidth = 5, bg = "lightblue", padx = 90, fg = "black", relief = "raised", font = font3, pady = 20, width = 50)
header.grid(row = 0, column = 1, pady = 100, columnspan = 3)

AccessionNumber= Label(ReserveBookFrame, text = "Accession Number", font = font3, bg = "lightblue", fg = "black", width = 15)
AccessionNumber.grid(row = 1, column = 1)
AccessionInputBox = Entry(ReserveBookFrame, font = font4, bg = "white", fg = "black", width = 55, insertbackground = 'black')
AccessionInputBox.grid(row = 1, column = 2,columnspan=3)
AccessionInputBox.insert(0, "Used to identify an instance of book")

MemberIDBox = Label(ReserveBookFrame, text = " Membership ID", font = font3, bg = "lightblue", fg = "black", width = 15)
MemberIDBox.grid(row = 2, column = 1)
MemberIDInputBox = Entry(ReserveBookFrame, font = font4, bg = "white", fg = "black", width = 55, insertbackground = 'black')
MemberIDInputBox.grid(row = 2, column = 2,columnspan=3)
MemberIDInputBox.insert(0, "A unique alphanumeric id that distinguishes every member")

ReserveDateBox = Label(ReserveBookFrame, text = "Reserve date \n (yyyy-mm-dd)", font = font3, bg = "lightblue", fg = "black", width = 15, pady = 20)
ReserveDateBox.grid(row = 3, column = 1)
ReserveDateInputBox = Entry(ReserveBookFrame, font = font4, bg = "white", fg = "black", width = 55, insertbackground = 'black')
ReserveDateInputBox.grid(row = 3, column = 2,columnspan=3)
ReserveDateInputBox.insert(0, "Date of book reservation")

ReserveBookButton = Button(ReserveBookFrame, text = "Reserve Book", bg="lightblue", font=font3,command = reserveBook(ReserveBookFrame,AccessionInputBox, MemberIDInputBox, ReserveDateInputBox), pady = 20)
ReserveBookButton.grid(row = 7, column = 1,pady = 100) 
returnToMainMenuButton = Button(ReserveBookFrame, text = "Back to Reservations Menu", bg="lightblue", font= font3,command = movetosomewhere(ReservationFrame, ReserveBookFrame), pady = 20)
returnToMainMenuButton.grid(row = 7, column = 3, pady = 100)

# This is to make cancelReservation frame #

header = Label(CancelReservationFrame, text = "To Cancel a Reservation, Please Enter Information Below:", borderwidth = 5, bg = "lightblue", padx = 90, fg = "black", relief = "raised", font = font3, pady = 20, width = 50)
header.grid(row = 0, column = 1, pady = 100, columnspan = 4)

AccessionNumber= Label(CancelReservationFrame, text = "Accession Number", font = font3, bg = "lightblue", fg = "black", width = 15)
AccessionNumber.grid(row = 1, column = 1)
AccessionInputBox = Entry(CancelReservationFrame, font = font4, bg = "white", fg = "black", width = 55, insertbackground = 'black')
AccessionInputBox.grid(row = 1, column = 2,columnspan=3)
AccessionInputBox.insert(0, "Used to identify an instance of book")

MemberIDBox = Label(CancelReservationFrame, text = "Membership ID", font = font3, bg = "lightblue", fg = "black", width = 15)
MemberIDBox.grid(row = 2, column = 1)
MemberIDInputBox = Entry(CancelReservationFrame, font = font4, bg = "white", fg = "black", width = 55, insertbackground = 'black')
MemberIDInputBox.grid(row = 2, column = 2,columnspan=3)
MemberIDInputBox.insert(0, "A unique alphanumeric id that distinguishes every member")

CancelDateBox = Label(CancelReservationFrame, text = "Cancel Date \n (yyyy-mm-dd)", font = font3, bg = "lightblue", fg = "black", width = 15, pady = 20)
CancelDateBox.grid(row = 3, column = 1)
CancelDateInputBox = Entry(CancelReservationFrame, font = font4, bg = "white", fg = "black", width = 55, insertbackground = 'black')
CancelDateInputBox.grid(row = 3, column = 2,columnspan=3)
CancelDateInputBox.insert(0, "Date of Reservation Cancellation")

CancelReservationButton = Button(CancelReservationFrame, text = "Cancel Reservation", bg="lightblue", font=font3,command = cancelBook(CancelReservationFrame,AccessionInputBox, MemberIDInputBox, CancelDateInputBox), pady = 20)
CancelReservationButton.grid(row = 7, column = 1,pady = 100)  
returnToMainMenuButton = Button(CancelReservationFrame, text = "Back to Reservations Menu", bg="lightblue", font= font3,command = movetosomewhere(ReservationFrame, CancelReservationFrame), pady = 20)
returnToMainMenuButton.grid(row = 7, column = 4, pady = 100)


## Fines ##

# This is to create Fines frame

# Fine = PhotoImage(file = r"C:\Wei Han\Y1S2\BT2102\Assignment 1\Gerald\ALS_Python_Code\Images\Fines.png")
Fine = PhotoImage(file = "./Images/Fines.png")
FineImage = Label(FineFrame, image = Fine)
FineImage.grid(row=1,column=0)

mainheader = Label(FineFrame, text = "Select one of the options below:", borderwidth = 5, bg = "lightblue", padx = 100, fg = "black", relief = "raised", font = font3, pady = 20,width=50)
mainheader.grid(row = 0, column = 0, pady = 25, columnspan = 3)
BackToMainButton = Button(FineFrame, text = "Back to Main Menu", bg = "lightblue", font = font3, padx = 350, command = movetosomewhere(mainFrame, FineFrame)) 
BackToMainButton.grid(row = 5, column = 0, pady = 25, columnspan = 3)

PayFine= Label(FineFrame, text = "10. Payment", font = font3, bg = "lightblue", fg = "black", width = 20, height =3)
PayFine.grid(row=1, column=1)
PayFineButton = Button(FineFrame, text = "Fine Payment", font = font4, bg = "white", fg = "black", command = movetosomewhere(PayFineFrame,FineFrame), pady = 20, padx =40)
PayFineButton.grid(row=1,column=2)

#This is to create PayFine Frame

header = Label(PayFineFrame, text = "To Pay a Fine, Please Enter Information Below:", borderwidth = 5, bg = "lightblue", padx = 90, fg = "black", relief = "raised", font = font3, pady = 20, width = 50)
header.grid(row = 0, column = 1, pady = 100, columnspan = 4)

MemberIDBox = Label(PayFineFrame, text = "Membership ID", font = font3, bg = "lightblue", fg = "black", width = 15)
MemberIDBox.grid(row = 1, column = 1)
MemberIDInputBox = Entry(PayFineFrame, font = font4, bg = "white", fg = "black", width = 55, insertbackground = 'black')
MemberIDInputBox.grid(row = 1, column = 2,columnspan=3)
MemberIDInputBox.insert(0, "A unique alphanumeric id that distinguishes every member")

PaymentDateBox = Label(PayFineFrame, text = "Payment Date \n (yyyy-mm-dd)", font = font3, bg = "lightblue", fg = "black", width = 15, pady = 20)
PaymentDateBox.grid(row = 2, column = 1)
PaymentDateInputBox = Entry(PayFineFrame, font = font4, bg = "white", fg = "black", width = 55, insertbackground = 'black')
PaymentDateInputBox.grid(row = 2, column = 2,columnspan=3)
PaymentDateInputBox.insert(0, "Date Payment Received")

PaymentAmountBox = Label(PayFineFrame, text = "Payment Amount", font = font3, bg = "lightblue", fg = "black", width = 15)
PaymentAmountBox.grid(row = 3, column = 1)
PaymentAmountInputBox = Entry(PayFineFrame, font = font4, bg = "white", fg = "black", width = 55, insertbackground = 'black')
PaymentAmountInputBox.grid(row = 3, column = 2,columnspan=3)
PaymentAmountInputBox.insert(0, "Total fine amount")

PayFineButton = Button(PayFineFrame, text = "Pay Fine", bg="lightblue", font=font3,command = payFine(PayFineFrame, MemberIDInputBox, PaymentDateInputBox,PaymentAmountInputBox), pady = 20, padx=5)
PayFineButton.grid(row = 6, column = 1,pady = 100)  
returnToMainMenuButton = Button(PayFineFrame, text = "Back to Fines Menu", bg="lightblue", font= font3,command = movetosomewhere(FineFrame, PayFineFrame), pady = 20)
returnToMainMenuButton.grid(row = 6, column = 4, pady = 100)

## Reports ##

# This is to create the reportsFrame 
Header = Label(reportsFrame, text = "Select one of the Options below:", borderwidth = 5, bg = "lightblue", padx = 350, fg = "black", font = font3, pady = 20)
Header.grid(row = 0, column = 0, pady = 50, columnspan = 4)

# reports = PhotoImage(file = r"C:\Wei Han\Y1S2\BT2102\Assignment 1\Gerald\ALS_Python_Code\Images\MemberImage.png").subsample(2, 2)
reports = PhotoImage(file = "./Images/ReportsImage.png").subsample(3, 3)
reportsImage = Label(reportsFrame, image = reports)
reportsImage.grid(row=1,column=0,rowspan=4)

BookSearchTextBox = Label(reportsFrame, text = "11. Book Search", font = font5, bg = "blue", fg = "white", width = 34)
BookSearchTextBox.grid(row = 1, column = 1, columnspan = 2)
goToBookSearchButton = Button(reportsFrame, text = "A member can perform a search \n on the collection of books.", padx = 47, pady = 20, command = movetosomewhere(allBookSearchFrame, reportsFrame))
goToBookSearchButton.grid(row = 1, column = 3, pady = 10)

booksOnLoanTextBox = Label(reportsFrame, text = "12. Books on Loan", font = font5, bg = "blue", fg = "white", width = 34)
booksOnLoanTextBox.grid(row = 2, column = 1, columnspan = 2)
goToBooksOnLoanButton = Button(reportsFrame, text = "This functions displays all the books \n currently on loan to members.", pady = 20, padx = 38, command = createTableBooksOnLoan(ori)) # Create a frame to display the table
goToBooksOnLoanButton.grid(row = 2, column = 3, pady = 10)

booksOnReservationTextBox = Label(reportsFrame, text = "13. Books on Reservation", font = font5, bg = "violet", fg = "white", width = 34)
booksOnReservationTextBox.grid(row = 3, column = 1, columnspan = 2)
goToBooksOnReservationButton = Button(reportsFrame, text = "This functions displays all the books \n that members have reserved.", pady = 20, padx = 36, command = createTableOnReservationSearch(ori)) # create a frame to display the table
goToBooksOnReservationButton.grid(row = 3, column = 3, pady = 10)

outstandingFinesTextBox = Label(reportsFrame, text = "14. Outstanding Fines", font = font5, bg = "purple", fg = "white", width = 34)
outstandingFinesTextBox.grid(row = 4, column = 1, columnspan = 2)
goToOutstandingFinesButton = Button(reportsFrame, text = "This functions displays all the members \n that have outstanding fines.", pady = 20, padx = 30, command = createTableOnFineSearch(ori)) # create a frame to display the table
goToOutstandingFinesButton.grid(row = 4, column = 3, pady = 10)

updateTextBox = Label(reportsFrame, text = "15. Books on Loan to Member", font = font5, bg = "purple", fg = "white", width = 34)
updateTextBox.grid(row = 5, column = 1, columnspan = 2)
goToUpdateMemberButton = Button(reportsFrame, text = "This functions displays all the books a member \n identified by the membership id has borrowed.", pady = 20, padx = 10, command = movetosomewhere(booksOnLoanFrame, reportsFrame))
goToUpdateMemberButton.grid(row = 5, column = 3, pady = 10)

returnToMainMenuButton = Button(reportsFrame, text = "Back to Main Menu", command = movetosomewhere(mainFrame, reportsFrame), pady = 20, padx = 400, bg = "lightblue", font = font3)
returnToMainMenuButton.grid(row = 6, column = 0, pady = 30, columnspan=4)

# This is to create the allBookSearchFrame
header = Label(allBookSearchFrame, text = "Search based on ONE of the categories below: \n \n ( Please enter only ONE word and \n leave the other boxes BLANK )", borderwidth = 5, bg = "cyan", padx = 200, fg = "black", relief = "raised", font = font3, pady = 20)
header.grid(row = 0, column = 0, pady = 100, columnspan = 4)

TitleTextBox = Label(allBookSearchFrame, text = "Title", font = font3, bg = "blue", fg = "white", width = 15)
TitleTextBox.grid(row = 1, column = 0, padx = 10)
TitleInputBox = Entry(allBookSearchFrame, font = font4, bg = "white", fg = "black", width = 45, insertbackground = 'black')
TitleInputBox.grid(row = 1, column = 1, columnspan=2)
TitleLabel = Label(allBookSearchFrame, text = "Book Name", font = font5, bg = "blue", fg = "white", width = 30)
TitleLabel.grid(row = 1, column = 3, padx = 10)

AuthorsTextBox = Label(allBookSearchFrame, text = "Authors", font = font3, bg = "blue", fg = "white", width = 15)
AuthorsTextBox.grid(row = 2, column = 0, padx = 10)
AuthorsInputBox = Entry(allBookSearchFrame, font = font4, bg = "white", fg = "black", width = 45, insertbackground = 'black')
AuthorsInputBox.grid(row = 2, column = 1, columnspan=2)
AuthorsLabel = Label(allBookSearchFrame, text = "There can be multiple authors \n for a book", font = font5, bg = "blue", fg = "white", width = 30)
AuthorsLabel.grid(row = 2, column = 3, padx = 10)

ISBNTextBox = Label(allBookSearchFrame, text = "ISBN", font = font3, bg = "blue", fg = "white", width = 15)
ISBNTextBox.grid(row = 3, column = 0, padx = 10)
ISBNInputBox = Entry(allBookSearchFrame, font = font4, bg = "white", fg = "black", width = 45, insertbackground = 'black')
ISBNInputBox.grid(row = 3, column = 1, columnspan=2)
ISBNLabel = Label(allBookSearchFrame, text = "ISBN Number", font = font5, bg = "blue", fg = "white", width = 30)
ISBNLabel.grid(row = 3, column = 3, padx = 10)

PublisherTextBox = Label(allBookSearchFrame, text = "Publisher", font = font3, bg = "blue", fg = "white", width = 15)
PublisherTextBox.grid(row = 4, column = 0, padx = 10)
PublisherInputBox = Entry(allBookSearchFrame, font = font4, bg = "white", fg = "black", width = 45, insertbackground = 'black')
PublisherInputBox.grid(row = 4, column = 1, columnspan=2)
PublisherLabel = Label(allBookSearchFrame, text = "Springer, Cengage, etc.", font = font5, bg = "blue", fg = "white", width = 30)
PublisherLabel.grid(row = 4, column = 3, padx = 10)

PublicationYearTextBox = Label(allBookSearchFrame, text = "Publication Year", font = font3, bg = "blue", fg = "white", width = 15)
PublicationYearTextBox.grid(row = 5, column = 0, padx = 10)
PublicationYearInputBox = Entry(allBookSearchFrame, font = font4, bg = "white", fg = "black", width = 45, insertbackground = 'black')
PublicationYearInputBox.grid(row = 5, column = 1, columnspan=2)
PublicationYearLabel = Label(allBookSearchFrame, text = "Edition year", font = font5, bg = "blue", fg = "white", width = 30)
PublicationYearLabel.grid(row = 5, column = 3, padx = 10)

searchBookButton = Button(allBookSearchFrame, text = "Search Book", pady = 20, padx = 30, font = font3, command = createTableOnSearch(ori, TitleInputBox, AuthorsInputBox, ISBNInputBox, PublisherInputBox, PublicationYearInputBox)) # Add a function to display table based on some condition
searchBookButton.grid(row = 6, column = 1, pady = 30)

backToReportsMenuButton = Button(allBookSearchFrame, text = "Back to Reports Menu", pady = 20, command = movetosomewhere(reportsFrame, allBookSearchFrame), font = font3)
backToReportsMenuButton.grid(row = 6, column = 2, pady = 30)

# This is to create the booksOnLoanFrame
header = Label(booksOnLoanFrame, text = "Books on Loan to Member", borderwidth = 5, bg = "cyan", padx = 200, fg = "black", relief = "raised", font = font3, pady = 20)
header.grid(row = 0, column = 0, pady = 100, columnspan = 4)

memberID = Label(booksOnLoanFrame,text="Membership ID",font = font3, bg = "cyan", fg = "black", width = 20,height=5)
memberID.grid(row=1,column=1,padx=20)
memberIDInputBox = Entry(booksOnLoanFrame,font=font4, bg = "white", fg = "black", width = 45, insertbackground = 'black')
memberIDInputBox.grid(row=1, column=2,padx=20)
memberIDInputBox.insert(0, "A unique alphanumeric id that distinguishes every member")

withdrawBookButton = Button(booksOnLoanFrame, text= "Search Member", font=font3, bg="cyan", pady = 20, padx = 20, command = createTableOnMemberSearch(ori, memberIDInputBox)) # Add a function to search member and display table
withdrawBookButton.grid(row = 2, column =1,pady=85)

returnToReportsMenuButton = Button(booksOnLoanFrame, text = "Back to Reports Menu", bg="cyan", font= font3,command = movetosomewhere(reportsFrame, booksOnLoanFrame), pady = 20, padx = 20)
returnToReportsMenuButton.grid(row = 2, column = 2, pady = 100,padx=90)

### Pack everything in
mainFrame.pack()