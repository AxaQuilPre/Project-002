#Following definiton will cover the patrol calculations.
def number_divider(a):
    a = str(a)
    length = len(a)
    cut = length
    while cut >= 4:
        cut -= 3
        a = a[:cut] + "\'" + a[cut:]
    return a

def patrol_calculator():
    final_draft = "**Contracted Patrol by (name)** \n Link: \n \n **Bonuses**"
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
    final_draft = final_draft + f"\n {question}x KIA's: -$" + number_divider(question * 50000)
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
        total = total * -1
        final_draft = final_draft + f"\n \n **Total: -${number_divider(total)}**"
    return final_draft

def hardcore_calculator():
    final_draft = "**Hardcore Patrol by (name)** \n Link: \n \n **Bonuses**"
    question = int(input("Did the event take over 50 minutes? Was a main base raided? \n Choices: \n Type 1 for less than 50 min \n Type 2 for more than 50 min \n Type 3 for more than 50min w/ main base raided \n"))
    if question == 1:
        total = 500000
        final_draft = final_draft + "\n Minimum Payment: $500'000"
    elif question == 2:
        total = 750000
        final_draft = final_draft + "\n Minimum Payment: $750'000"
    else:
        total = 1250000
        final_draft = final_draft + "\n Minimum Payment: $1'250'000"
    question = int(input("Were at lest 4 settlement cleared? \n Choices: \n Type 1 for yes \n Type 2 for no \n"))
    if question == 1:
        total += 250000
        final_draft = final_draft + "\n 4+ Settlements cleared: $250'0000"
    question = int(input("How many main bases were cleared? \n Type the number below \n"))
    total += question * 200000
    final_draft = final_draft + f"\n {question}x Main Bases cleared: $" + number_divider(question * 200000)
    question = int(input("Were 5 settlements cleared with 0 KIA's? \n Choices: \n Type 1 for yes \n Type 2 for no \n"))
    if question == 1:
        total += 350000
        final_draft = final_draft + "\n 5 settlements cleared with 0 KIA's: $350'000"
    question = int(input("Were 6 settlements cleared with 1 KIA or less? \n Choices: \n Type 1 for yes \n Type 2 for no \n"))
    if question == 1:
        total += 500000
        final_draft = final_draft + "\n 6 settlements cleared with 1 KIA or less: $500'000"
    question = int(input("How many main bases were cleared with 1 KIA or less? \n Type the number below \n"))
    total += question * 750000
    final_draft = final_draft + f"\n {question}x Main Bases cleared with 1 KIA or less: $" + number_divider(question * 750000)
    final_draft = final_draft + f"\n \n *Sub-Total: " + number_divider(total) + "*"
    
    # All penalities are calculated below from here on
    final_draft = final_draft + " \n \n **KIA Penalities**"
    question = int(input("How many KIA's? \n"))
    total -= question * 100000
    final_draft = final_draft + f"\n {question}x KIA's: -$" + number_divider(question * 100000)
    if question == 0:
        total += 500000
        final_draft = final_draft + "\n 0 KIA's: $500'000"
    elif question >= 3 and question <= 4:
       total -= 1500000
       final_draft = final_draft + "\n 3-4 KIA's: -$1'500'000"
    elif question >= 5 and question <= 8:
        total -= 3000000
        final_draft = final_draft + "\n 5-8 KIA's: -$3'000'000"
    elif question > 9:
        total -= 6000000
        final_draft = final_draft + "\n 9+ KIA's: -$6'000'000"
    question = int(input("How many VDIA's? \n"))
    if question == 0:
        total += 250000
        final_draft = final_draft + "\n 0 VDIA's: $250'000"
    elif question >= 1 and question <= 2:
        total -= 500000
        final_draft = final_draft + "\n 1-2 VDIA's: -$500'000"
    elif question >= 3:
        total -= 1000000
        final_draft = final_draft + "\n 3+ VDIA's: -$1'000'000"
