#Following definition will split numbers to be easier to read.
def number_divider(a):
    a = str(a)
    length = len(a)
    cut = length
    while cut >= 4:
        cut -= 3
        a = a[:cut] + "\'" + a[cut:]
    return a

#Following definiton will cover the patrol calculations.
def patrol_calculator():
    final_draft = "**Contracted Patrol by (name)** \n \n **Bonuses**"
    question = int(input("Did the event take over 40 minutes? \n Choices: \n Type 1 for yes \n Type 2 for no \n"))
    if question == 1:
        total = 375000
        final_draft = final_draft + "\n Minimum Payment: $375'000"
    elif question == 2:
        total = 250000
        final_draft = final_draft + "\n Minimum Payment: $250'000"
    question = int(input("Were at lest 4 settlement cleared? \n Choices: \n Type 1 for yes \n Type 2 for no \n"))
    if question == 1:
        total += 50000
        final_draft = final_draft + "\n 4+ Settlements cleared: $50'0000"
    question = int(input("How many main bases were cleared? \n Type the number below \n"))
    total += question * 100000
    final_draft = final_draft + f"\n {question}x Main Bases cleared: $" + number_divider(question * 100000)
    question = int(input("Was 1 wave held in at least 4 locations? \n Choices: \n Type 1 for yes \n Type 2 for no \n"))
    if question == 1:
        total += 100000
        final_draft = final_draft + "\n Waves held: $100'000"
    final_draft = final_draft + f"\n \n *Sub-Total: " + number_divider(total) + "*"
    # All penalities are calculated below from here on
    final_draft = final_draft + " \n \n **KIA Penalities**"
    question = int(input("How many KIA's? \n"))
    total -= question * 50000
    final_draft = final_draft + f"\n {question}x KIA's: -$" + number_divider(question * 100000)
    if question == 0:
        total += 150000
        final_draft = final_draft + "\n 0 KIA's: $150'000"
    elif question >= 5 and question <= 8:
       total -= 100000
       final_draft = final_draft + "\n 5-8 KIA's: -$100'000"
    elif question >= 9 and question <= 12:
        total -= 200000
        final_draft = final_draft + "\n 9-12 KIA's: -$200'000"
    elif question >= 13 and question <= 16:
        total -= 350000
        final_draft = final_draft + "\n 13-16 KIA's: -$350'000" 
    elif question > 16:
        total -= 500000
        final_draft = final_draft + "\n 16+ KIA's: -$500'000"
    question = int(input("How many VDIA's? \n"))
    if question == 0:
        total += 75000
        final_draft = final_draft + "\n 0 VDIA's: $75'000"
    elif question >= 1 and question <= 2:
        total -= 100000
        final_draft = final_draft + "\n 1-2 VDIA's: -$100'000"
    elif question >= 3 and question <= 4:
        total -= 200000
        final_draft = final_draft + "\n 3-4 VDIA's: -$200'000"
    elif question >= 5:
        total -= 500000
        final_draft = final_draft + "\n 5+ VDIA's: -$500'000"
#Totals and final formatting
    if total >= 0:
        final_draft = final_draft + f"\n \n **Total: ${number_divider(total)}**"
    else:
        final_draft = final_draft + f"\n \n **Total: -${number_divider(total)}**"
    return final_draft

#User callings
print(patrol_calculator())







#This is a automation for financial agents. This code belongs to AxaQuilPre. Any reproduction or inauthorized use is prohibited. 
