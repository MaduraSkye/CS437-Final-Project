create table USERS (
    USER_ID serial primary key,
    USERNAME varchar(255) not null,
    PASSWORD varchar(255) not null
);

create table CLOSET_INFO (
    USER_ID integer REFERENCES USERS(USER_ID),
    CLOSET_ID serial,
    CLOSET_NAME varchar(255) not null,
    CLOSET_TYPE varchar(255) not null,
    CLOSET_LOCATION varchar(255) not null,
    CLOSET_SIZE varchar(255) not null,
    CLOSET_COLOR varchar(255) not null,
    PRIMARY KEY (USER_ID, CLOSET_ID)
);

create table CLOSET_STATUS (
    USER_ID integer,
    CLOSET_ID integer,
    HANGER_NUMBER int not null,
    CLOTHING_ITEM_ID int not null,
    STATUS boolean,
    PRIMARY KEY (USER_ID, CLOSET_ID, HANGER_NUMBER, CLOTHING_ITEM_ID),
    FOREIGN KEY (USER_ID, CLOSET_ID) REFERENCES CLOSET_INFO(USER_ID, CLOSET_ID)
);

create table CLOTHING_ITEM (
    USER_ID integer,
    CLOTHING_ITEM_ID integer,
    CLOTHING_ITEM_NAME varchar(255) not null,
    CLOTHING_ITEM_FILE_PATH varchar(255) not null,
    PRIMARY KEY (USER_ID, CLOTHING_ITEM_ID),
    FOREIGN KEY (USER_ID) REFERENCES USERS(USER_ID)
);

create table OUTFIT_INFO (
    USER_ID integer,
    OUTFIT_ID serial,
    OUTFIT_NAME varchar(255) not null,
    CLOTHING_ITEM_ID integer,
    PRIMARY KEY (USER_ID, OUTFIT_ID, CLOTHING_ITEM_ID),
    FOREIGN KEY (USER_ID, CLOTHING_ITEM_ID) REFERENCES CLOTHING_ITEM(USER_ID, CLOTHING_ITEM_ID)
);