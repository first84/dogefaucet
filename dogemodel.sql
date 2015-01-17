CREATE TABLE balance (
   id integer NOT NULL  PRIMARY KEY,
   datetime text NOT NULL,
   amount real NOT NULL
);
CREATE TABLE waiting (
   id integer NOT NULL  PRIMARY KEY,
   datetime text NOT NULL,
   address text NOT NULL
);
CREATE TABLE processed (
   id integer NOT NULL  PRIMARY KEY,
   datetime text NOT NULL,
   payout real NOT NULL,
   number_addresses integer NOT NULL,
   txid text NOT NULL
);
CREATE TABLE processed_addresses (
    id integer NOT NULL  PRIMARY KEY,
    address text NOT NULL,
    process_id integer NOT NULL,
    FOREIGN KEY (process_id) REFERENCES processed (id)
);
/* No STAT tables available */
