if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)



input_question = "def foo 3 /n def bar 7 /n calc foo + bar = /n def is 4 /n def fun 8 /n def programming 10 /n calc programming - is + fun = /n def fun 1 /n calc programming - is + fun = /n clear /n calc programming - is + fun ="

def define_words(input_question):
    key_value = {}
    value_key = {}

    def dictionary(words, key_value, value_key):
        key_value[words[1]] = int(words[2])
        value_key[int(words[2])] = words[1]
        return key_value, value_key

    def create_line(words, key_value, value_key):
        result = 0
        res_unkonwn = False

        line = ''
        for i in range(1, len(words)):
            if words[i] in key_value:
                if words[i-1] == '+' or words[i-1] == 'calc':
                    result += key_value[words[i]]
                elif words[i-1] == '-':
                    result -= key_value[words[i]]
            elif words[i] != '=' and words[i] != '+' and words[i] != '-':
                res_unkonwn = True
            line += words[i] + ' '
        
        if result in value_key and not res_unkonwn:
            line += value_key[result]
        else:
            line += 'unknown'
        
        print(line)

        return key_value, value_key

    
    lines = input_question.split('/n')
    for line in lines:
        words = line.split()
        if words[0] == 'def':
            key_value, value_key = dictionary(words, key_value, value_key)
        elif words[0] == 'calc':
            key_value, value_key = create_line(words, key_value, value_key)
        else:
            key_value = {}
            value_key = {}

define_words(input_question)