#Totals and final formatting
    if total >= 0:
        final_draft = final_draft + f"\n \n **Total: ${number_divider(total)}**"
    else:
        total = total * -1
        final_draft = final_draft + f"\n \n **Total: -${number_divider(total)}**"
    return final_draft

def divisional_calculator():
    final_draft = "**Contracted Patrol by (name)** \n Link: \n \n **Bonuses**"
    question = int(input("Did the event take over 40 minutes? \n Choices: \n Type 1 for yes \n Type 2 for no \n"))
    if question == 1:
        total = 800000
        final_draft = final_draft + "\n Minimum Payment: $800'000"
    elif question == 2:
        total = 400000
        final_draft = final_draft + "\n Minimum Payment: $400'000"
    question = int(input("Were at lest 4 settlement cleared? \n Choices: \n Type 1 for yes \n Type 2 for no \n"))
    if question == 1:
        total += 100000
        final_draft = final_draft + "\n 4+ Settlements cleared: $100'000"
    question = int(input("How many main bases were cleared? \n Type the number below \n"))
    total += question * 250000
    final_draft = final_draft + f"\n {question}x Main Bases cleared: $" + number_divider(question * 250000)
    question = int(input("Was 1 wave held in at least 5 locations? \n Choices: \n Type 1 for yes \n Type 2 for no \n"))
    if question == 1:
        total += 200000
        final_draft = final_draft + "\n Waves held: $200'000"
    question = int(input("How many main bases were held for 2+ waves? \n"))
    if question == 1 :
        total += question * 500000
        final_draft = final_draft + f"{question}x Main Bases held for 2+ waves: ${number_divider(question * 500000)} \n "
    final_draft = final_draft + f"\n \n *Sub-Total: $" + number_divider(total) + "*"
    # All penalities are calculated below from here on
    final_draft = final_draft + " \n \n **KIA Penalities**"
    question = int(input("How many KIA's? \n"))
    total -= question * 75000
    final_draft = final_draft + f"\n {question}x KIA's: -$" + number_divider(question * 75000)
    if question == 0:
        total += 200000
        final_draft = final_draft + "\n 0 KIA's Bonus: $200'000"
    elif question >= 4 and question <= 7:
       total -= 300000
       final_draft = final_draft + "\n 4-7 KIA's: -$300'000"
    elif question >= 8 and question <= 11:
        total -= 500000
        final_draft = final_draft + "\n 8-11 KIA's: -$500'000"
    elif question > 12:
        total -= 700000
        final_draft = final_draft + "\n 12+ KIA's: -$700'000"
    question = int(input("How many VDIA's? \n"))
    if question == 0:
        total += 150000
        final_draft = final_draft + "\n 0 VDIA's Bonus: $150'000"
    elif question >= 1 and question <= 2:
        total -= 200000
        final_draft = final_draft + "\n 1-2 VDIA's: -$200'000"
    elif question >= 3 and question <= 5:
        total -= 400000
        final_draft = final_draft + "\n 3-5 VDIA's: -$400'000"
    elif question >= 6:
        total -= 600000
        final_draft = final_draft + "\n 6+ VDIA's: -$600'000"
#Totals and final formatting
    if total >= 0:
        final_draft = final_draft + f"\n \n **Total: ${number_divider(total)}**"
    else:
        total = total * -1
        final_draft = final_draft + f"\n \n **Total: -${number_divider(total)}**"
    return final_draft

#User callings
query = int(input(" Type 1 or 2 to select \n 1: Patrol \n 2: Hardcore Patrol \n 3: Divisional Patrol \n"))
if query == 1:
    print(patrol_calculator())
elif query == 2:
    print(hardcore_calculator())
elif query == 3:
    print(divisional_calculator())







#This is a automation for financial agents. This code belongs to AxaQuilPre. Any reproduction or inauthorized use is prohibited. 
