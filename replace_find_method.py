#replace() method
string="she is a good dancer and she is beautiful"
#print(string.replace(" ","_"))
#print(string.replace("is","was",1))



#find() method
#print(string.find("is"))
is_pos1=string.find("is")
is_pos2=string.find("is", is_pos1 + 1)
print (is_pos2)



