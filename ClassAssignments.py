class SubfieldsInAI():
    def Subfields():
        print("Sub-fields in AI are: \n Machine Learning \n Neural Networks \n Vision \n Robotics \n Speech Processing \n Natural Language Processing \n")
# SubfieldsInAI.Subfields()
# # ==============Oddeven========
# class OddEven():
    def OddEven():
        n=int(input("Enter a number" ))
        if(n%2==0):
            print(n,"is a Even number")
        else:
            print(n,"is a Odd number")
# OddEven.OddEven()
# # ==============Eligibilllity========
# class EligibilltyForMarriage():
    def Eligible():
        n = int(input("Your Age:" ))
        m = input("Your Gender:" )

        if(n>18):
            print("Not Eligible")
        else:
            print("Eligible")
# EligibilltyForMarriage.Eligible()
# # ==============percentage========
# class FindPercent():
    def percentage():
        sub1=int(input("Subject1 marks" ))
        sub2=int(input("Subject2 marks" ))
        sub3=int(input("Subject3 marks" ))
        sub4=int(input("Subject4 marks" ))
        sub5=int(input("Subject5 marks" ))
        Total = sub1+sub2+sub3+sub4+sub5
        Percentage = (Total/5)
        print("Percentage", Percentage)
# FindPercent.percentage()
# # ==============triangle========
# class triangle():
    def triangle(): 
        Height = int(input("Height:" ))
        Breadth = int(input("Breadth:" ))
        Area=(Height*Breadth)/2
        print(f'Area of Traingle: {Area:.1f}')

        Height1 = int(input("Height:" ))
        Height2 = int(input("Height:" ))
        Breadth1 = int(input("Breadth:" ))
        Area1=Height1+Height2+Breadth
        print("Perimeter of Triangle:", Area1)

# triangle.triangle()