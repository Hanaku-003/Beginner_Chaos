def shape_calcule():
    print("Please enter numbers only")
    length=float(input("what is the length of your Rectangle?:"))
    width=float(input("what is the width of your Rectangle?:"))
    print("calculating...")
    if length==width:
        print("wait")
        print("Checking something... 📐")
        print("well,this is a square!")
    area=length*width
    print(f"the shape's area is {area}💡")
    area_round=round(area)
    print(f"The rounding for the area unit is:{area_round}💡")
    question=input("Do you want to measure the dimension of your shape?: |yes|or |no|")
    import math
    if question.lower()=="yes":
        print("calculating")
        length_pow=length**2
        width_pow=width**2
        total=length_pow+width_pow
        dim=math.sqrt(total)
        print(dim,"💡")
        round_dim=round(dim)
        print(f"the rounding for the dimension of your shape is:{round_dim}💡")
    elif question.lower()=="no":
        print("ok")
    else:
        print("something is wrong.please try again(〜￣▽￣)〜")
    
    ques=input("(￣▽,￣)╭ wanna try again or quit?|again|or|quit|:")
   
    if ques.lower()=='again':
        print("( •̀ ω •́ )✧ Ok!")
        shape_calcule()
    elif ques.lower()=='quit':
        return
    else:
        ques_2=input("please enter 'again' or'quit'")
        if ques_2.lower()=='again':
             print("( •̀ ω •́ )✧ Ok!")
             shape_calcule()
        elif ques_2.lower()=='quit':
             return
    
shape_calcule()


