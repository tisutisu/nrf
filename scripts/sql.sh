create database nf_db;

use nf_db;

create table profiles (nfid varchar(100), nftype varchar(100), ip varchar(100), port varchar(100));

insert into profiles values ("100", "AMF", "10.10.10.10", "8888");
insert into profiles values ("200", "SMF", "11.11.11.11", "9999");
