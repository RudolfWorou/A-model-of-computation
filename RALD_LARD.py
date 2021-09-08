class RALD_LARD_model():
    def __init__(self,inputs=[0]):  # inputs ex [4]
        self.inputs=inputs
        self.inputs_format=['O' + n*'C' for n in inputs]
        self.outputs = inputs
        self.outputs_format = ['O' + n*'C' for n in inputs]
    def apply_instructions(self,instructions):   #intructions [D,L,index input]
        n_steps=0
        l=len(instructions)
        i_index=0
        while True :
            instruction=instructions[i_index]

            i = instruction[2]
            if instruction[0]=='D' and instruction[1]=='R' : 
                o_index = self.outputs_format[i].index('O')
                n=len(self.outputs_format[i])
                if o_index == n - 1:
                    break
                else:
                    
                    self.outputs_format[i]=self.outputs_format[i][: n -1]
                    print(self.outputs_format[i])

            if instruction[0]=='A' and instruction[1]=='R' : 
                self.outputs_format[i]+='C'
                print(self.outputs_format[i])
            
            if instruction[0]=='A' and instruction[1]=='L' : 
                self.outputs_format[i]='C' + self.outputs_format[i]
                print(self.outputs_format[i])

            if instruction[0]=='D' and instruction[1]=='L' : 
                o_index = self.outputs_format[i].index('O')
                
                if o_index == 0:
                    break
                else:
                    
                    self.outputs_format[i]=self.outputs_format[i][1:]
                    print(self.outputs_format[i])



            i_index=(i_index+1)%l

            print('end')
            
            


