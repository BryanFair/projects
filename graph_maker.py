#created on 06/01/2024
#basic python code to create a graph by determining the plotpoints and the x/y axis
#first project so there will be probably inefficiencies in the code


OL = "    "
Xaxis_list = []
I = int(input("enter the X axis: "))
I+= 1
for x in range(1, I):
    Xaxis_list.append(x)



x_axis ="\n   "

Xaxis_length = len(Xaxis_list)

for y in range(Xaxis_length):
    
    b = "  " + str(Xaxis_list[y])
    x_axis += b
    OL += "‾‾‾" 




Y_axis = ""
Yaxis_list = []
IY = int(input("enter the Y axis: "))
for a in range(IY, 0, -1):
    Yaxis_list.append(a)





Y_axisB =" |\n"


Yaxis_length = len(Yaxis_list)

for b in range(Yaxis_length):
    if Yaxis_list[b] > 9:            
        
        Y_axisB ="|\n"
        N = str(Yaxis_list[b]) + Y_axisB
        Y_axis += N
        

    elif Yaxis_list[b] < 10:

        Y_axisB =" |\n"
        N = str(Yaxis_list[b]) + Y_axisB
        Y_axis += N
        
print(Y_axis + OL + x_axis)



split = Y_axis.splitlines()


PP_list=[]

for i in Xaxis_list:
    PP = int(input("\n now enter the plotpoint for {} on the x axis: ".format(i)))
    while PP >  Xaxis_list[-1]:
         print("WARNING, the number inputted is too big. \nenter something equal to or smaller than {}".format(Xaxis_list[-1]))
         #asks for the number again
         PP = int(input("\n now enter the plotpoint for {} on the x axis: ".format(i)))

    if PP <= Xaxis_list[-1]:
     PP_list.append(PP)
     print("\n you have chosen: {}".format(PP))


new_split = []
for ya, S in zip(Yaxis_list, split):
            for P in PP_list:
                if P >= ya:
                    S += '  #'
                else:
                    S += '   '
            new_split.append(S)

Lbreak = '\n'
content = Lbreak.join(new_split)
content += '\n'+ OL + x_axis
print(content)
