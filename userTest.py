import sqlQuer

database = sqlQuer.Database()

#database.addPlayer('virat Kholi',10,'batsman','RCB', 'right-arm pace','right')

dic = {
    'runs_to_Lspin' : 1203,
    'runs_to_Rspin' : 1353,
    'runs_to_Rpace' : 2312,
    'runs_to_Lpace' : 1344,
    'out_to_Lspin'  : 12,
    'out_to_Rspin'  : 24,
    'out_to_Rpace'  : 6,
    'out_to_Lpace'  : 15,
    'balls_Lspin'   : 902,
    'balls_Rspin'   : 945,
    'balls_Rpace'   : 1564,
    'balls_Lpace'   : 985,
    'pos' : 'top',
    'inng' : 60,
    'best' : 123
}

database.AddBattingInfo(1,dic)