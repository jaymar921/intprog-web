# Project: INTPROG-HAUS
> Members
- Abejar, Jayharron Mar (LEADER)
- Cempron, Trisha Ann
- Cuico, Harold
- Elim, Daisy May
- Ministerio, Jemaica
## Category: 
> Home and Living
# Database [intprog_haus]
```sql
cmd_command: create database intprog_haus;
```
# [Tables]
## Users
```sql
create table users(id int primary key, lastname varchar(50) not null, firstname varchar(50) not null, email varchar(50) not null, contact varchar(11) not null, password varchar(32) not null) engine = innodb;
```
- ID (int 10) primary key
- Lastname (varchar 50)
- Firstname (varchar 50)
- Email (varchar 50)
- Contact (varchar 11)
- Password (varchar 32) - Hashed (MD5)
## Output samples
<img align="left" width="384" height="240" src="https://github.com/jaymar921/intprog-web/blob/master/ProjectFiles/static/images/haus1.png"/>
<img align="left" width="384" height="240" src="https://github.com/jaymar921/intprog-web/blob/master/ProjectFiles/static/images/haus2.png"/>
