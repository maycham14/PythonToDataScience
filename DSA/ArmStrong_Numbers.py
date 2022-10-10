
def arm_strong(self ,m ,n):

        for num in range(m ,n):
          sum = 0
          temp = num
          while temp > 0:
              digit = temp % 10
              sum += digit
              # temp // =10
              if sum == num:
                  print(num)
