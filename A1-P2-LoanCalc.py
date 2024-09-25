#Program 2 – Weekly Loan Calculator
#Develop a short term loan calculator program as a console application 

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    #Display Program Name
    print("Weekly Loan Calculator\n")

    #Enter the amount of the loan
    loan_amount = float(input("Enter the amount of the loan: "))

    #Enter the interest rate (%)
    interest_rate = float(input("Enter the interest rate (%): "))

    #Enter the number of years
    years = int(input("Enter the number of years: "))
    print("")

    #Display total numbers of years
    i = interest_rate / 5200 #using i from the formula in the assisnment 1 document for program two
    weekly_payment = (i / (1-(1+i)**(-52*years))) * loan_amount
    print("Your weekly payment will be: ${0:.2f}".format(weekly_payment))
    



    # YOUR CODE ENDS HERE

main()