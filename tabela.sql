CREATE TABLE Loyalty 
(
    ID_cliente NOT NULL INT PRIMARY KEY,
    Sobrenome_cliente VARCHAR(50),
    Nome_cliente VARCHAR(50),
    Numero_fidelidade INTEGER NOT NULL VARCHAR(20),
    Numero_contato VARCHAR(20),
    Email VARCHAR(100),
    Saldo_pontos INTEGER
);

INSERT INTO Loyalty
values (1, "Alves", "Diego", "00001", "83999277456", "diegoalves@hotmail.com", 10000)""