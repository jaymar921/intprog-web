# Database [intprog_haus]
> cmd_command: create database intprog_hause;
# [Tables]
## Users
> cmd_command: create table users(ID int(10) not null, Email varchar(50) not null, Password varchar(50) not null, primary key(ID)) engine = innodb;
- ID (int 10) primary key
- Email (varchar 50)
- Password (varchar 50) - Hashed (MD5)