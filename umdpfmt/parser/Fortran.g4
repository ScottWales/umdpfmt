grammar Fortran;

fortranFile: r* EOF ;

r: 'hello' ID ;
ID: [a-z]+ ;
// WS: [ \t\r\n]+ -> skip ;
