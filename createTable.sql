CREATE TABLE Member(
id varchar(10) NOT NULL,
name varchar(25) NOT NULL,
faculty varchar(20) NOT NULL,
phoneNum varchar(11) NOT NULL,
email varchar(25) NOT NULL,
PRIMARY KEY (id));

CREATE TABLE Book(
accessionNo varchar(5) NOT NULL,
title varchar(60) NOT NULL,
authors varchar(60) NOT NULL,
isbn varchar(13) NOT NULL,
publisher varchar(50) NOT NULL,
yearPublish integer NOT NULL,
PRIMARY KEY (accessionNo));

CREATE TABLE Loan(
id varchar(10) NOT NULL,
accessionNo varchar(5) NOT NULL,
borrowDate DATE NOT NULL,
dueDate DATE NOT NULL,
PRIMARY KEY (id, accessionNo),
FOREIGN KEY (id) REFERENCES Member(id),
FOREIGN KEY (accessionNo) REFERENCES Book(accessionNo));

CREATE TABLE Reservation(
id varchar(10) NOT NULL,
accessionNo varchar(5) NOT NULL,
reserveDate DATE NOT NULL,
PRIMARY KEY (id, accessionNo),
FOREIGN KEY (id) REFERENCES Member(id),
FOREIGN KEY (accessionNo) REFERENCES Book(accessionNo));

CREATE TABLE Fine(
id varchar(10) NOT NULL,
amountDue INT NOT NULL,
fineDate DATE NOT NULL,
FOREIGN KEY (id) REFERENCES Member(id));

CREATE TABLE FinePayment(
id varchar(10) NOT NULL,
payDate DATE,
paidAmount INT);

CREATE TABLE Cancellation(
id varchar(10) NOT NULL,
accessionNo varchar(5) NOT NULL,
PRIMARY KEY (id, accessionNo),
FOREIGN KEY (id) REFERENCES Member(id),
FOREIGN KEY (accessionNo) REFERENCES Book(accessionNo));

