DROP TABLE IF EXISTS user_card;
DROP TABLE IF EXISTS reward_mcc;
DROP TABLE IF EXISTS merchant_mcc;
DROP TABLE IF EXISTS creditcard;
DROP TABLE IF EXISTS "user";
DROP TABLE IF EXISTS merchant;
DROP TABLE IF EXISTS reward;
DROP TABLE IF EXISTS mcc;
DROP TABLE IF EXISTS bank;
DROP TABLE IF EXISTS creditcard_network;
DROP TABLE IF EXISTS address;

CREATE TABLE IF NOT EXISTS address (
    id UUID PRIMARY KEY,
    lat FLOAT,
    long FLOAT,
    street bpchar,
    street2 bpchar,
    city bpchar,
    state bpchar,
    country bpchar,
    zip bpchar
);

CREATE TABLE IF NOT EXISTS creditcard_network (
    id int PRIMARY key,
    name bpchar not null unique,
    open_or_closed bpchar not NULL,
    logo bpchar
);

CREATE TABLE IF NOT EXISTS bank (
    id int PRIMARY KEY,
    "name" bpchar not null,
    logo bpchar,
    unique(id, "name")
);

CREATE TABLE IF NOT EXISTS mcc (
    mcc_code INT PRIMARY KEY,
    "name" bpchar not null unique,
    is_business bit NULL,
    is_category bit null,
    UNIQUE("name")
);

CREATE TABLE IF NOT EXISTS reward (
    id UUID PRIMARY KEY,
    "name" bpchar,
    pts_multiplier FLOAT,
    cashback_pct FLOAT
);

CREATE TABLE IF NOT EXISTS merchant (
    id UUID PRIMARY KEY,
    "name" bpchar not NULL,
    location_id UUID REFERENCES address(id),
    website bpchar
);
CREATE TABLE IF NOT EXISTS "user" (
    id UUID PRIMARY KEY,
    username bpchar not null unique,
    Name bpchar not null unique,
    PhoneNumber bpchar,
    Email bpchar not null unique,
    location_id UUID REFERENCES address(id),
    profile_picture bpchar
);

CREATE TABLE IF NOT EXISTS creditcard (
    id UUID PRIMARY KEY,
    name bpchar not NULL,
    network_id int REFERENCES creditcard_network(id),
    bank_id int REFERENCES bank(id)
);
CREATE TABLE IF NOT EXISTS merchant_mcc (
    merchant_id UUID REFERENCES merchant(id),
    mcc_code INT references mcc(mcc_code),
    PRIMARY KEY (merchant_id, mcc_code)
);


CREATE TABLE IF NOT EXISTS reward_mcc (
    reward_id UUID REFERENCES reward(id),
    mcc_code INT references mcc(mcc_code),
    PRIMARY KEY (reward_id, mcc_code)
);

CREATE TABLE IF NOT EXISTS user_card (   
    user_id UUID REFERENCES "user"(id),
    card_id UUID REFERENCES creditcard(id),
    PRIMARY KEY (user_id, card_id)
);

