def split_and_join(sentence):   
    w= sentence.split(" ")   
    return "-".join(w) 

if __name__ == '__main__':
    sentence = input() 
    result = split_and_join(sentence) 
    print(result)
