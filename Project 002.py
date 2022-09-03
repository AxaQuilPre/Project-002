#Following definiton will cover the patrol calculations.
def patrol_calculator():
    final_drawft = "**Contracted Patrol by (name)** \n **Bonuses**"
    question = int(input("Did the event take over 40 minutes? \n Choices: \n Type 1 for yes \n Type 2 for no \n"))
    if question == 1:
        total = 375000
        final_drawft = final_drawft + "\n Minimum Payment: $375'000"
    elif question == 2:
        total = 250000
        final_drawft = final_drawft + "\n Minimum Payment: $250'000"
    question = int(input("Were at lest 4 settlement cleared? \n Choices: \n Type 1 for yes \n Type 2 for no \n"))
    if question == 1:
        total += 50000
        final_drawft = final_drawft + "\n 4+ Settlements cleared: $50'0000"
    question = int(input("How many main bases were cleared? \n Type the number below \n"))
    total += question * 100000
    final_drawft = final_drawft + f"\n {question}x Main Bases cleared: ${question * 100000}"
    question = int(input("Was 1 wave held in at least 4 locations? \n Choices: \n Type 1 for yes \n Type 2 for no \n"))
    if question == 1:
        total += 100000
        final_draft = final_drawft + "\n Waves held: $100'000"
    final_draft = final_draft + f"\n *Sub-Total: {total}*"
    final_draft = final_draft + " \n \n **KIA Penalities**"
    question = int(input("How many KIA's? \n"))
    total -= question * 50000
    final_drawft = final_drawft + f"\n {question}x KIA's: -${question * 100000}"





#This is a automation for financial agents. This code belongs to AxaQuilPre. Any reproduction or inauthorized use is prohibited. CCC-33e3S3-ddfm