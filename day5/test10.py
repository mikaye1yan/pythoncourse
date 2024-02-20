lst1=["Jimmy","Layla", "Bob"]
lst2=["Bob","Layla","Kaitlyn","Patrica"]
lst3=["Jimmy","Layla","James"]

lst1Index= lst1.index("Bob") if "Bob" in lst1 else -1
lst2Index= lst2.index("Bob") if "Bob" in lst2 else -1
lst3Index= lst3.index("Bob") if "Bob" in lst3 else -1
print(lst1Index)
print(lst2Index)
print(lst3Index)
