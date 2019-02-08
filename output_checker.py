import os.path
import sys
args = sys.argv

output_name = args[1] + "/results/Prob" + args[2] + "_res.txt"
ans_name =  args[1] + "/Outputs/JudgingOutputs/Prob" + args[2] + ".out.txt"

while not os.path.exists(output_name):
   output_name = raw_input("File does not exist. Please enter a valid file name.  ")

infile_out = open(output_name, 'r')
infile_ans = open(ans_name, 'r')
output_text = infile_out.read()
ans_text = infile_ans.read()

infile_out.close()
infile_ans.close()

output = output_text.split("\n")
ans = ans_text.split("\n")

print("{0:<50} {1:>50}".format("Output", "Answers"))
print("-----------------------------------------------------------------------------------------------------------------")

for i in range(0, len(output) - 1):
    check = str(output[i] == ans[i])
    print("{0:<50} {1:>50} {2:>20}".format(output[i], ans[i], check))
    
    
