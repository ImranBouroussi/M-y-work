hedelmät ={"banaani", "omena", "tomaatti", "kirsikka"}
vihannekset = {"tinaatti", "peruna", "porkkana", "munakoiso"}
marjat = {"mustikka", "mansikka", "kirsikka", "munakoiso"}

print("1 ", *hedelmät & marjat)
print("2 ", *vihannekset - hedelmät)
print("3 ", *vihannekset | hedelmät | marjat)
print("4 ", *hedelmät | marjat - vihannekset)
print("5 ", *hedelmät ^ vihannekset ^ marjat)